from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, current_timestamp
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType
import time

# ----------------------------
# Config
# ----------------------------
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"
KAFKA_TOPIC = "events"

POSTGRES_URL = "jdbc:postgresql://postgres:5432/platform_db"
POSTGRES_PROPERTIES = {
    "user": "platform_user",
    "password": "platform_pass",
    "driver": "org.postgresql.Driver"
}

# ----------------------------
# Spark Session
# ----------------------------
spark = SparkSession.builder \
    .appName("AdaptiveStreamingETL") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("🚀 Spark Streaming Started...")

# ----------------------------
# Schema
# ----------------------------
event_schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("event_type", StringType(), True),
    StructField("amount", DoubleType(), True)
])

# ----------------------------
# Read Kafka
# ----------------------------
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

json_df = raw_df.selectExpr("CAST(value AS STRING)")

parsed_df = json_df.select(
    from_json(col("value"), event_schema).alias("data")
).select("data.*")

final_df = parsed_df.withColumn("processed_at", current_timestamp())

# ----------------------------
# Write to Postgres
# ----------------------------
def write_to_postgres(batch_df, batch_id):

    row_count = batch_df.count()

    if row_count > 0:
        batch_df.write.jdbc(
            url=POSTGRES_URL,
            table="processed_events",
            mode="append",
            properties=POSTGRES_PROPERTIES
        )

    print(f"Batch {batch_id} | Rows: {row_count}")

query = final_df.writeStream \
    .foreachBatch(write_to_postgres) \
    .outputMode("append") \
    .trigger(processingTime="5 seconds") \
    .start()

query.awaitTermination()

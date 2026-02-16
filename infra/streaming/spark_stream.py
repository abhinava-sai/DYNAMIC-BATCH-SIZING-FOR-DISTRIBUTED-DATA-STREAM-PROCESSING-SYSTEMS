from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, IntegerType, StringType, DoubleType

spark = SparkSession.builder \
    .appName("AdaptiveStreamingETL") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("event_type", StringType()) \
    .add("amount", DoubleType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "events") \
    .option("startingOffsets", "latest") \
    .load()

parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = parsed.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()

query.awaitTermination()

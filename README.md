# Dynamic Batch Sizing for Distributed Data Stream Processing Systems

**Production-grade real-time streaming architecture with adaptive batch control and observability.**

---

## 📖 Project Overview
This project implements an end-to-end distributed data platform designed to handle real-time event ingestion, processing, and monitoring. The core innovation focuses on solving the "Static Batch" problem—where fixed intervals cause latency during low load and backpressure during spikes—by introducing **Adaptive Batch Control** and full-stack observability.

### The Objective:
* Build a scalable, decoupled streaming pipeline.
* Introduce rule-based (ML-ready) logic to adjust batch sizing.
* Achieve deep system visibility using the Prometheus/Grafana stack.

---

## 🏗 System Architecture
The system follows a modern event-driven design, fully containerized via Docker:



1.  **Ingestion:** FastAPI REST endpoints receive events and produce to Kafka.
2.  **Buffering:** Apache Kafka decouples the producer from the processing engine.
3.  **Processing:** Spark Structured Streaming performs ETL, schema enforcement, and enrichment.
4.  **Storage:** PostgreSQL stores both processed business data and system performance metrics.
5.  **Observability:** Prometheus scrapes metrics which are visualized in real-time via Grafana.

---

## 🛠 Tech Stack
| Layer | Technology |
| :--- | :--- |
| **API / Ingestion** | FastAPI, Uvicorn |
| **Message Broker** | Apache Kafka |
| **Stream Processing** | Apache Spark (Structured Streaming) |
| **Database** | PostgreSQL |
| **Observability** | Prometheus, Grafana |
| **Infrastructure** | Docker, Docker Compose |

---

## 🚀 Key Features
* **Real-time Event Ingestion:** High-throughput ingestion simulated via FastAPI.
* **Streaming ETL Pipeline:** Distributed JSON parsing and timestamp enrichment.
* **Batch Metrics Tracking:** Granular logging of row counts and processing duration for every micro-batch.
* **Dynamic Batch Controller:** Logic designed to monitor system health and suggest optimal batch intervals.
* **Fault Tolerance:** Implemented using Kafka offsets and Spark micro-batch retry mechanisms.

---

## 📊 Monitoring & Observability
The project includes a custom **Grafana Dashboard** that provides real-time insights into:
* **Throughput:** Events processed per second.
* **Batch Latency:** Time taken to complete each Spark micro-batch.
* **System Health:** Service uptime and resource consumption.

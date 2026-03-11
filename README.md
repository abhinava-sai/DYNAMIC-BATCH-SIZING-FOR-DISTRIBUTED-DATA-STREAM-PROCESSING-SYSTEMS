Dynamic Batch Sizing for Distributed Data Stream Processing Systems

A production-style real-time streaming architecture with adaptive batch control, monitoring, and distributed event processing.

📖 Project Overview

This project implements an end-to-end distributed data streaming platform designed to handle real-time event ingestion, processing, and monitoring.

Traditional streaming systems often rely on static micro-batch intervals, which can lead to inefficiencies such as higher latency during low load or system bottlenecks during peak traffic. To address this, the system introduces an Adaptive Batch Controller that dynamically adjusts processing intervals based on system workload and performance metrics.

The platform integrates Apache Kafka, Spark Structured Streaming, PostgreSQL, Prometheus, and Grafana to simulate a modern real-time data infrastructure similar to those used in large-scale production systems.

Project Goals

Build a scalable and decoupled streaming data pipeline

Implement adaptive batch sizing logic for improved system efficiency

Enable real-time monitoring and observability

Demonstrate a distributed streaming architecture using containerized services

🏗 System Architecture

The system follows an event-driven microservices architecture fully containerized using Docker.

Users / Clients
      ↓
FastAPI Ingestion Service
      ↓
Apache Kafka (Event Streaming Layer)
      ↓
Spark Structured Streaming (Real-time ETL Processing)
      ↓
Adaptive Batch Controller (Rule-Based + ML Ready)
      ↓
PostgreSQL (Processed Data + Metrics)
      ↓
Prometheus (Monitoring)
      ↓
Grafana (Visualization Dashboard)
Pipeline Workflow

Event Ingestion

Client events are sent to a FastAPI REST endpoint.

Event Streaming

Events are published to Kafka topics which act as a distributed event buffer.

Stream Processing

Spark Structured Streaming consumes events from Kafka and performs:

JSON parsing

Data transformation

Timestamp enrichment

Batch processing

Data Storage

Processed events and system metrics are stored in PostgreSQL.

Adaptive Batch Control

A rule-based controller (ML-ready) analyzes processing metrics and recommends optimal batch intervals.

Monitoring

Prometheus collects system metrics.

Visualization

Grafana dashboards visualize throughput, latency, and system performance.

🛠 Technology Stack
Layer	Technology
API / Ingestion	FastAPI, Uvicorn
Streaming Platform	Apache Kafka
Stream Processing	Apache Spark (Structured Streaming)
Database	PostgreSQL
Monitoring	Prometheus
Visualization	Grafana
Infrastructure	Docker, Docker Compose
Adaptive Controller	Python (Rule-based + ML-ready logic)
🚀 Key Features
Real-Time Event Streaming

High-throughput event ingestion using FastAPI and Kafka.

Distributed ETL Processing

Spark Structured Streaming performs real-time transformation and enrichment of incoming events.

Adaptive Batch Controller

Implements rule-based logic with ML-ready architecture to dynamically recommend optimal micro-batch intervals.

Batch Metrics Tracking

Each micro-batch records:

Row counts

Processing duration

System performance metrics

Fault Tolerance

System resilience is ensured through:

Kafka offset management

Spark micro-batch retry mechanisms

Decoupled streaming architecture

Containerized Infrastructure

All services run inside Docker containers ensuring portability and reproducibility.

📊 Monitoring & Observability

The system includes a full monitoring stack.

Prometheus

Collects metrics from system components including processing performance.

Grafana Dashboard

Provides visual insights into:

Event throughput

Spark micro-batch latency

System health

Processing trends

This observability layer allows operators to monitor pipeline behavior in real time.

📁 Project Structure
adaptive-streaming-platform
│
├── controller
│   ├── adaptive_batch_controller.py
│   └── system_controller.py
│
├── streaming
│   └── spark_stream.py
│
├── services
│   └── ingestion
│       ├── Dockerfile
│       ├── requirements.txt
│       └── app
│           ├── main.py
│           └── kafka.py
│
├── infra
│   ├── docker-compose.yml
│   └── prometheus
│       └── prometheus.yml
│
└── README.md
🔬 Research Inspiration

This project is inspired by the research paper:

Nwe Ni Hlaing, Si Si Mar Win
Dynamic Batch Sizing for Distributed Data Stream Processing Systems
University of Computer Studies, Yangon, Myanmar.

The research explores how dynamic batch sizing can improve performance in distributed streaming environments.

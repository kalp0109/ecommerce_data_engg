# E-Commerce Data Engineering Pipeline

An end-to-end **E-Commerce Data Engineering project** built using **Databricks, PySpark, Delta Lake, Kafka, Auto Loader, CDC, and Unity Catalog**.

The project demonstrates how batch and real-time e-commerce data can be ingested, transformed, processed using CDC, and converted into business-ready analytics in a Databricks Lakehouse architecture.

## 🏗️ Architecture

```text
                         E-COMMERCE DATA SOURCES
                                  │
                 ┌────────────────┴────────────────┐
                 │                                 │
            BATCH DATA                       STREAMING DATA
                 │                                 │
        customers.csv                        Kafka Producers
        products.csv                         Order Events
        orders.csv                           CDC Events
        delivery.csv                              │
                 │                                 │
                 └────────────────┬────────────────┘
                                  ↓
                         DATABRICKS / PYSPARK
                                  │
                         UNITY CATALOG
                                  │
                                  ↓
                         ┌─────────────────┐
                         │  BRONZE LAYER   │
                         │                 │
                         │ Raw Ingestion   │
                         │ Batch + Stream  │
                         │ Auto Loader     │
                         └────────┬────────┘
                                  ↓
                         ┌─────────────────┐
                         │  SILVER LAYER   │
                         │                 │
                         │ Cleaning        │
                         │ Transformations │
                         │ CDC Processing  │
                         │ MERGE / Upsert  │
                         └────────┬────────┘
                                  ↓
                         ┌─────────────────┐
                         │   GOLD LAYER    │
                         │                 │
                         │ Business        │
                         │ Analytics       │
                         │ Revenue Metrics │
                         └────────┬────────┘
                                  ↓
                       DATABRICKS DASHBOARD
```

## 🚀 Project Highlights

* Batch data ingestion using CSV files
* Real-time streaming using Kafka
* Change Data Capture (CDC) processing
* CDC `INSERT` and `UPDATE` operations
* Delta Lake tables
* Auto Loader for file-based streaming ingestion
* Bronze, Silver and Gold data layers
* Data cleansing and transformations using PySpark
* Delta `MERGE` for CDC/upsert processing
* Unity Catalog for data organization and governance
* Gold-layer business metrics
* Databricks Dashboard for analytics
* Python/Faker-based synthetic e-commerce data generation

## 🛠️ Technologies

| Technology           | Purpose                                 |
| -------------------- | --------------------------------------- |
| Python               | Data generation and streaming producers |
| Faker                | Synthetic e-commerce data generation    |
| Apache Kafka         | Real-time event streaming               |
| PySpark              | Data processing and transformations     |
| Databricks           | Lakehouse processing platform           |
| Delta Lake           | Reliable storage and upserts            |
| Auto Loader          | Incremental file ingestion              |
| Unity Catalog        | Data organization and governance        |
| Databricks SQL       | Analytics and reporting                 |
| Databricks Dashboard | Data visualization                      |
| GitHub               | Version control                         |

## 📂 Project Structure

```text
ecommerce_data_engg/
│
├── batch_data/
│   ├── customers.csv
│   ├── delivery.csv
│   ├── orders.csv
│   └── products.csv
│
├── data_generation/
│   ├── generate_customers.py
│   ├── generate_delivery.py
│   ├── generate_orders.py
│   └── generate_products.py
│
├── data_streaming/
│   ├── .gitignore
│   ├── order_producer.py
│   ├── scs_test_producer
│   └── cdc_test
│
├── databricks/
│   └── notebooks/
│       ├── 01_bronze_ingestion.py
│       ├── 02_silver_layer.py
│       ├── 03_gold_layer.py
│       ├── 04_streaming_data.py
│       ├── 05_auto_loader_brz.py
│       └── 06_auto_loader_slv.py
│
├── architecture/
│   └── architecture_diagram
│
└── README.md
```

## 🔄 Data Pipeline

### 1. Data Generation

Synthetic e-commerce data is generated using Python and Faker.

The generated datasets include:

* Customers
* Products
* Orders
* Delivery information

The data is stored as CSV files for batch processing.

### 2. Batch Ingestion

Batch CSV data is ingested into Databricks and stored in the Bronze layer using Delta Lake.

The Bronze layer preserves the raw ingested data before further processing.

### 3. Streaming Ingestion

Real-time order events are generated using Python producers and sent through Kafka.

The streaming pipeline consumes these events and processes them using Spark Structured Streaming.

### 4. Auto Loader

Databricks Auto Loader is used for incremental ingestion of newly arriving files.

This enables the pipeline to automatically detect and process new data without manually reprocessing existing files.

### 5. Silver Layer

The Silver layer performs:

* Data cleansing
* Type conversions
* Null handling
* Deduplication
* Business transformations
* CDC processing

### 6. Change Data Capture

CDC events are processed using Spark Structured Streaming and Delta Lake.

For applicable CDC events, the pipeline uses `MERGE` logic to update existing records or insert new records.

Example:

```text
CDC INSERT
    ↓
New order inserted

CDC UPDATE
    ↓
Existing order identified
    ↓
Delta MERGE
    ↓
Existing record updated
```

### 7. Gold Layer

The Gold layer contains business-ready analytical data.

Examples include:

* Daily revenue
* Order metrics
* Customer analytics
* Product performance

These datasets are optimized for reporting and visualization.

### 8. Dashboard

The Gold-layer data is used to create a **Databricks Dashboard** for business analysis and visualization.

## 📊 CDC Demonstration

The project demonstrates CDC processing using an order event.

Example:

```text
Initial Order
ORD999999
Quantity = 2

        ↓

CDC UPDATE EVENT

        ↓

Delta MERGE

        ↓

Updated Order
ORD999999
Quantity = 3
```

This demonstrates how changes in an incoming event can be propagated to the analytical Delta table.

## 🔐 Data Governance

The project uses **Unity Catalog** to organize and manage data assets within the Databricks environment.

The Lakehouse follows a layered structure:

```text
Catalog
   │
   └── Schema
         │
         ├── Bronze
         ├── Silver
         └── Gold
```

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Modern Data Engineering architecture
* Batch ETL pipelines
* Real-time streaming pipelines
* Kafka
* Spark Structured Streaming
* Change Data Capture
* Delta Lake
* Delta MERGE
* Auto Loader
* Medallion Architecture
* Unity Catalog
* PySpark transformations
* Databricks analytics

## 👩‍💻 Author

**Kalpana Pandit**

Data Engineering | Python | SQL | PySpark | Databricks | Kafka | Delta Lake

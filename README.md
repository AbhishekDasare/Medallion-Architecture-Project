# Medallion Architecture Project

## Overview

This project demonstrates the Medallion Architecture pattern using PySpark. The pipeline processes customer data through Bronze, Silver, and Gold layers to improve data quality and generate business insights.

## Technology Stack

- Python
- PySpark
- Apache Spark
- Git
- GitHub

## ETL Process

### Bronze Layer
- Reads raw customer data
- Stores source data with minimal transformation
- Acts as the landing layer

### Silver Layer
- Cleans and validates records
- Removes null values
- Standardizes data structure

### Gold Layer
- Performs business aggregations
- Calculates total sales by city
- Generates reporting-ready datasets

## Business Logic

```python
total_sales = SUM(amount) GROUP BY city
```

## Key Features

- Medallion Architecture
- Bronze, Silver, Gold Layers
- Data Validation
- Data Transformation
- Business Aggregation
- PySpark Processing

## Future Enhancements

- Delta Lake Integration
- Databricks Implementation
- Incremental Data Loading
- Data Quality Framework
- AWS S3 Storage
- Dashboard Integration

## Author

Abhishek Dasare

Data Engineer | PySpark | AWS | Databricks

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Bronze Layer").getOrCreate()

df = spark.read.csv(
    "data/raw/customer_data.csv",
    header=True,
    inferSchema=True
)

df.write.mode("overwrite").csv(
    "data/bronze",
    header=True
)

spark.stop()

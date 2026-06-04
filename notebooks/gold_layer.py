from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("Gold Layer").getOrCreate()

df = spark.read.csv(
    "data/silver",
    header=True,
    inferSchema=True
)

gold_df = df.groupBy("city").agg(
    sum("amount").alias("total_sales")
)

gold_df.write.mode("overwrite").csv(
    "data/gold",
    header=True
)

spark.stop()

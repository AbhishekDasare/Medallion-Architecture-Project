from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Silver Layer").getOrCreate()

df = spark.read.csv(
    "data/bronze",
    header=True,
    inferSchema=True
)

df = df.dropna()

df.write.mode("overwrite").csv(
    "data/silver",
    header=True
)

spark.stop()

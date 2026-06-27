#TODO: steps:
    #1) load postgres data into here
    #2) write spark script to manipulate the data
    #3) send the manipulated data to bigquery 


from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder\
        .appName("PostgresToBigQuery")\
        .config("spark.jars", "/Users/jasminemarwaha/Documents/ETL_pipeline/postgresql-42.7.3.jar") \
        .getOrCreate()

# data_csv = (
#     spark
#     .read
#     .format("csv")
#     .option("header", "true")
#     .option("inferSchema", "true")
#     .load("./csv_files/*.csv")
# )
df = (
    spark
    .read
    .format("jdbc")
    .option("url", "jdbc:postgresql://localhost:5432/db123")
    .option("dbtable", "employees")
    .option("user", "user123")
    .option("password", "password123")
    .option("driver", "org.postgresql.Driver")
    .load()
)

df_manipulated = (
    df.withColumn("status", F.lit("On Leave"))
)
df_manipulated.show(10)




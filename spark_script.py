#TODO: steps:
    #1) load postgres data into here
    #2) write spark script to manipulate the data
    #3) send the manipulated data to bigquery 


from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder\
        .appName("PostgresToBigQuery")\
        .getOrCreate()

data_csv = (
    spark
    .read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("./csv_files/*.csv")
)
#using jdbc to read/write from databases
# jdbc_url = "jdbc:postgresql://<YOUR_POSTGRES_HOST>:<PORT>/<DATABASE_NAME>"
# jdbc_connection_properties = {
#     "user": "<YOUR_USERNAME>",
#     "password": "<YOUR_PASSWORD>",
#     "driver": "org.postgresql.Driver"
# }
# #writing the local csv files to postgres
# data_csv.write \
#     .jdbc(url=jdbc_url, table="raw_csv_data", mode="overwrite", properties=jdbc_connection_properties)
# #reading those files from postgres into spark
# df_postgres = spark.read \
#     .jdbc(url=jdbc_url, table="raw_csv_data", properties=jdbc_connection_properties)

df_manipulated = (
    data_csv.withColumn("status", F.lit("On Leave"))
)
df_manipulated.show(10)




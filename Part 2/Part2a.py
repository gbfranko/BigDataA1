import findspark
findspark.init('/home/ubuntu/spark-3.3.1-bin-hadoop3')

findspark.find()

from pyspark.sql import SparkSession

# The entry point into all functionality in Spark is the SparkSession class.
spark = (SparkSession
         .builder
         .appName("Data Sorter")
         .master("spark://172.31.47.167:7077")
         .getOrCreate())

# Read the file in
df = spark.read.load("hdfs://172.31.47.167:9000/export.csv", format = 'csv', inferSchema = 'true', sep = ',', header='true')

#Sort the dataset, first by cca2 then by the timestamp
df1 = df.sort('cca2', 'timestamp')

#Saves the sorted file as a csv
df1.write.format("csv").save("hdfs://172.31.47.167:9000/new.csv")

spark.stop()

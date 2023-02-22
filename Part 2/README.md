Make sure hadoop and Spark are started up. 
Make sure export.csv is coppied to from local into hadoop
Run spark submit code: bin/spark-submit hdfs://172.31.47.167:9000/Assignment1.py hdfs://172.31.47.167:9000/export.csv hdfs://172.31.47.167:9000/new.csv

Input is the export.csv file 
Output is new.csv 

This new.csv is the export.csv sorted first by caa2 and then by timestamp 

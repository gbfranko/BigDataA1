# Setup
- Make sure hadoop and Spark are started up     
- Make sure export.csv is coppied to from local into hadoop 
- In the master incstance, cd into the spark directory 
- Run spark submit code: bin/spark-submit hdfs://172.31.47.167:9000/Assignment1.py hdfs://172.31.47.167:9000/export.csv hdfs://172.31.47.167:9000/new.csv 
- For the export.csv and new.csv parts of above, they can be named whatever you want them to, just make sure export is same as input code. 

# Input/Output
- Input is the export.csv file
- Output is new.csv 
- Same as above where they can be named differently depending on your preference 

# Purpose 
- This new.csv is the export.csv sorted first by caa2 and then by timestamp 

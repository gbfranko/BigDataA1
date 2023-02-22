# Setup
- Make sure hadoop and Spark are started up     
- Make sure web-BerkStan.txt is coppied to from local into hadoop 
- In the master incstance, cd into the spark directory 
- Run spark submit code: bin/spark-submit hdfs://172.31.47.167:9000/Part3Task2.py hdfs://172.31.47.167:9000/web-BerkStan.txt hdfs://172.31.47.167:9000/part_output.csv 
- For the web-BerkStan.txt and part_output.csv parts of above, they can be named whatever you want them to, just make sure export is same as input code. 

# Input/Output
- Input is the web-BerkStan.txt file
- Output is part_output.csv 
- Same as above where they can be named differently depending on your preference 

# Purpose 
- This part_output.csv is the web-BerkStan.txt with page rank done with partitions 

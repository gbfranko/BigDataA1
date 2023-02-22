# Setup
- Make sure hadoop and Spark are started up     
- Make sure web-BerkStan.txt is coppied to from local into hadoop 
- In the master incstance, cd into the spark directory 
- Run spark submit code: bin/spark-submit hdfs://172.31.47.167:9000/Part3Task3.py hdfs://172.31.47.167:9000/web-BerkStan.txt hdfs://172.31.47.167:9000/killed_output.csv 
- For the web-BerkStan.txt and killed_output.csv parts of above, they can be named whatever you want them to, just make sure export is same as input code. 

# Input/Output
- Input is the web-BerkStan.txt file
- Output is killed_output.csv 
- Same as above where they can be named differently depending on your preference 

# Purpose 
- This killed_output.csv is the web-BerkStan.txt with page rank done 
- Same code as Part 3 Task 1, just when we run this one we were supposed to kill one of the workers.  

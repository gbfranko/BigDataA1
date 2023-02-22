# Setup
- Make sure hadoop and Spark are started up     
- Make sure web-BerkStan.txt is coppied to from local into hadoop 
- In the master incstance, cd into the spark directory 
- Run spark submit code: bin/spark-submit hdfs://172.31.47.167:9000/Part3Task1.py hdfs://172.31.47.167:9000/web-BerkStan.txt hdfs://172.31.47.167:9000/prank_output.csv 
- For the export.csv and new.csv parts of above, they can be named whatever you want them to, just make sure export is same as input code. 

# Input/Output
- Input is the web-BerkStan.txt file
- Output is prank_output.csv 
- Same as above where they can be named differently depending on your preference 

# Purpose 
- This prank_output.csv is the updated page rank of web-BerkStan.txt using Page Rank algorithm 

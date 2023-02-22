import findspark
findspark.init('/home/ubuntu/spark-3.3.1-bin-hadoop3')

findspark.find()

import re
import sys
from operator import add
from typing import Iterable, Tuple

from pyspark.resultiterable import ResultIterable
from pyspark.sql import SparkSession
import pyspark
from pyspark.sql import functions as sf

"""Helper function to calculates URL contributions to the rank of other URLs"""
def computeContribs(urls: ResultIterable[str], rank: float) -> Iterable[Tuple[str, float]]:
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)

        
"""Helper function to parses a urls string into urls pair"""
def parseNeighborURLs(urls: str) -> Tuple[str, str]:
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]



if __name__ == "__main__":
    # A baseline implementation should take three command-line arguments except the python code
    # You can extend this by including however many arguments you want
    #if len(sys.argv) != 4:
        #print("Usage: pagerank <path_to_input> <path_to_output> <iterations>", file=sys.stderr)
        #sys.exit(-1)

    # Initialize the Spark context
    spark = SparkSession\
        .builder\
        .appName("Page Rank")\
        .master("spark://172.31.47.167:7077")\
        .getOrCreate()


    # Loads in input file
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     ...
    
    
    
    #lines = spark.read.text(sys.argv[1]).rdd.map(lambda ir: r[0])
    lines = spark.sparkContext.textFile(sys.argv[1])

    links = lines.map(lambda urls: parseNeighborURLs(urls)).distinct().groupByKey()

    # Initialize a ranks RDD
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    # Calculates and updates URL ranks continuously using PageRank algorithm.
    for iteration in range(10):
        # Calculates URL contributions to the rank of other URLs.
        contribs = links.join(ranks).flatMap(lambda url_urls_rank: computeContribs(
            url_urls_rank[1][0], url_urls_rank[1][1]))  # type: ignore[arg-type] 

        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)


    # Dump output to HDFS
    ranksDf = ranks.toDF()
    # TODO: You should replace xxx with the private IPv4 address of your HDFS master
    ranksDf.write.format("csv").save("hdfs://172.31.47.167:9000/killed_output.csv")

    # You should always stop the Spark session when it's done
    spark.stop()

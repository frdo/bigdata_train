import pyspark_csv as pycsv
from pyspark.sql import SQLContext

def init_sqlcontext(sc):
    sc.addPyFile('pyspark_csv.py')
    sqlc = SQLContext(sc)
    return sqlc

def main(sc):
    # Create RDD loading the CSV file located in Hadoop	HDFS
    rdd_iris = sc.textFile("hdfs://localhost/user/iris.csv")

    sqlc = init_sqlcontext(sc)

    # Create the DataFrame using pyspark_csv libraries
    # pyspark_csv on github -> https://github.com/seahboonsiew/pyspark-csv
    dataframe_iris = pycsv.csvToDataFrame(sqlc, rdd_iris)

    # Returns all column names and their data types as a list
    #df_iris.dtypes

    # Print out	the schema in the three	format
    #df_iris.printSchema()

    # Calculates the mean on "Sepal Length" column grouping by "Species" column
    #df_iris.groupBy("Species").mean("Sepal Length").show()

    return dataframe_iris

if __name__ is "__main__":
    main()

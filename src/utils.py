from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

def get_spark_session(app_name="DataChallenge"):
    """
    Creates a SparkSession configured for Delta Lake.
    This mimics the Databricks runtime environment locally.
    """
    builder = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.sql.warehouse.dir", "./spark-warehouse")
    
    # Configure Spark with Delta packages
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    
    # Set logging to WARN to avoid cluttering the terminal
    spark.sparkContext.setLogLevel("WARN")
    
    return spark

class MockDBUtils:
    """
    A minimal mock for dbutils to allow candidates to use
    dbutils.fs.rm or similar commands without crashing.
    """
    class FS:
        def rm(self, path, recurse=False):
            import shutil
            import os
            if os.path.exists(path):
                if recurse:
                    shutil.rmtree(path)
                else:
                    os.remove(path)
            print(f"Mock DBUtils: Removed {path}")

    fs = FS()

# Instantiate for import
dbutils = MockDBUtils()

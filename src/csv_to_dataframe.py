import pandas as pd

def create_pandas_code(lines):
    header = lines[0].split(',')
    rows = [line.split(',') for line in lines[1:]]
    data_code = ',\n    '.join([str(tuple(row)) for row in rows])
    
    return f'''
import pandas as pd

data = [
    {data_code}
]

df = pd.DataFrame(data, columns={header})
df.head()
'''

def create_spark_code(lines):
    header = lines[0].split(',')
    rows = [line.split(',') for line in lines[1:]]
    data_code = ',\n    '.join([str(tuple(row)) for row in rows])

    schema_code = ', '.join([f"StructField('{col}', StringType(), True)" for col in header])

    return f'''
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName('ManualDataFrameCreation').getOrCreate()

data = [
    {data_code}
]

schema = StructType([
    {schema_code}
])

df = spark.createDataFrame(data, schema=schema)
df.show()

spark.stop()
'''

def main():
    csv_file_path = input("Please enter the path to the CSV file: ")
    dataframe_type = input("Would you like to create a Spark DataFrame or a Pandas DataFrame? (Enter 'spark' or 'pandas'): ").strip().lower()

    with open(csv_file_path, 'rt') as file:
        lines = file.readlines()

    if dataframe_type == 'pandas':
        code = create_pandas_code(lines)
    elif dataframe_type == 'spark':
        code = create_spark_code(lines)
    else:
        print("Invalid input. Please enter 'spark' or 'pandas'.")
        return

    output_option = input("Would you like to print the output or export it to a text file? (Enter 'print' or 'export'): ").strip().lower()

    if output_option == 'print':
        print("Here is your code:")
        print(code)
    elif output_option == 'export':
        export_file_path = input("Please enter the path and file name to export the text file: ")
        with open(export_file_path, 'wt') as export_file:
            export_file.write(code)
        print(f"Your code has been written to {export_file_path}")
    else:
        print("Invalid input. Please enter 'print' or 'export'.")
        
if __name__ == "__main__":
    main()

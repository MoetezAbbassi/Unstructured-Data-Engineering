from pyspark.sql import SparkSession
from config.config import configuration
from udf_utils import *
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType

def define_udfs():
    return{
        'extract_file_name_udf': udf(extract_file_name, StringType()),
        'extract_position_udf': udf(extract_file_name, StringType()),
        'extract_salary_udf': udf(extract_file_name, DoubleType()),
        'extract_date_udf': udf(extract_file_name, DateType()),
        'extract_classcode_udf': udf(extract_file_name, StringType()),
        'extract_requirements_udf': udf(extract_file_name, StringType()),
        'extract_notes_udf': udf(extract_file_name, StringType()),
        'extract_duties_udf': udf(extract_file_name, StringType()),
        'extract_end_date_udf': udf(extract_file_name, DateType()),
        'extract_selection_udf': udf(extract_file_name, StringType()),
        'extract_experience_length_udf': udf(extract_file_name, StringType()),
        'extract_education_length_udf': udf(extract_file_name, StringType()),
        'extract_sele_udf': udf(extract_file_name, StringType()),
        'extract_selection_udf': udf(extract_file_name, StringType())
    
    
    }

if __name__ == "__main__":
    spark = (SparkSession.builder.appName('AWS_Spark_Unstructured')
            .config('spark.jars.packages',
                     'org.apache.hadoop:hadoop-aws:3.3.1,',
                     'com.amazonaws:aws-java-sdk:1.11.469')
            .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
            .config('spark.hadoop.fs.s3a.access.key', configuration.get('AWS_ACCESS_KEY'))
            .config('spark.hadoop.fs.s3a.secret.key', configuration.get('AWS_SECRET_KEY'))
            .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
            .getOrCreate()
            )
    text_input_dir = 'C:\Users\Moetez\Desktop\Data Engineering projects\Unstructured Data Engineering\Unstructured-Data-Engineering\input\input_text'
    json_input_dir = 'C:\Users\Moetez\Desktop\Data Engineering projects\Unstructured Data Engineering\Unstructured-Data-Engineering\input\input_json'
    csv_input_dir = 'C:\Users\Moetez\Desktop\Data Engineering projects\Unstructured Data Engineering\Unstructured-Data-Engineering\input\input_csv'
    pdf_input_dir = 'C:\Users\Moetez\Desktop\Data Engineering projects\Unstructured Data Engineering\Unstructured-Data-Engineering\input\input_pdf'
    video_input_dir = 'C:\Users\Moetez\Desktop\Data Engineering projects\Unstructured Data Engineering\Unstructured-Data-Engineering\input\input_video'
    img_input_dir = 'C:\Users\Moetez\Desktop\Data Engineering projects\Unstructured Data Engineering\Unstructured-Data-Engineering\input\input_img'
    
    data_schema = StructType([
        StructField('file_name', StringType(), True),
        StructField('position', StringType(), True),
        StructField('classcode', StringType(), True),
        StructField('salary_start', DoubleType(), True),
        StructField('salary_end', DoubleType(), True),
        StructField('start_date', DateType(), True),
        StructField('end_date', DateType(), True),
        StructField('req', StringType(), True),
        StructField('notes', StringType(), True),
        StructField('duties', StringType(), True),
        StructField('selection', StringType(), True),
        StructField('experience_length', StringType(), True),
        StructField('job_type', StringType(), True),
        StructField('education_length', StringType(), True),
        StructField('school_type', StringType(), True),
        StructField('application_location', StringType(), True),
    ])

    udf= define_udfs()
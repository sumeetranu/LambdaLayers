import json
from pyarrow.parquet import ParquetDataset 
import s3fs

def lambda_handler(event, context):
    s3 = s3fs.S3FileSystem()
    dataset1 = ParquetDataset("s3://superpods-lambda-layer/userdata1.parquet", filesystem=s3) 
    dataset2= ParquetDataset("s3://superpods-lambda-layer/userdata1.parquet", filesystem=s3) 
    dataset3= ParquetDataset("s3://superpods-lambda-layer/wrongdata.parquet", filesystem=s3) 

    boolean_result_1v2 = dataset1.schema.equals(dataset2.schema)
    print("1 vs 2: " + str(boolean_result_1v2))
    boolean_result_1v3 = dataset1.schema.equals(dataset3.schema)
    print("1 vs 2: " + str(boolean_result_1v3))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
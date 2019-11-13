# Creating the layer
- Create a Lambda layer from aws-pyarrow-s3fs-numpy-layer.zip
- Use Python3.6 as the runtime
- Copy the ARN

# Creating the lambda
- Create a Lambda from scratch
- Use Python3.6 as the runtime
- Upload function.zip for the code
- Click on Layers and add a layer
- Select "provide a layer version ARN" and enter the ARN you copied earlier
- Save and test the function

# How I created the layer zip
- Open a python3.6 virtual environment
- Follow instructions here for file organization: https://dev.to/vealkind/getting-started-with-aws-lambda-layers-4ipk
- Install these 3 using pip3 install: pyarrow, numpy, s3fs
- Run these commands to trim unwanted files:
    - find .  -name '*.so' -exec strip {} \+
    - find .  -name '*__pycache__*' -exec rm -rf {} \+ 
    - find .  -name '*.dist-info*' -exec rm -rf {} \+ 
    - find .  -name '*.py[c|o]' -exec rm {} \+
- Delete these directories (not needed or already included in lambda):
    - boto3
    - botocore
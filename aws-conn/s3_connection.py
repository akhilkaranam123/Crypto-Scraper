import boto3
import scraper

def upload_s3(filename,filepath):
        s3_client = boto3.client(service_name='s3', region_name='ap-southeast-1',
                         aws_access_key_id='AKIAXI34O22FIZ5N253E',
                         aws_secret_access_key='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')

        s3_client.upload_file(filepath+filename, "web-scrappy", filename)


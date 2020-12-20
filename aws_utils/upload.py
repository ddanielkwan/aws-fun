import boto3
import argparse
import sys
from utils import get_s3_client
#CONSTANTS
global bucketname
bucketname = "stackname2-s3generalbucket-ioov7aj665vw" 
ARG_HELP = "File to upload" 
DESCRIPTION = "Upload file to s3 bucket"

#Functions

def upload(filename:str, uploadfile:str) -> None:
	"""Uploads file from local machine to AWS S3"""
	client = get_s3_client()
	filename = filename[0]
	uploadfile = uploadfile[0]
	#upload_file(path_of_file, bucketname, key)
	client.upload_file(filename, bucketname, uploadfile)	
	generate_url(client,uploadfile)
	return
 
def generate_url(client,uploadfile):
	location = client.get_bucket_location(Bucket=bucketname)['LocationConstraint']
	url = f"https://{bucketname}.s3.{location}.amazonaws.com/{uploadfile}"
	print(url)
	return 

def main():
	parser = argparse.ArgumentParser(description=DESCRIPTION)
	parser.add_argument("filename", type=str, nargs='+')
	parser.add_argument("uploadname", type=str, nargs='+')
	args = parser.parse_args()
	upload(args.filename, args.uploadname)


	sys.exit(0)
	
main()

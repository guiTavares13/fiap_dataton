import csv
import boto3
import os
from datetime import datetime
from botocore.exceptions import NoCredentialsError

csv.field_size_limit(10 * 1024 * 1024)  # 10MB

def create_s3_client():
    try:
        return boto3.client('s3',
                            endpoint_url='http://localhost:4566',
                            aws_access_key_id='test',
                            aws_secret_access_key='test',
                            region_name='sa-east-1')
    except NoCredentialsError:
        print('Credentials not available')
        return None

def upload_csv_to_s3(s3, bucket_name, file_path):
    file_name = os.path.basename(file_path)
    # Aqui estamos especificando que o arquivo será colocado na pasta 'raw' do S3
    s3_key = f"raw/{file_name}"

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_name} uploaded successfully to {bucket_name}/{s3_key}")
    except NoCredentialsError:
        print('Credentials not available')
    except FileNotFoundError:
        print(f"File {file_name} not found")

def main():
    bucket_name = 'eglobo-dataton'
    csv_files = []
    path_file = 'C:/workspace/fiap/challengers/Tech Challenger 5/dataset/files/treino/treino_parte'

    s3 = create_s3_client()

    for i in range(1, 7):

        name_file = path_file + str(i)  + '.csv'
        print(name_file)

        if os.path.exists(name_file):
            try:
                with open(name_file, 'r') as file:
                    csv_files.append(name_file)
                    print(f"{name_file} File found and added to the list")
            except Exception as e:
                print(f"Error processing file {name_file}: {e}")
            
        else:
            print(f"File not found: {name_file}")

    for file_path in csv_files:
        try:
            upload_csv_to_s3(s3, bucket_name, file_path)
            print(f"File {file_path} uploaded successfully")
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}")

if __name__ == '__main__':
    main()

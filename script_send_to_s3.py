import csv
import sys
import boto3
import os

# Aumentando o limite do campo para 10MB (ou qualquer outro valor que atenda ao seu caso)
csv.field_size_limit(10 * 1024 * 1024)  # 10MB
bucket_name = 'raw-webmedia-eglobo'

path_file = 'C:/workspace/fiap/challengers/Tech Challenger 5/dataset/files/treino/treino_parte'

# Especificando o perfil (se necessário)
session = boto3.Session(profile_name='ASIA4KM5HOGNOPIN6G5N')
s3_client = session.client('s3')

for i in range(1, 7):
    name_file = path_file + str(i) + '.csv'
    print(name_file)
    
    if os.path.exists(name_file):
        try:
            with open(name_file, 'r') as file:
                csv_file = csv.reader(file, delimiter=',')
                s3_key = f"treino_parte_{i}.csv"

                s3_client.upload_file(name_file, bucket_name, s3_key)
                print(f"Arquivo {name_file} enviado com sucesso para {bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Erro ao processar o arquivo {name_file}: {e}")
    else:
        print(f"Arquivo não encontrado: {name_file}")
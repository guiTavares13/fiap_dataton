# Use uma imagem base do Python
FROM python:3.9-slim

WORKDIR /app

# Copiar o arquivo de requisitos (requirements.txt) para o diretório de trabalho
# COPY requirements.txt /app/

# Instalar as dependências Python a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação para dentro do container
COPY . /app/

# Expor a porta onde a API Flask irá rodar
EXPOSE 5000

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para rodar a aplicação Flask
CMD ["flask", "run"]

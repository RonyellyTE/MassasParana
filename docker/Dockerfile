# Usa uma imagem base com Python
FROM python:3.10-slim

# Configura o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os arquivos necessários para instalar dependências
COPY requirements.txt /app/

# Instala dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto para dentro do container
COPY . /app/

# Expõe a porta para acessar a aplicação
EXPOSE 8000

# Comando padrão para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.12-slim

WORKDIR /app

# Instala as dependências necessárias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

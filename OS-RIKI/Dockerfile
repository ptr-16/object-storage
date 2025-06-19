FROM python:3.11-slim

RUN apt-get update && apt-get install -y ca-certificates curl && \
    update-ca-certificates && \
    pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org ruff
    
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

CMD ["python", "minioClient.py"]

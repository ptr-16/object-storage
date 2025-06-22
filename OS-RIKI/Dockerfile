FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ca-certificates curl && \
    update-ca-certificates

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org ruff

WORKDIR /app

COPY . .

RUN ruff check . --fix && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt


CMD ["sh", "-c", "ruff check . --fix && python -m unittest test_read_data.py && python minioClient.py"]

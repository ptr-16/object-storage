FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt


COPY demo.py .

CMD ["bash", "-c", "ruff check . && ruff format . && python demo.py"]

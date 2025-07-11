# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim
# RUN apt-get update && apt-get install -y ca-certificates
RUN apt-get update && apt-get install -y ca-certificates openssl curl

# ...existing code...


# Install pip requirements
COPY requirements.txt .
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN python -m pip install --upgrade pip setuptools
RUN python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "mindio.py"]

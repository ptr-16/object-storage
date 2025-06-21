# Base image
FROM python:3.10-slim-buster

# Update package list and install certificates
RUN apt-get update \
    && apt-get install -y ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python dependencies file
COPY requirements.txt .

# Install dependencies (skip SSL verification for internal networks)
RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt

# Copy the Python script
COPY Interact_with_miniO.py .

# Set the default command to run the script
CMD ["python", "-u", "Interact_with_miniO.py"]

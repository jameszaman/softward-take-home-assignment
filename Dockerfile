# Base image
FROM python:3.9.7-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY api api
COPY config.py .
COPY main.py .
COPY .env .

# Set environment variables
ENV MONGO_URI=${MONGO_URI}
ENV MONGO_DB_NAME=${MONGO_DB_NAME}
ENV API_PREFIX=${API_PREFIX}
ENV API_KEY=${API_KEY}

# Expose port
EXPOSE 8000

# Start application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

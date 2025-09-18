# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask app code
COPY app.py .

# Expose internal port
EXPOSE 8080

# Run Flask app
CMD ["python", "app.py"]

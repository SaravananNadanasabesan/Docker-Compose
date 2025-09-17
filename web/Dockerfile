# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY app.py .

# Expose the Flask port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
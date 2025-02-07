# Gunakan image Python resmi sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt ke working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set FLASK_APP environment variable
ENV FLASK_APP=app.__init__

# Copy seluruh kode aplikasi ke working directory
COPY . .

# Expose port 5000 untuk aplikasi Flask
EXPOSE 5000

# Command untuk menjalankan aplikasi
CMD ["flask", "run", "--host=0.0.0.0"]

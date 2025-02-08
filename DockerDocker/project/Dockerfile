# Gunakan image Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Salin semua file ke dalam container
COPY . .

# Expose port 5000 untuk akses web
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "__init__.py"]

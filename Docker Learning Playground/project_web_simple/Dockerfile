# Menggunakan Python sebagai base image
FROM python:3.9-slim

# Menetapkan direktori kerja
WORKDIR /app

# Menyalin file requirement.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Menyalin seluruh aplikasi
COPY . .

# Menjalankan aplikasi
CMD ["python", "app.py"]
    
# Menggunakan image Python sebagai base image
FROM python:3.8-slim

# Menetapkan direktori kerja dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh aplikasi ke dalam container
COPY . .

# Menjalankan aplikasi web
CMD ["python", "app.py"]

# Gunakan image Python
FROM python:3.9

# Set working directory dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Install dependencies
RUN pip install flask

# Jalankan aplikasi saat container berjalan
CMD ["python", "app.py"]

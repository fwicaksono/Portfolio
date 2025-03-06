# Gunakan base image Python
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy semua file ke dalam container
COPY . .

# Install dependensi
RUN pip install -r requirements.txt

# Jalankan aplikasi dengan Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

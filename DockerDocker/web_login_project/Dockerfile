# Gunakan image dasar Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/requirements.txt

# Install dependencies Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file dari folder app ke dalam container
COPY ./app /app

# Expose port 5000 untuk aplikasi Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app.py"]

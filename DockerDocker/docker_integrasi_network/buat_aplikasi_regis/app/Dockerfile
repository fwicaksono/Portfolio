FROM python:3.9-slim

# Set working directory
WORKDIR /buat_aplikasi_regis/app

# Install necessary dependencies
RUN pip install psycopg2-binary

# Copy the app code
COPY . /buat_aplikasi_regis/app

CMD ["python", "main.py"]

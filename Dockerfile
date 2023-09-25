# Gunakan image Python dari Docker Hub sebagai dasar
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Salin requirements.txt dan instal dependensi Python
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install jinja2
RUN pip install python-multipart

# Salin seluruh proyek Anda ke dalam container
COPY . .

# Jalankan aplikasi FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

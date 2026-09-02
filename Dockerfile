FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Forzar la actualización de pip y setuptools ANTES de instalar requerimientos
RUN python -m pip install --upgrade pip "setuptools>=78.1.1" && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
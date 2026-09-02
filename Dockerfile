FROM python:3.10-slim

WORKDIR /app

# requerimientos e instala dependencias actualizadas
COPY requirements.txt .
RUN python -m pip install --upgrade pip "setuptools>=78.1.1" && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
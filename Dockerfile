FROM python:3.10-slim

WORKDIR /app


RUN pip install --upgrade pip "setuptools>=78.1.1" wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
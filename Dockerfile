# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY Scores.txt /Scores.txt

EXPOSE 8777

CMD ["python", "MainScores.py"]

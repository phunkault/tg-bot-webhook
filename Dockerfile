FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV BOT_TOKEN = .
ENV ADMIN_ID = .

CMD ["python", "main.py"]

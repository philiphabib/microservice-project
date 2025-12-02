FROM python:3.11-slim

WORKDIR /app

RUN pip install fastapi uvicorn[standard]

COPY . .

CMD ["uvicorn", "main_frontend:app", "--host", "0.0.0.0", "--port", "80"]


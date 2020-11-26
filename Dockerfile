
FROM python:3.9

RUN pip install fastapi uvicorn requests urllib3

EXPOSE 80

COPY . .

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "80"]

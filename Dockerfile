
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# docker-compose up --build
# http://localhost:8000/docs
# docker exec -it mongo_db mongosh
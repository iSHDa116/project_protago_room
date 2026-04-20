FROM python:3.12

WORKDIR /code

RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc pkg-config default-mysql-client

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "project_protago_room.wsgi:application", "--bind", "0.0.0.0:8000"]
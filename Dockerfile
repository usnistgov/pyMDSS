# DockerFile, Image, Container
FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt  /code/requirements.txt

RUN pip install  --no-cache-dir --upgrade /code/requirements.txt

COPY /pymdss /code/pymdss

ADD pymdss .\\pymdss

CMD ["python" , "manage.py runserver pg902544.campus.nist.gov:8000", "--host", "0.0.0.0", "80"]
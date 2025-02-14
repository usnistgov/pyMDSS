FROM python:3.10-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /pymdss
COPY ./pymdss /pymdss
COPY requirements.txt /pymdss/requirements.txt
RUN apt-get update
RUN apt-get install -y git
RUN git init
RUN apt-get install -y gcc python3-dev
RUN apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev pkg-config
RUN apt-get install -y default-mysql-client default-libmysqlclient-dev
RUN pip install -r requirements.txt

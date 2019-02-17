FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gettext
RUN mkdir /main/code
WORKDIR /main/code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /main/code/
WORKDIR /code


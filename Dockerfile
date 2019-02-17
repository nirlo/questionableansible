FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gettext
RUN mkdir /main/
RUN mkdir /main/code
RUN mkdir /main/temp
WORKDIR /main/code
ADD requirements.txt /main/code/
RUN pip install -r requirements.txt
ADD . /main/code/
WORKDIR /main/code


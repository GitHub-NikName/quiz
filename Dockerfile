# docker build -t

FROM python:3.11-alpine3.18

#RUN apk add --no-cache curl supervisor
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/project
COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

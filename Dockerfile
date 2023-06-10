# docker build -t

FROM python:3.11-alpine3.18

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
COPY ./quiz .
EXPOSE 8000

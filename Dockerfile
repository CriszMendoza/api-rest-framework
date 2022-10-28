FROM python:3.9-alpine3.13
LABEL maintainer="criszmendoza212@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN apk update && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .temp-build-deps \ 
        postgresql-dev build-base musl-dev && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .temp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user
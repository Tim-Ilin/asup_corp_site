FROM python:3.7-alpine
COPY . /app
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc libc-dev python-dev musl-dev build-base linux-headers \
    && apk add --no-cache jpeg-dev zlib-dev \
    && apk add postgresql-dev \
    && pip install --no-cache-dir meinheld gunicorn psycopg2 \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps gcc libc-dev python-dev musl-dev build-base linux-headers
EXPOSE 8000

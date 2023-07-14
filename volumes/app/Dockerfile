FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1


RUN mkdir -p /home/src/app
ADD ./src/ /home/src/app
WORKDIR /home/src/app

RUN apk update
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev libpq-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py initadmin; \
    gunicorn -b 0.0.0.0:8000 config.wsgi
FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 8383

EXPOSE 8383

COPY ./app /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

FROM python:3.5
ENV PYTHONBUFFERED 1

RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_5.x > node.sh
RUN bash /node.sh
RUN apt-get install -y nodejs

COPY ./requirements /requirements

RUN pip install -r /requirements/production.txt

RUN groupadd -r django && useradd -r -g django django
COPY . /app
RUN chown -R django /app

COPY ./compose/django/gunicorn.sh /gunicorn.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /entrypoint.sh && chown django /entrypoint.sh
RUN chmod +x /gunicorn.sh && chown django /gunicorn.sh

WORKDIR /app

RUN npm i
RUN npm run build

ENTRYPOINT ["/entrypoint.sh"]

from python:3.10-slim-buster

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


RUN mkdir -p /api
Add . ./api
WORKDIR /api


EXPOSE 8000
ENTRYPOINT /bin/bash run.sh

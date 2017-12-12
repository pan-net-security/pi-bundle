FROM alpine:3.6

MAINTAINER Diogenes Santos de Jesus <diogenes.jesus@telekom.com>

# Install python3
RUN apk update && \
    apk add --no-cache python3 git && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# Install newer certs and pycog3
RUN apk add ca-certificates wget && \
  ln -s /usr/bin/python3 /usr/bin/python

RUN adduser -h /home/bundle -D bundle

USER root

RUN    update-ca-certificates --fresh


WORKDIR /home/bundle
RUN mkdir -p /home/bundle/pi-bundle/pi/commands

COPY setup.py requirements.txt /home/bundle/pi-bundle/
COPY pi/ /home/bundle/pi-bundle/pi/


WORKDIR /home/bundle/pi-bundle

RUN pip3 install -r requirements.txt
RUN pip3 install .

RUN apk del git
RUN rm -rfv /home/bundle/pi-bundle/  \
            /var/cache/apk/*  \
            /root/.cache

WORKDIR /home/bundle/

USER bundle

FROM alpine:3.6

MAINTAINER Diogenes Santos de Jesus <diogenes.jesus@telekom.com>


# Install python3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

# Install newer certs and pycog3
RUN apk update && \
  apk add ca-certificates wget && \
  ln -s /usr/bin/python3 /usr/bin/python && \
  rm -rfv /var/cache/apk/*

RUN adduser -h /home/bundle -D bundle

USER root

RUN wget -q https://gitlab.tools.in.pan-net.eu/ansible-roles/ansible-trust-ca/raw/93f4a0e44f864b344a21ff6acffe4b14f184c5e8/files/ca-certs/pannetss-ica1.crt \
    -P /usr/local/share/ca-certificates/ && \
    wget -q https://gitlab.tools.in.pan-net.eu/ansible-roles/ansible-trust-ca/raw/93f4a0e44f864b344a21ff6acffe4b14f184c5e8/files/ca-certs/pannetss-root.crt \
    -P /usr/local/share/ca-certificates/ && \
    update-ca-certificates --fresh


WORKDIR /home/bundle
RUN mkdir -p /home/bundle/pi-bundle/pi/commands

COPY setup.py requirements.txt /home/bundle/pi-bundle/
COPY pi/*.py /home/bundle/pi-bundle/pi/
COPY pi/commands/*.py /home/bundle/pi-bundle/pi/commands/

WORKDIR /home/bundle/pi-bundle
RUN pip3 install .
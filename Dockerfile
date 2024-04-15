FROM python:3.11-bullseye

LABEL   version = "1.0" \
        author.name    = "Mateo Restrepo" \
        author.email   = "mateo9116@gmail.com"

RUN apt-get update -y

# Create filesystem tree structure
RUN mkdir /opt/prueba_mvm
RUN mkdir /opt/prueba_mvm/bin
RUN mkdir /opt/prueba_mvm/config
RUN mkdir /var/log/prueba_mvm

WORKDIR /opt/prueba_mvm

ADD requirements.txt .
RUN apt-get update -y
RUN pip install -r requirements.txt

ADD source /opt/prueba_mvm/bin
ADD config /opt/prueba_mvm/config

COPY start.sh /start.sh

CMD sh start.sh
FROM ubuntu:18:04

RUN apt-get update
RUN apt-get install -y nginx


COPY entrypoint.sh /
COPY index.html /var/www/html/index.html

EXPOSE 80


ENTRYPOINT ["/entrypoint.sh"]
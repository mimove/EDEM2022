FROM ubuntu:18.04

RUN apt-get update
# RUN echo "hello1"

RUN apt-get install -y nginx

#RUN echo "hello2"


EXPOSE 80


ENTRYPOINT /usr/sbin/nginx -g "daemon off;"
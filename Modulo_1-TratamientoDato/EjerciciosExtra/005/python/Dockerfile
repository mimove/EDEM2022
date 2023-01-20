FROM python:3.10-slim-bullseye

RUN mkdir app
RUN mkdir datos

COPY ./main.py /app/
COPY ./requirements.txt /app/
COPY ./db/ /datos/

WORKDIR /app/

RUN apt-get update

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
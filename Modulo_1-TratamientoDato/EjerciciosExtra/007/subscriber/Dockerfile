FROM python:3.9.15-slim

# Esta parte ya sabéis cómo va
RUN mkdir app

WORKDIR /app
COPY main.py main.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "-u", "main.py" ]

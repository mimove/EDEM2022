FROM python

COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/
RUN mkdir results
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]
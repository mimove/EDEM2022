FROM python

COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/
RUN mkdir Homer
RUN mkdir Lisa
RUN mkdir General
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]
FROM python

COPY ./simpsons.py /app/
COPY ./requirements.txt /app/
COPY ./script.sh /app/

WORKDIR /app/
RUN mkdir Homer
RUN mkdir Lisa
RUN mkdir General
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "simpsons.py"]
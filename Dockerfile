FROM python:3.10-alpine3.17
WORKDIR /server
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./server .
CMD python3 app.py
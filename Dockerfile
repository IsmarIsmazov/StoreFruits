FROM python:3.8
LABEL authors="ismarhahazov"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR .

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /Store/
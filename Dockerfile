FROM django:latest
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


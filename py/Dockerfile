FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST="0.0.0.0"
ENV FLASK_APP="/src/app.py"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN mkdir /src
WORKDIR /src

EXPOSE 5000
COPY ./src/ ./
#COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["flask" , "run" ]

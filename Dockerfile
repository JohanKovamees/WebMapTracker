FROM ubuntu:latest

RUN apt update && apt-get install -y python3-pip sqlite3
WORKDIR /app

COPY ./src/ /app

RUN pip3 install -r /app/requirements.txt

#WORKDIR /app/src

ENV FLASK_APP=flaskp.py
ENV FLASK_DEBUG=1

#EXPOSE 5000
#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

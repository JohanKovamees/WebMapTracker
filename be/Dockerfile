FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y sqlite3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./src/ /app

RUN pip3 install -r /app/requirements.txt

ENV FLASK_APP=flaskp.py
ENV FLASK_DEBUG=1

RUN python3 set_up_db.py && chmod +x flaskp.py

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

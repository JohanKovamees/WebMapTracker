FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3

WORKDIR /app

COPY index.html style.css main.js ./

EXPOSE 8000

CMD ["python3", "-m", "http.server"]

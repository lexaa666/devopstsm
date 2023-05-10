FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

#ENV PATH="/root/.local/bin:${PATH}"
ENV FLASK_APP=app
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
#CMD ["Pwd"]
#ENTRYPOINT ["python"]
CMD ["python3","./app.py"]
#CMD ["flask","run"]

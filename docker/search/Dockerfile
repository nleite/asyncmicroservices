FROM ubuntu:14.10

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y

WORKDIR /home
ADD run.py /home/search

EXPOSE 30001

CMD /home/search/run.py

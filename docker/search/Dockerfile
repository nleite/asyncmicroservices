FROM ubuntu:14.10

RUN apt-get update -y
RUN apt-get install python3 python3-pip tree -y

WORKDIR /home
ADD run.py /home/run.py

CMD /home/run.py


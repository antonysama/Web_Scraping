FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
ENV TZ=America/Edmonton
RUN apt  update -y &&\ 
    apt install -y git gcc &&\ 
    mkdir /app    
WORKDIR /app     
COPY requirements.txt /app/     
RUN pip3 install -r requirements.txt
COPY ./ /app/  
CMD ["/bin/bash", "-c", "scrapy runspider edmjnl.py -o file.csv && scrapy runspider post.py -o file2.csv"]
#alternative: CMD bash -c "scrapy runspider edmjnl.py -o file.csv && scrapy runspider post.py -o file2.csv"
# instructions: 1. build image w., sudo docker build --tag test .  2. run w., sudo docker run -v /home/antonysama/docker_scrapy:/app [image no.]
#references: runs multiple python files https://intellipaat.com/community/19590/docker-run-multiple-commands-using-docker-compose-at-once
# https://stackoverflow.com/questions/49630960/dockerfile-running-multiple-cmd-starting-nginx-and-php
# to run your docker without sudo, https://docs.docker.com/engine/install/linux-postinstall/


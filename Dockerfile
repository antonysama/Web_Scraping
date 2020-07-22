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
CMD bash -c "scrapy runspider edmjnl.py -o file.csv && scrapy runspider post.py -o file2.csv"
#runs multiple python files https://intellipaat.com/community/19590/docker-run-multiple-commands-using-docker-compose-at-once
# build image w., sudo docker build --tag test .
# run w., sudo docker run -v /home/antony/scrapy:/app 0132a1b91cf7
# execute in order to run your docker without sudo, https://docs.docker.com/engine/install/linux-postinstall/


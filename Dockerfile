FROM python:3.8-slim-buster
#it setup our first layer or the base image we can say
RUN apt update -y && apt install awscli -y

COPY . /app
#it copies all the files from the current directory and move it to app folder of the base image
WORKDIR /app
#it specifies the working directory
RUN pip install -r requirements.txt
#to install all the necessary libraries
CMD ['python3', 'app.py']
#this will be the command to run the files
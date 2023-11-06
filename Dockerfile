# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT python3 run.py

# docker build -t clean_project_img .     
# docker images    
# docker run --name clean_project -p 8900:8900 clean_project_img
# docker ps
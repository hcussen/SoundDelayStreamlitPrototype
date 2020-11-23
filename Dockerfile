# base python is huge, so use slim
FROM python:3.7.6-slim 

# name it whatever you want - becomes root of docker image
WORKDIR /proto

COPY requirements.txt ./
# run is for installing things
RUN pip install -r requirements.txt

COPY . . 

#opens Docker port
EXPOSE 8501

# final command that runs things
# CMD = run this command in this Docker image
CMD ["streamlit", "run", "soundDelay.py"]
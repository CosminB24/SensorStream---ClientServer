FROM python:latest
#Labels as key value pair
LABEL Maintainer="cosmin"
WORKDIR /usr/app/src
RUN pip install paho-mqtt
RUN pip install Flask
COPY mainAPI.py ./
COPY bpublish.py ./
COPY bsubscribe.py ./
CMD [ "python", "./mainAPI.py"]
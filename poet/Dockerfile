FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime  

# Coping source in current directory into the image
# python:3-onbuild expects the source in /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
# Commands in a list
CMD ["python", "api.py"]
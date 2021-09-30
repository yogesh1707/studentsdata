FROM python:3.6-slim-buster
WORKDIR /app
COPY . .
RUN pip install flask
RUN pip install requests
RUN pip install flask-restful
RUN from flask import Flask
RUN from flask_restful import Resource, Api, reqparse
RUN import pandas as pd
RUN import ast
RUN pip install gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

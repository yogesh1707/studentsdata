FROM python:3.6-slim-buster
ENV PYTHONPATH "${PYTHONPATH}:/app/"
COPY . .
RUN pip install flask
RUN pip install requests
RUN pip install flask-restful
RUN pip install pandas
RUN pip install gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

FROM python:3.7
COPY .  /flask-api
WORKDIR /flask-api
RUN pip install -r requirements.txt
EXPOSE  5000
CMD ["python", "src/main.py"]
FROM ubuntu:20.04

RUN apt -y update && apt -y install python3-pip

WORKDIR /Timesheet

COPY . .

RUN pip install Django==4.0.6 django-extensions psycopg2-binary djangorestframework

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]

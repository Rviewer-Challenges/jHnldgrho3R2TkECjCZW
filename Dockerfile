# pull official base image
FROM python:3.11

# set work directory
WORKDIR /usr/src/django_project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Europe/Madrid

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:latest

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Install requirements
COPY ./provision/requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/production.txt

WORKDIR /app
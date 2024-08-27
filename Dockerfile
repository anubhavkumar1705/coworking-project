# Use Python Python 3.10 as the base image
FROM python:3.10-slim-buster

# Setup working directory
WORKDIR /src

# Dependencies required for psycopg2 (used for Postgres client)
RUN apt update -y && apt install -y build-essential libpq-dev

COPY ./analytics/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./analytics .

# Run the application when the container starts
CMD python app.py
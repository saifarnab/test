FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Creating working directory
RUN mkdir /app
WORKDIR /app

# Set timezone
RUN echo "Asia/Dhaka" > /etc/timezone

# Copy & Install project dependencies
COPY ./requirements.txt ./


RUN apt-get update \
    && apt-get install build-essential tzdata -y \
    && python3 -m pip install -r requirements.txt \
    && apt-get remove build-essential -y \
    && apt-get autoremove -y


# Copy project files
COPY . .

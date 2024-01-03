FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Creating working directory
RUN mkdir /app
WORKDIR /app

# Set timezone
RUN echo "Asia/Dhaka" > /etc/timezone

# Install project dependencies
COPY ./requirements.txt ./


RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
RUN apt-get install build-essential tzdata -y
RUN python3 -m pip install -r requirements.txt
RUN apt-get remove build-essential -y
RUN apt-get autoremove -y

# Copy project files
COPY . .

# Make port 8009 available to the world outside this container
EXPOSE 8009

# Define the default command to run when the container starts
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

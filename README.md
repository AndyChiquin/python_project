# Python Project

This is a simple Python project that prints a message to the console.

## Technologies Used
- Language: Python
- Container: Docker

## Prerequisites
- Docker installed
- Python installed locally (if running locally)

## Project Files
- **app.py**: Main file of the project that prints the message to the console.
- **Dockerfile**: Docker file for building the image.

# Create image in Docker

Execute it in the project directory.

~~~
docker build -t itsandy/python_project .
~~~

## Run the Docker Container
~~~
docker run itsandy/python_project
~~~

## Login in Docker Hub
~~~
docker login
~~~

## Docker Desktop pull in Docker Hub
~~~
docker pull itsandy/python_project
~~~

# RailWay
We log in and link to GitHub to deploy the repositories.

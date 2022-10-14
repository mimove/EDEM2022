#!/bin/bash


# List Docker images

docker images

#Create a new <hello-world> container

docker run hello-world

# List running containers

docker ps


# List all containers


docker ps -a


# List Docker images

docker images

# Create a new <Ubuntu> container

docker run Ubuntu



# Remove image

docker rmi <image>


# Create container from but not freeze terminal


docker run -d <imagen>



# Copy a file/folder into a container


docker cp <source> <target>



# Build an image

docker build <path of Dockerfile>


# Build an image with a name


docker build -t <name> <path to Dockerfile>



##### DOCKER COMPOSE ####

# Build a .yaml file

docker compose up


# List active compose containers (inside directory)


docker compose ps


# Stop containers (inside directory)


docker compose stop 
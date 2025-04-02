# warship-stack
Warehouse and Shipping


# Frequent use Docker command
Stop all running containers:
docker stop $(docker ps -aq)

Remove all containers:
docker rm $(docker ps -aq)

Remove all images:
docker rmi $(docker images -q)

Build a container
docker build -t warship-app .

Run a container
docker run -d -p 8503:8503 warship-app
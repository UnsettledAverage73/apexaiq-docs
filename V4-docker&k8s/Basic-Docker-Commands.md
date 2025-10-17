# Basic Docker Commands

Docker is an open-source platform that enables developers to build, ship, and run applications in containers. Containers are lightweight, standalone, executable packages of software that include everything needed to run an application: code, runtime, system tools, system libraries and settings.

## Docker Concepts

*   **Image:** A lightweight, standalone, executable package of software that includes everything needed to run an application.
*   **Container:** A runnable instance of an image. You can create, start, stop, move, or delete a container.
*   **Dockerfile:** A text document that contains all the commands a user could call on the command line to assemble an image.
*   **Docker Hub:** A cloud-based registry service where you can find and share container images.

## Basic Docker Commands

Here are some fundamental Docker commands you'll use frequently:

### 1. `docker run` - Run a container

Used to create and start a new container from an image. If the image is not available locally, Docker will pull it from Docker Hub.

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

# Example: Run an Ubuntu container and keep it interactive
docker run -it ubuntu /bin/bash

# Example: Run a Nginx web server in detached mode (background)
docker run -d -p 80:80 --name my-nginx nginx
```

*   `-it`: Interactive and pseudo-TTY allocation.
*   `-d`: Detached mode (run in the background).
*   `-p HOST_PORT:CONTAINER_PORT`: Publish a container's port(s) to the host.
*   `--name NAME`: Assign a name to the container.

### 2. `docker ps` - List containers

Used to list running containers. Add `-a` or `--all` to see all containers (running and stopped).

```bash
docker ps [OPTIONS]

# Example: List all running containers
docker ps

# Example: List all containers (running and stopped)
docker ps -a
```

### 3. `docker stop` - Stop a running container

Used to stop one or more running containers gracefully.

```bash
docker stop [OPTIONS] CONTAINER [CONTAINER...]

# Example: Stop a container named my-nginx
docker stop my-nginx
```

### 4. `docker start` - Start one or more stopped containers

Used to start one or more stopped containers.

```bash
docker start [OPTIONS] CONTAINER [CONTAINER...]

# Example: Start a container named my-nginx
docker start my-nginx
```

### 5. `docker restart` - Restart containers

Used to restart one or more containers.

```bash
docker restart [OPTIONS] CONTAINER [CONTAINER...]

# Example: Restart a container named my-nginx
docker restart my-nginx
```

### 6. `docker rm` - Remove one or more containers

Used to remove one or more stopped containers. To remove a running container, you'll need to stop it first or use the `-f` (force) flag.

```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]

# Example: Remove a stopped container named my-nginx
docker rm my-nginx

# Example: Force remove a running container
docker rm -f my-nginx
```

### 7. `docker rmi` - Remove one or more images

Used to remove one or more Docker images. You cannot remove an image if it's being used by a container.

```bash
docker rmi [OPTIONS] IMAGE [IMAGE...]

# Example: Remove an image named ubuntu
docker rmi ubuntu
```

### 8. `docker images` - List images

Used to list all local Docker images.

```bash
docker images [OPTIONS]
```

### 9. `docker build` - Build an image from a Dockerfile

Used to build a Docker image from a Dockerfile and a context. The context is the set of files at a specified path or URL.

```bash
docker build [OPTIONS] PATH | URL | -

# Example: Build an image named my-app from the current directory Dockerfile
docker build -t my-app .
```

*   `-t NAME:TAG`: Name and optionally a tag in the 'name:tag' format.
*   `.`: The build context (current directory).

### 10. `docker pull` - Pull an image or a repository from a registry

Used to pull an image or a repository from a Docker registry (e.g., Docker Hub).

```bash
docker pull [OPTIONS] NAME[:TAG|@DIGEST]

# Example: Pull the latest Ubuntu image
docker pull ubuntu:latest
```

### 11. `docker exec` - Run a command in a running container

Used to execute a command inside a running container.

```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

# Example: Execute a bash shell inside a running my-nginx container
docker exec -it my-nginx /bin/bash
```

### 12. `docker logs` - Fetch the logs of a container

Used to fetch the logs of a container.

```bash
docker logs [OPTIONS] CONTAINER

# Example: View logs of my-nginx container
docker logs my-nginx

# Example: Follow logs in real-time
docker logs -f my-nginx
```

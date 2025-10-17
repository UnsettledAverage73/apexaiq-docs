# Docker Implementation (Optional)

This section provides a practical guide on implementing a simple web application using Docker. We will cover creating a Dockerfile, building a Docker image, and running a Docker container.

## Prerequisites

*   Docker Desktop installed (or Docker Engine on your server).
*   Basic understanding of command-line interface.

## Example: Dockerizing a Simple Python Flask Application

Let's create a very basic Flask application and dockerize it.

### Step 1: Create the Application Files

Create a new directory named `flask-app` and navigate into it:

```bash
mkdir flask-app
cd flask-app
```

Inside `flask-app`, create two files: `app.py` and `requirements.txt`.

**`app.py`:**

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! This is a Flask application.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

**`requirements.txt`:**

```
Flask
```

### Step 2: Create a Dockerfile

In the `flask-app` directory, create a file named `Dockerfile` (no extension):

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### Step 3: Build the Docker Image

Navigate to the `flask-app` directory in your terminal and build the Docker image. The `-t` flag tags your image with a name (e.g., `my-flask-app`) and version (e.g., `1.0`). The `.` indicates that the Dockerfile is in the current directory.

```bash
docker build -t my-flask-app:1.0 .
```

You should see output indicating that the image is being built layer by layer.

### Step 4: Run the Docker Container

Now, run the Docker container based on the image you just built. The `-p 5000:5000` flag maps port 5000 of the host to port 5000 of the container. The `-d` flag runs the container in detached mode (in the background).

```bash
docker run -d -p 5000:5000 my-flask-app:1.0
```

To verify that the container is running, you can use:

```bash
docker ps
```

You should see your `my-flask-app:1.0` container listed.

### Step 5: Access the Application

Open your web browser and navigate to `http://localhost:5000`. You should see the message: "Hello, Docker! This is a Flask application."

### Step 6: Stop and Remove the Container and Image

To stop the running container:

```bash
docker stop <container_id_or_name>
```

To remove the stopped container:

```bash
docker rm <container_id_or_name>
```

To remove the Docker image:

```bash
docker rmi my-flask-app:1.0
```

This completes a basic Docker implementation for a Flask application. You can extend this further by adding more complex functionalities, database integrations, and deploying to a production environment.

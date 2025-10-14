.PHONY: all build up down clean backend frontend

# Define Docker image names and container names
BACKEND_IMAGE_NAME := dbf-scraper-backend
FRONTEND_IMAGE_NAME := dbf-scraper-frontend

BACKEND_CONTAINER_NAME := dbf-scraper-backend-container
FRONTEND_CONTAINER_NAME := dbf-scraper-frontend-container

# Define ports
BACKEND_PORT := 8000
FRONTEND_PORT := 3000

all: build up

build:
	@echo "Building Docker images..."
	docker build -t $(BACKEND_IMAGE_NAME) -f backend/Dockerfile backend
	docker build -t $(FRONTEND_IMAGE_NAME) -f frontend/Dockerfile frontend
	@echo "Docker images built successfully."

up:
	@echo "Starting Docker containers..."
	docker run -d --rm --name $(BACKEND_CONTAINER_NAME) -p $(BACKEND_PORT):$(BACKEND_PORT) $(BACKEND_IMAGE_NAME)
	docker run -d --rm --name $(FRONTEND_CONTAINER_NAME) -p $(FRONTEND_PORT):$(FRONTEND_PORT) $(FRONTEND_IMAGE_NAME)
	@echo "Backend API available at http://localhost:$(BACKEND_PORT)"
	@echo "Frontend application available at http://localhost:$(FRONTEND_PORT)"

down:
	@echo "Stopping Docker containers..."
	docker stop $(FRONTEND_CONTAINER_NAME) $(BACKEND_CONTAINER_NAME)
	@echo "Docker containers stopped."

clean:
	@echo "Removing Docker containers and images..."
	docker stop $(FRONTEND_CONTAINER_NAME) $(BACKEND_CONTAINER_NAME) || true
	docker rm $(FRONTEND_CONTAINER_NAME) $(BACKEND_CONTAINER_NAME) || true
	docker rmi $(FRONTEND_IMAGE_NAME) $(BACKEND_IMAGE_NAME) || true
	@echo "Docker containers and images removed."

# Convenience targets for individual component management
backend-build:
	docker build -t $(BACKEND_IMAGE_NAME) -f backend/Dockerfile backend

backend-up:
	docker run -d --rm --name $(BACKEND_CONTAINER_NAME) -p $(BACKEND_PORT):$(BACKEND_PORT) $(BACKEND_IMAGE_NAME)

backend-down:
	docker stop $(BACKEND_CONTAINER_NAME)

frontend-build:
	docker build -t $(FRONTEND_IMAGE_NAME) -f frontend/Dockerfile frontend

frontend-up:
	docker run -d --rm --name $(FRONTEND_CONTAINER_NAME) -p $(FRONTEND_PORT):$(FRONTEND_PORT) $(FRONTEND_IMAGE_NAME)

frontend-down:
	docker stop $(FRONTEND_CONTAINER_NAME)

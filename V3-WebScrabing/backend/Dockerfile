# Use a Python base image
FROM python:3.9-slim-buster

# Set environment variables for non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages for Chrome/Chromium and system dependencies
# This includes packages required by Selenium and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-glib-1-2 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxrender1 \
    libxkbcommon0 \
    xdg-utils \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome (stable version)
# Add Google Chrome's official GPG key
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Add Google Chrome's stable repository
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# Update package lists and install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Set environment variables for Chrome/ChromeDriver
ENV CHROME_DRIVER_VERSION="120.0.6099.109"
# Check if this version is still the latest compatible one from `run.sh --test` output or check chromedriver.chromium.org
# If it is not, then change it to the latest version
ENV CHROME_VERSION="120.0.6099.109"
# For a more dynamic approach you can omit the version and let selenium-manager handle it

# Install ChromeDriver
# RUN wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P /tmp/
# RUN unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/
# RUN chmod +x /usr/local/bin/chromedriver

# Alternatively, rely on selenium-manager (Selenium 4.6+) to download ChromeDriver
# This Dockerfile is set up to let Selenium Manager handle ChromeDriver.

# Set the working directory inside the container
WORKDIR /app/backend

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

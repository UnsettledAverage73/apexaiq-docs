# V3 - Web Scraping Automation Project

This project, titled "DBF Viewer 2000 Web Scraping Automation," is designed to extract version history data from the DBF Viewer 2000 website (https://www.dbf2002.com/news.html) using a web scraping backend API and display it through an interactive Next.js frontend.

## Table of Contents

1.  [Project Overview](#project-overview)
2.  [Features](#features)
3.  [Architecture](#architecture)
4.  [Prerequisites](#prerequisites)
5.  [Installation](#installation)
6.  [Usage](#usage)
7.  [Project Structure](#project-structure)
8.  [Configuration](#configuration)
9.  [Troubleshooting](#troubleshooting)
10. [Logging](#logging)
11. [Docker Management with Makefile](#docker-management-with-makefile)

## 1. Project Overview

The core purpose of this project is to automate the extraction of software version release information from a specific website. It achieves this by employing a backend service built with FastAPI for the scraping logic and a frontend application built with Next.js for user interaction and data visualization. The project is containerized using Docker, and a `Makefile` is provided for easy management of the Docker images and containers.

## 2. Features

*   **Web Scraping Backend**: A FastAPI application responsible for initiating and performing web scraping operations.
*   **Data Extraction**: Capable of extracting crucial version details such as version numbers, release dates, and associated download URLs.
*   **RESTful API**: The FastAPI backend exposes a RESTful API endpoint that can be triggered to start the scraping process and retrieve the extracted data.
*   **Interactive Next.js Frontend**: A user-friendly dashboard built with Next.js allows users to input the target URL for scraping and view the results in an organized manner.
*   **Robust Date Parsing**: The system is designed to handle various date formats encountered on the target website, ensuring accurate data capture.
*   **Comprehensive Logging**: Detailed logging mechanisms are in place for both the backend and scraper, aiding in debugging, monitoring, and understanding application behavior.
*   **Error Handling**: Implements robust error handling strategies to gracefully manage issues that may arise during web scraping or API interactions.

## 3. Architecture

The project follows a client-server architecture, with a clear separation of concerns:

*   **Backend Service (FastAPI)**: Handles the heavy lifting of web scraping, data processing, and exposing a consumable API. It uses `selenium` with `Chromium` or `Chrome` and `ChromeDriver` to interact with the target website.
*   **Frontend Application (Next.js)**: Provides the graphical user interface for users to trigger scraping requests and display the results. It communicates with the backend API to fetch data.
*   **Containerization (Docker)**: Both the backend and frontend are containerized, ensuring consistent environments across development, testing, and production. This also simplifies deployment.

## 4. Prerequisites

To set up and run this project, you will need the following:

### General Prerequisites:

*   **Docker Desktop** (or Docker Engine) installed: Essential for building and running the containerized applications.
*   **Command-Line Interface (CLI)**: Basic familiarity with using a terminal for commands.

### For running without Docker (Development Setup):

#### Backend Prerequisites:

*   **Python 3.7+**: Ensure Python 3.7 or a newer version is installed, along with `pip`.
*   **Google Chrome or Chromium Browser**: The scraper requires a browser to function. Install one of the following:
    *   **Ubuntu/Debian**: `sudo apt install chromium-browser`
    *   **macOS**: `brew install --cask google-chrome`
    *   **Windows**: Download from the [Chrome website](https://www.google.com/chrome/)
*   **ChromeDriver**: The script is designed to automatically manage ChromeDriver. However, you can also install it manually if needed:
    *   **Ubuntu/Debian**: `sudo apt install chromium-chromedriver`
    *   Alternatively, download from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)

#### Frontend Prerequisites:

*   **Node.js (LTS recommended)**: Ensure Node.js is installed, which includes `npm` or `yarn`.

## 5. Installation

1.  **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd V3-WebScrabing
    ```

2.  **Using Docker (Recommended for quick setup and deployment)**:
    *   Navigate to the project root directory.
    *   Use the `Makefile` to build and run everything:
        ```bash
        make all
        ```
        This command will:
        *   Build Docker images for both backend and frontend.
        *   Start both backend and frontend containers.

3.  **Manual Setup (for development without Docker)**:

    #### Backend Setup:

    *   Navigate to the `backend` directory:
        ```bash
        cd backend
        ```
    *   Run the setup script:
        ```bash
        ./setup.sh
        ```
    *   Install Python dependencies:
        ```bash
        python3 -m pip install -r requirements.txt
        ```
    *   Return to the project root:
        ```bash
        cd ..
        ```

    #### Frontend Setup:

    *   Navigate to the `frontend` directory:
        ```bash
        cd frontend
        ```
    *   Install Node.js dependencies:
        ```bash
        npm install # or yarn install
        ```
    *   Return to the project root:
        ```bash
        cd ..
        ```

## 6. Usage

### 1. With Docker (After running `make all`):

*   The Backend API will be accessible at: `http://localhost:8000`
*   The Frontend Application will be accessible at: `http://localhost:3000`

### 2. Manual Start (After manual installation):

#### Start the Backend API:

*   Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
*   Run the backend script:
    ```bash
    ./run.sh
    ```
    The API will be accessible at `http://localhost:8000`.

#### Start the Frontend Application:

*   Open a **new terminal**, navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
*   Run the development server:
    ```bash
    npm run dev # or yarn dev
    ```
    The frontend will be accessible at `http://localhost:3000` (or another configured port).

### API Endpoints:

The backend API exposes the following endpoints:

*   **GET /**: Returns a basic API status message.
*   **GET /scrape?url=<url>**: Triggers the web scraping process for the provided URL and returns the extracted JSON data.
    *   **Example**: `http://localhost:8000/scrape?url=https://www.dbf2002.com/news.html`

## 7. Project Structure

```
V3-WebScrabing/
├── backend/                 # FastAPI backend application
│   ├── app.py               # Main FastAPI application
│   ├── dbf_scraper.py       # Core web scraping logic using Selenium
│   ├── config.py            # Backend configuration (logging, scraping parameters)
│   ├── requirements.txt     # Python dependencies
│   ├── setup.sh             # Script for backend environment setup
│   ├── run.sh               # Script to run the FastAPI server
│   ├── Dockerfile           # Dockerfile for building the backend image
│   ├── README.md            # Backend-specific documentation
│   └── USAGE.md             # Backend usage guide
├── frontend/                # Next.js frontend application
│   ├── app/                 # Next.js app directory (routing, UI components)
│   │   ├── favicon.ico
│   │   ├── global.css
│   │   ├── globals.css
│   │   ├── layout.tsx       # Root layout for the Next.js app
│   │   └── page.tsx         # Main page component
│   ├── public/              # Static assets for the frontend
│   │   ├── file.svg
│   │   ├── globe.svg
│   │   ├── next.svg
│   │   ├── vercel.svg
│   │   └── window.svg
│   ├── Dockerfile           # Dockerfile for building the frontend image
│   ├── package.json         # Node.js project metadata and dependencies
│   ├── package-lock.json    # Records exact dependency versions
│   ├── next.config.ts       # Next.js configuration
│   ├── eslint.config.mjs    # ESLint configuration
│   ├── postcss.config.mjs   # PostCSS configuration
│   ├── README.md            # Frontend-specific documentation
│   └── tsconfig.json        # TypeScript configuration
├── __pycache__/             # Python cache directory
├── Makefile                 # Utility for Docker build, up, down, clean commands
└── Web Scraping.pptx        # Original project presentation file
```

## 8. Configuration

*   **Backend Configuration**: The `backend/config.py` file allows you to modify various parameters, including web scraping settings, logging configurations, and supported date parsing formats. Review this file to customize the scraping behavior.

## 9. Troubleshooting

### Backend Issues:

*   **Python Dependencies**: Ensure all dependencies listed in `backend/requirements.txt` are installed (`python3 -m pip install -r requirements.txt`).
*   **ChromeDriver/Browser**: Verify that Google Chrome/Chromium browser is installed and accessible. The script attempts to auto-download ChromeDriver; if issues persist, manual installation might be necessary.
*   **API Not Starting**: Check if port `8000` is free. Confirm that `backend/run.sh` correctly executes the `uvicorn` command.
*   **No Data Scraped**: Check your internet connection. Try running the scraper with a visible browser (e.g., `./run.sh --headless=false`). Ensure the target website is accessible.

### Frontend Issues:

*   **Node.js Dependencies**: Navigate to `frontend` and run `npm install` (or `yarn install`) to ensure all Node.js dependencies are installed.
*   **Communication with Backend**: Verify that the backend API is running and accessible at `http://localhost:8000`. Check your browser's developer console for any network errors or CORS-related issues (CORS settings are managed in `backend/app.py`).

## 10. Logging

*   **Backend API Logs**: Found in `backend/backend.log`.
*   **Scraper-Specific Logs**: Found in `backend/dbf_automation.log`.

These logs are crucial for diagnosing issues and understanding the execution flow of the application.

## 11. Docker Management with Makefile

The `Makefile` at the project root simplifies common Docker operations:

*   `make build`: Builds Docker images for both the backend and frontend.
*   `make up`: Starts Docker containers for both applications. Frontend will be available at `http://localhost:3000` and backend at `http://localhost:8000`.
*   `make down`: Stops all running Docker containers associated with the project.
*   `make clean`: Stops and removes all Docker containers and images for the project.
*   `make backend-build`, `make backend-up`, `make backend-down`: Specific commands for managing the backend Docker container.
*   `make frontend-build`, `make frontend-up`, `make frontend-down`: Specific commands for managing the frontend Docker container.

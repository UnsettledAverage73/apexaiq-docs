# DBF Viewer 2000 Web Scraping Automation

This project provides a web scraping backend API (FastAPI) to extract version history from the DBF Viewer 2000 website (https://www.dbf2002.com/news.html), and an interactive Next.js frontend to interact with it.

## Features

- **Web Scraping Backend**: FastAPI application to scrape version data.
- **Data Extraction**: Extracts version numbers, dates, and URLs.
- **FastAPI**: Provides a RESTful API endpoint for triggering scraping.
- **Next.js Frontend**: Interactive dashboard for user input and data display.
- **Date Parsing**: Handles multiple date formats automatically.
- **Logging**: Comprehensive logging for debugging and monitoring.
- **Error Handling**: Robust error handling for scraping and API.

## Prerequisites

Before running the application, ensure you have the following installed:

### Backend Prerequisites:

1.  **Python 3.7+**:
    Ensure Python 3.7 or higher is installed and `pip` is available. You will need to manually install the dependencies listed in `backend/requirements.txt`.
    ```bash
    python3 --version
    # To install dependencies (example, from backend directory):
    # cd backend
    # python3 -m pip install -r requirements.txt
    ```

2.  **Google Chrome or Chromium Browser**:
    The scraper uses a web browser. Install one of the following:
    - **Ubuntu/Debian**: `sudo apt install chromium-browser`
    - **macOS**: `brew install --cask google-chrome`
    - **Windows**: Download from [Chrome website](https://www.google.com/chrome/)

3.  **ChromeDriver**:
    The script will automatically manage ChromeDriver, but you can also install it manually:
    ```bash
    # Ubuntu/Debian
    sudo apt install chromium-chromedriver
    
    # Or download from: https://chromedriver.chromium.org/
    ```

### Frontend Prerequisites:

1.  **Node.js (LTS recommended)**:
    Ensure Node.js is installed. This includes `npm` or `yarn`.
    ```bash
    node -v
    npm -v
    ```

## Installation

1.  **Clone or download the project files**

2.  **Backend Setup**:
    Navigate to the `backend` directory:
    ```bash
    cd backend
    ./setup.sh
    python3 -m pip install -r requirements.txt
    cd ..
    ```

3.  **Frontend Setup**:
    Navigate to the `frontend` directory and install dependencies:
    ```bash
    cd frontend
    npm install # or yarn install
    cd ..
    ```

## Usage

### 1. Start the Backend API

Navigate to the `backend` directory and run:
```bash
cd backend
./run.sh
```
The API will be accessible at `http://localhost:8000`.

### 2. Start the Frontend Application

Open a new terminal, navigate to the `frontend` directory and run:
```bash
cd frontend
npm run dev # or yarn dev
```
The frontend will be accessible at `http://localhost:3000` (or another port if configured).

### API Endpoints:

- **GET /**: Basic API status.
- **GET /scrape?url=<url>**: Triggers web scraping for the given URL and returns JSON data.
    *   Example: `http://localhost:8000/scrape?url=https://www.dbf2002.com/news.html`

## Project Structure

```
apexaiq/
├── backend/
|   ├── app.py             # FastAPI application
|   ├── dbf_scraper.py     # Web scraping logic
|   ├── config.py         # Backend configuration
|   ├── requirements.txt  # Python dependencies
|   ├── setup.sh         # Backend setup script
|   ├── run.sh           # Backend runner script
|   ├── README.md        # Backend README (this file)
|   ├── USAGE.md         # Backend usage guide
|   └── logs/            # Backend log directory
├── frontend/
|   └── ...             # Next.js application files
└── Web Scraping.pptx  # Project presentation (original)
```

## Configuration

Edit `backend/config.py` to modify:

- Web scraping parameters
- Logging configuration
- Date parsing formats

## Troubleshooting

### Backend Issues:

1.  **Python dependencies not installed**:
    Ensure you run `python3 -m pip install -r requirements.txt` from the `backend` directory.

2.  **ChromeDriver not found**:
    - The script auto-downloads ChromeDriver.
    - Ensure Chrome/Chromium browser is installed.

3.  **API not starting/accessible**:
    - Check if port 8000 is free.
    - Verify `run.sh` is correctly executing `uvicorn`.

4.  **No data scraped**:
    - Check internet connection.
    - Run with visible browser: `./run.sh --headless=false`.
    - Check website accessibility.

### Frontend Issues:

1.  **Node.js dependencies not installed**:
    Navigate to `frontend` and run `npm install` or `yarn install`.

2.  **Frontend not communicating with backend**:
    - Ensure backend API is running at `http://localhost:8000`.
    - Check browser console for network errors.
    - Verify CORS settings in `backend/app.py`.

## Logging

Check `backend/backend.log` for backend API logs and `backend/dbf_automation.log` for scraper-specific logs.

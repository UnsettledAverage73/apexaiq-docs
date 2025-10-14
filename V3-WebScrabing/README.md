# DBF Viewer 2000 Web Scraping Automation

This automation script scrapes version information from the DBF Viewer 2000 website (https://www.dbf2002.com/news.html) and prints it to the console.

## Features

- **Web Scraping**: Uses Selenium WebDriver to scrape version data from the DBF website
- **Data Extraction**: Extracts version numbers, dates, and URLs
- **Date Parsing**: Handles multiple date formats automatically
- **Logging**: Comprehensive logging for debugging and monitoring
- **Error Handling**: Robust error handling and retry mechanisms

## Prerequisites

Before running the automation, ensure you have the following installed:

### 1. Python 3.7+
```bash
python3 --version
```

### 2. Google Chrome or Chromium Browser
- **Ubuntu/Debian**: `sudo apt install chromium-browser`
- **macOS**: `brew install --cask google-chrome`
- **Windows**: Download from [Chrome website](https://www.google.com/chrome/)

### 3. ChromeDriver
The script will automatically manage ChromeDriver, but you can also install it manually:
```bash
# Ubuntu/Debian
sudo apt install chromium-chromedriver

# Or download from: https://chromedriver.chromium.org/
```

## Installation

1.  **Clone or download the project files**

2.  **Run the setup script**:
    ```bash
    ./setup.sh
    ```

3.  **Or install manually**:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

### Basic Usage
```bash
./run.sh
```

### Test Components
```bash
./run.sh --test
```

### Run with Visible Browser
```bash
./run.sh --headless=false
```

## Project Structure

```
apexaiq/
├── main.py              # Main orchestration script
├── dbf_scraper.py       # Web scraping module
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── setup.sh           # Setup script
├── run.sh             # Runner script
├── README.md          # This file
├── USAGE.md           # Detailed usage guide
└── dbf_automation.log # Log file (created when running)
```

## Configuration

Edit `config.py` to modify:

- Web scraping parameters
- Logging configuration
- Date parsing formats

## Troubleshooting

### Check Logs
```bash
# View automation logs
tail -f dbf_automation.log
```

### Common Issues

1. **ChromeDriver not found**
   - The script auto-downloads ChromeDriver
   - Ensure Chrome/Chromium is installed

2. **No data scraped**
   - Check internet connection
   - Run with `--headless=false` to see browser
   - Check website accessibility

3. **Permission errors**
   - Ensure proper file permissions
   - Use virtual environment paths

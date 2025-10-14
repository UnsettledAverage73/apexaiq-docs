# DBF Scraper Automation - Usage Guide

## Quick Start

### 1. Setup (First Time Only)
```bash
cd /home/unsettledaverage73/apexaiq
./setup.sh
```

### 2. Run the Automation
```bash
# Run with virtual environment
./venv/bin/python main.py

# Test components only
./venv/bin/python main.py --test

# Run with visible browser (for debugging)
./venv/bin/python main.py --headless=false
```

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

## Prerequisites

Before running the automation, ensure you have the following installed:

### 1. Python 3.7+
```bash
python3 --version
```

### 2. Google Chrome or Chromium Browser
- **Ubuntu/Debian**: `sudo apt install chromium-browser`
- **Arch Linux**: `sudo pacman -S chromium`
- **macOS**: `brew install --cask google-chrome`
- **Windows**: Download from [Chrome website](https://www.google.com/chrome/)

### 3. ChromeDriver
The script will automatically manage ChromeDriver, but you can also install it manually:
```bash
# Ubuntu/Debian
sudo apt install chromium-chromedriver

# Arch Linux
sudo pacman -S chromium-chromedriver

# Or download from: https://chromedriver.chromium.org/
```

## Configuration

The `config.py` file contains various settings for the automation. You can override other settings in `config.py`:

- Web scraping parameters
- Logging configuration
- Date parsing formats

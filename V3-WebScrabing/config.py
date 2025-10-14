"""
Configuration file for DBF Scraper Automation
"""

# Web Scraping Configuration
SCRAPING_CONFIG = {
    "target_url": "https://www.dbf2002.com/news.html",
    "headless_mode": True,
    "timeout": 10,
    "retry_attempts": 3
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_file": "dbf_automation.log"
}

# Date Parsing Configuration
DATE_FORMATS = [
    "%B %d, %Y",      # October 13, 2025
    "%b %d, %Y",      # Oct 13, 2025
    "%d %B %Y",       # 13 October 2025
    "%d %b %Y",       # 13 Oct 2025
    "%Y-%m-%d",       # 2025-10-13
    "%m/%d/%Y",       # 10/13/2025
    "%d/%m/%Y"        # 13/10/2025
]

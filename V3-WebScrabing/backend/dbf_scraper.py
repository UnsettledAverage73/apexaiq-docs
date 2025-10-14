"""
DBF Viewer 2000 Web Scraper
Scrapes version information from https://www.dbf2002.com/news.html
"""

import re
import time
from datetime import datetime
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DBFScraper:
    def __init__(self, headless=True):
        """Initialize the scraper with Chrome WebDriver"""
        self.url = "https://www.dbf2002.com/news.html"
        self.headless = headless
        self.driver = None
        self.setup_driver()
    
    def setup_driver(self):
        """Setup Chrome WebDriver with appropriate options"""
        try:
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            logger.info("Chrome WebDriver initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            raise
    
    def scrape_version_data(self, target_url: str) -> List[Dict[str, str]]:
        """Scrape version data from the news page"""
        try:
            logger.info(f"Navigating to {target_url}")
            self.driver.get(target_url)
            
            # Wait for the page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Get page source (no BeautifulSoup needed for parsing)
            
            version_data = []
            
            # Look for elements that might contain version entries, e.g., headings or paragraphs
            # The pattern "VERSION vX.XX (Date)" is usually in plain text within elements.
            # We'll use a broad XPath to find all text-containing elements.
            potential_version_elements = self.driver.find_elements(By.XPATH, "//*[self::h2 or self::h3 or self::p or self::span]")
            
            # Look for version entries - they typically follow the pattern "VERSION vX.XX (Date)"
            version_pattern = re.compile(r'VERSION\s+(v[\d\.]+)\s*\(([^)]+)\)', re.IGNORECASE)
            
            for element in potential_version_elements:
                element_text = element.text
                if element_text:
                    version_entries = re.findall(version_pattern, element_text)
                    
                    for version, date_str in version_entries:
                        # Clean up the version string
                        clean_version = version.strip()
                        
                        # Parse and format the date
                        formatted_date = self.parse_date(date_str.strip())
                        
                        # Create the URL (assuming it's the same page for now)
                        url = target_url  # Use target_url here
                        
                        version_info = {
                            "version": clean_version,
                            "date": formatted_date,
                            "url": url
                        }
                        
                        version_data.append(version_info)
                        logger.info(f"Found version: {clean_version} - {formatted_date}")
            
            # Filter out duplicate entries and clean up the data
            unique_versions = {}
            for entry in version_data:
                key = f"{entry['version']}_{entry['date']}"
                if key not in unique_versions:
                    unique_versions[key] = entry
            
            version_data = list(unique_versions.values())
            
            # Sort by date (newest first)
            version_data.sort(key=lambda x: x['date'], reverse=True)
            
            logger.info(f"Successfully scraped {len(version_data)} version entries")
            return version_data
            
        except Exception as e:
            logger.error(f"Error scraping version data: {e}")
            raise
    
    def parse_date(self, date_str: str) -> str:
        """Parse and format date string to ISO format"""
        try:
            # Remove extra whitespace and clean up
            date_str = date_str.strip()
            
            # Handle different date formats
            date_formats = [
                "%B %d, %Y",      # October 13, 2025
                "%b %d, %Y",      # Oct 13, 2025
                "%d %B %Y",       # 13 October 2025
                "%d %b %Y",       # 13 Oct 2025
                "%Y-%m-%d",       # 2025-10-13
                "%m/%d/%Y",       # 10/13/2025
                "%d/%m/%Y"        # 13/10/2025
            ]
            
            for fmt in date_formats:
                try:
                    parsed_date = datetime.strptime(date_str, fmt)
                    return parsed_date.strftime("%Y-%m-%d")
                except ValueError:
                    continue
            
            # If no format matches, return the original string
            logger.warning(f"Could not parse date: {date_str}")
            return date_str
            
        except Exception as e:
            logger.error(f"Error parsing date '{date_str}': {e}")
            return date_str
    
    def close(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
            logger.info("WebDriver closed")

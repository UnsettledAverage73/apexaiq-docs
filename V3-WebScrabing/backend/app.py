from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import logging
import sys

# Add the directory containing dbf_scraper.py to the Python path
sys.path.append(".")

from dbf_scraper import DBFScraper
import config

# Set up logging for the API
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backend.log'),  # Separate log for backend API
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DBF Scraper API",
    description="API for scraping DBF Viewer 2000 version history.",
    version="1.0.0",
)

# Configure CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for now, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScrapeResult(BaseModel):
    version: str
    date: str
    url: str

@app.get("/", summary="Root endpoint for API status")
async def root():
    return {"message": "DBF Scraper API is running!"}

@app.get("/scrape", response_model=List[ScrapeResult], summary="Scrape version data from a specified URL")
async def scrape_data(
    url: str = Query(config.SCRAPING_CONFIG["target_url"], description="URL to scrape version data from")
):
    """
    Scrapes version data (version, date, URL) from the specified news page.
    """
    logger.info(f"Received scrape request for URL: {url}")
    scraper = None
    try:
        scraper = DBFScraper(headless=config.SCRAPING_CONFIG["headless_mode"])
        version_data = scraper.scrape_version_data(target_url=url) # Pass URL to scraper
        logger.info(f"Successfully scraped {len(version_data)} entries from {url}")
        return version_data
    except Exception as e:
        logger.error(f"Error during scraping for {url}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to scrape data: {e}")
    finally:
        if scraper:
            scraper.close()
            logger.info("Scraper WebDriver closed.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

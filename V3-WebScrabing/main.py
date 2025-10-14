"""
DBF Viewer 2000 Automation Script
Main script that orchestrates web scraping and MongoDB storage
"""

import logging
import sys
from datetime import datetime
from dbf_scraper import DBFScraper
import config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dbf_automation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main function to orchestrate the scraping and database operations"""
    logger.info("Starting DBF Viewer 2000 automation...")
    
    scraper = None
    
    try:
        # Initialize scraper
        logger.info("Initializing web scraper...")
        scraper = DBFScraper(headless=config.SCRAPING_CONFIG["headless_mode"])
        
        # Perform scraping
        logger.info("Starting web scraping...")
        version_data = scraper.scrape_version_data()
        
        if not version_data:
            logger.warning("No version data found during scraping")
            return
        
        logger.info(f"Scraped {len(version_data)} version entries")
        
        # Print scraped data to console
        print("\n" + "="*80)
        print("SCRAPED DBF VIEWER 2000 VERSION DATA")
        print("="*80)
        
        for i, entry in enumerate(version_data, 1):
            print(f"\n{i}. Version: {entry['version']}")
            print(f"   Date: {entry['date']}")
            print(f"   URL: {entry['url']}")
            print("-" * 40)
            
        print(f"\nTotal versions found: {len(version_data)}")
        
        logger.info("Automation completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during automation: {e}")
        sys.exit(1)
        
    finally:
        # Clean up resources
        if scraper:
            scraper.close()
        logger.info("Resources cleaned up")

def test_components():
    """Test individual components"""
    logger.info("Testing components...")
    
    # Test scraper
    try:
        scraper = DBFScraper(headless=True)
        version_data = scraper.scrape_version_data()
        logger.info(f"Scraper test successful - found {len(version_data)} versions")
        scraper.close()
        
        # Display sample data
        if version_data:
            logger.info("Sample scraped data:")
            for i, entry in enumerate(version_data[:3]):  # Show first 3
                logger.info(f"  {i+1}. Version: {entry['version']}, Date: {entry['date']}")
        
    except Exception as e:
        logger.error(f"Scraper test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="DBF Viewer 2000 Automation")
    parser.add_argument("--test", action="store_true", help="Test components only")
    parser.add_argument("--headless", action="store_false", dest="headless_mode", help="Run browser in visible mode")
    parser.set_defaults(headless_mode=True) # Default to headless
    
    args = parser.parse_args()
    
    if args.test:
        logger.info("Running component tests...")
        if test_components():
            logger.info("All tests passed!")
        else:
            logger.error("Some tests failed!")
            sys.exit(1)
    else:
        # Update scraping config based on CLI arg
        config.SCRAPING_CONFIG["headless_mode"] = args.headless_mode
        main()

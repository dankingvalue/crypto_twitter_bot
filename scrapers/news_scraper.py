import feedparser
import logging

logger = logging.getLogger(__name__)

class NewsScraper:
    def __init__(self):
        self.sources = {'global': [], 'local': []}
    
    def scrape_all(self):
        logger.info("Scraping news...")
        return 0
    
    def get_top_unused(self, category='global', limit=5):
        return []

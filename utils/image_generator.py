"""Image generation utilities"""
import logging

logger = logging.getLogger(__name__)

class ImageGenerator:
    def __init__(self):
        self.enabled = False
        logger.info("Image generator initialized (disabled)")
    
    def generate_price_chart(self, data, title="Chart", filename=None):
        return None
    
    def generate_quote_card(self, quote, author="", filename=None):
        return None

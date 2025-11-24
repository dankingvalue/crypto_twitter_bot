import logging

logger = logging.getLogger(__name__)

class RedditScraper:
    def __init__(self):
        self.enabled = False
    
    def get_hot_topics(self, limit=10):
        return []

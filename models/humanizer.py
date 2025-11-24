import random
import logging

logger = logging.getLogger(__name__)

class Humanizer:
    def __init__(self):
        self.kenyan_slang = ["sawa", "poa", "noma"]
    
    def humanize_tweet(self, text, is_morning=False):
        return text, None
    
    def get_response_delay(self):
        return random.randint(60, 300)
    
    def get_correction_delay(self):
        return random.randint(2, 5)
    
    def get_correction_tweet(self, word):
        return f"*{word}"

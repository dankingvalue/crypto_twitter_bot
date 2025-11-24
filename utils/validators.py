"""Validation utilities"""

class Validators:
    @staticmethod
    def is_valid_tweet_length(text, max_length=280):
        return len(text) <= max_length
    
    @staticmethod
    def is_valid_url(url):
        return url.startswith(('http://', 'https://'))
    
    @staticmethod
    def sanitize_input(text, max_length=None):
        text = text.strip()
        if max_length:
            text = text[:max_length]
        return text

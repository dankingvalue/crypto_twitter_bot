"""Text utilities"""
import re

class TextUtils:
    @staticmethod
    def truncate_text(text, max_length=280):
        if len(text) <= max_length:
            return text
        return text[:max_length-3] + "..."
    
    @staticmethod
    def extract_hashtags(text):
        return re.findall(r'#\w+', text)
    
    @staticmethod
    def clean_text(text):
        return re.sub(r'\s+', ' ', text).strip()

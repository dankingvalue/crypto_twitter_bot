"""
Configuration settings
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Twitter API
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Reddit (optional)
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID', '')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET', '')
REDDIT_USER_AGENT = 'CryptoNewsBot/1.0'

# Database
DATABASE_URL = os.getenv('DATABASE_URL')

# Bot Settings
BOT_USERNAME = os.getenv('BOT_USERNAME', 'YourTwitterHandle')
TIMEZONE = 'Africa/Nairobi'

# Posting Schedule (East Africa Time)
POSTING_TIMES = [
    '06:30',
    '09:00',
    '12:30',
    '15:00',
    '18:00',
    '21:00',
]

# Content Mix Ratios
CONTENT_MIX = {
    'local_kenya': 0.35,
    'global_crypto': 0.40,
    'engagement': 0.15,
    'curated': 0.10
}

# Humanization Settings
HUMANIZATION = {
    'typo_probability': 0.05,
    'correction_delay_min': 2,
    'correction_delay_max': 5,
    'emoji_probability': 0.70,
    'response_delay_min': 60,
    'response_delay_max': 1800,
    'varied_greetings': True,
    'kenyan_slang_probability': 0.20,
}

# Rate Limits
MAX_TWEETS_PER_DAY = 50
MAX_REPLIES_PER_HOUR = 10
MAX_FOLLOWS_PER_DAY = 400

# ML Settings
MIN_CONFIDENCE_SCORE = 0.7
USE_GPT4 = os.getenv('USE_GPT4', 'false').lower() == 'true'
MODEL_NAME = 'gpt-4-turbo-preview' if USE_GPT4 else 'gpt-3.5-turbo'

# Monitoring
SENTRY_DSN = os.getenv('SENTRY_DSN', '')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Admin
ADMIN_TOKEN = os.getenv('ADMIN_TOKEN', 'change-this-secret-token')

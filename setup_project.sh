#!/bin/bash

echo "🚀 Setting up Crypto Twitter Bot..."

# Create directories
mkdir -p analytics config core models scrapers utils web scripts data

# Create __init__.py files
for dir in analytics config core models scrapers utils web scripts; do
    echo "\"\"\"${dir^} package\"\"\"" > $dir/__init__.py
done

echo "✅ Directories created"

# Create placeholder files with minimal content
# These will be replaced with full content

# web/app.py
cat > web/app.py << 'EOF'
from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'service': 'Crypto Twitter Bot', 'status': 'online'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})

@app.route('/wake')
def wake():
    return jsonify({'status': 'awake'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
EOF

# analytics/tracker.py
cat > analytics/tracker.py << 'EOF'
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class AnalyticsTracker:
    def __init__(self):
        logger.info("Analytics tracker initialized")
    
    def calculate_daily_metrics(self):
        logger.info("Calculating daily metrics...")
EOF

# analytics/dashboard.py
cat > analytics/dashboard.py << 'EOF'
import logging

logger = logging.getLogger(__name__)

class Dashboard:
    def __init__(self):
        logger.info("Dashboard initialized")
    
    def print_daily_report(self):
        logger.info("📊 Daily report generated")
EOF

# models/content_generator.py
cat > models/content_generator.py << 'EOF'
import openai
import os
import logging

logger = logging.getLogger(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

class ContentGenerator:
    def __init__(self):
        self.model = 'gpt-3.5-turbo'
        logger.info("Content generator initialized")
    
    def generate_tweet(self, topic, content_type='global', context=None):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": f"Write a tweet about {topic}"}],
                max_tokens=100
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Generation error: {e}")
            return None
    
    def generate_reply(self, original_tweet, username, sentiment="neutral"):
        return f"Thanks for sharing @{username}!"
    
    def generate_thread(self, topic, context=None):
        return [f"Thread about {topic} 🧵", "Point 1", "Point 2", "Conclusion"]
EOF

# models/humanizer.py
cat > models/humanizer.py << 'EOF'
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
EOF

# models/sentiment_analyzer.py
cat > models/sentiment_analyzer.py << 'EOF'
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
    
    def analyze(self, text):
        scores = self.vader.polarity_scores(text)
        compound = scores['compound']
        if compound >= 0.05:
            return 'positive', compound
        elif compound <= -0.05:
            return 'negative', compound
        return 'neutral', compound
    
    def should_respond(self, text, username):
        sentiment, score = self.analyze(text)
        return score > -0.7
EOF

# models/engagement_predictor.py
cat > models/engagement_predictor.py << 'EOF'
import logging
from datetime import datetime
import pytz

logger = logging.getLogger(__name__)

class EngagementPredictor:
    def __init__(self, timezone='Africa/Nairobi'):
        self.tz = pytz.timezone(timezone)
    
    def record_performance(self, tweet_id, score):
        logger.info(f"Recorded performance for {tweet_id}: {score}")
    
    def get_best_posting_time(self):
        return None
    
    def get_content_type_performance(self):
        return {}
EOF

# core/tweet_manager.py
cat > core/tweet_manager.py << 'EOF'
import tweepy
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class TweetManager:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_SECRET'),
            wait_on_rate_limit=True
        )
        self.daily_tweet_count = 0
        logger.info("Tweet manager initialized")
    
    def post_tweet(self, content, content_type='global', media_ids=None):
        try:
            response = self.client.create_tweet(text=content)
            logger.info(f"✅ Posted: {content[:50]}...")
            return response.data['id']
        except Exception as e:
            logger.error(f"Tweet error: {e}")
            return None
    
    def post_thread(self, tweets_list, content_type='thread'):
        logger.info(f"Posting thread with {len(tweets_list)} tweets")
        return None
    
    def like_tweet(self, tweet_id):
        return True
    
    def get_tweet_metrics(self, tweet_id):
        return None
    
    def update_tweet_engagement(self, tweet_id):
        pass
EOF

# core/reply_handler.py
cat > core/reply_handler.py << 'EOF'
import logging
import time
import random

logger = logging.getLogger(__name__)

class ReplyHandler:
    def __init__(self, tweet_manager):
        self.tweet_manager = tweet_manager
        self.hourly_reply_count = 0
        self.replied_to = set()
        logger.info("Reply handler initialized")
    
    def process_mention(self, tweet_id, tweet_text, username):
        logger.info(f"Processing mention from @{username}")
        return True
    
    def cleanup_replied_to(self):
        self.replied_to.clear()
EOF

# core/thread_builder.py
cat > core/thread_builder.py << 'EOF'
import logging

logger = logging.getLogger(__name__)

class ThreadBuilder:
    def __init__(self, tweet_manager):
        self.tweet_manager = tweet_manager
        logger.info("Thread builder initialized")
    
    def post_scheduled_thread(self, thread_type='market_analysis'):
        logger.info(f"Building {thread_type} thread")
        return None
EOF

# core/scheduler.py
cat > core/scheduler.py << 'EOF'
import schedule
import time
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class SmartScheduler:
    def __init__(self, tweet_manager, reply_handler, thread_builder):
        self.tweet_manager = tweet_manager
        self.reply_handler = reply_handler
        self.thread_builder = thread_builder
        logger.info("Scheduler initialized")
    
    def daily_scrape(self):
        logger.info("🔍 Running daily scrape...")
    
    def setup_schedule(self):
        schedule.every(30).minutes.do(lambda: logger.info("Heartbeat ❤️"))
        logger.info("✅ Schedule configured")
    
    def run(self):
        self.setup_schedule()
        logger.info("🚀 Scheduler running...")
        while True:
            schedule.run_pending()
            time.sleep(60)
EOF

# scrapers/news_scraper.py
cat > scrapers/news_scraper.py << 'EOF'
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
EOF

# scrapers/market_data.py
cat > scrapers/market_data.py << 'EOF'
import requests
import logging

logger = logging.getLogger(__name__)

class MarketDataFetcher:
    def __init__(self):
        self.coingecko_base = 'https://api.coingecko.com/api/v3'
    
    def get_btc_price(self):
        try:
            url = f"{self.coingecko_base}/simple/price"
            params = {'ids': 'bitcoin', 'vs_currencies': 'usd', 'include_24hr_change': 'true'}
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            return {'price_usd': data['bitcoin']['usd'], 'change_24h': data['bitcoin'].get('usd_24h_change', 0)}
        except:
            return None
    
    def get_trending(self):
        return []
EOF

# scrapers/reddit_scraper.py
cat > scrapers/reddit_scraper.py << 'EOF'
import logging

logger = logging.getLogger(__name__)

class RedditScraper:
    def __init__(self):
        self.enabled = False
    
    def get_hot_topics(self, limit=10):
        return []
EOF

# scrapers/twitter_monitor.py
cat > scrapers/twitter_monitor.py << 'EOF'
import logging

logger = logging.getLogger(__name__)

class TwitterMonitor:
    def __init__(self, bearer_token=None):
        pass
    
    def get_mentions(self, username, limit=10):
        return []
    
    def search_keywords(self, keywords, limit=20):
        return []
EOF

# utils/text_utils.py
cat > utils/text_utils.py << 'EOF'
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
EOF

# utils/image_generator.py
cat > utils/image_generator.py << 'EOF'
import logging

logger = logging.getLogger(__name__)

class ImageGenerator:
    def __init__(self):
        self.enabled = False
    
    def generate_price_chart(self, data, title="Chart", filename=None):
        return None
EOF

# utils/validators.py
cat > utils/validators.py << 'EOF'
class Validators:
    @staticmethod
    def is_valid_tweet_length(text, max_length=280):
        return len(text) <= max_length
EOF

# scripts/init_db.py
cat > scripts/init_db.py << 'EOF'
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.database import init_db

if __name__ == '__main__':
    print("Initializing database...")
    init_db()
    print("✅ Database ready!")
EOF

# scripts/cleanup.py
cat > scripts/cleanup.py << 'EOF'
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Cleanup complete!")
EOF

# data/content_templates.json
cat > data/content_templates.json << 'EOF'
{"templates": {}, "hashtag_sets": {}}
EOF

# data/.gitkeep
touch data/.gitkeep

echo "✅ All files created!"
echo ""
echo "📁 Project structure:"
find . -name "*.py" -not -path "./.git/*" | sort

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

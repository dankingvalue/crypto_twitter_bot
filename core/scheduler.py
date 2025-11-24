import schedule
import time
import logging
from datetime import datetime
import random

logger = logging.getLogger(__name__)

class SmartScheduler:
    def __init__(self, tweet_manager, reply_handler, thread_builder):
        self.tweet_manager = tweet_manager
        self.reply_handler = reply_handler
        self.thread_builder = thread_builder
        logger.info("Scheduler initialized")
    
    def post_regular_tweet(self):
        """Post a regular crypto update tweet"""
        try:
            logger.info("📝 Posting regular tweet...")
            # Your tweet posting logic here
            # Example: self.tweet_manager.post_tweet()
            logger.info("✅ Tweet posted successfully")
        except Exception as e:
            logger.error(f"❌ Failed to post tweet: {e}")
    
    def post_market_update(self):
        """Post market analysis/update"""
        try:
            logger.info("📊 Posting market update...")
            # Your market update logic here
            logger.info("✅ Market update posted")
        except Exception as e:
            logger.error(f"❌ Failed to post market update: {e}")
    
    def check_replies(self):
        """Check and respond to mentions/replies"""
        try:
            logger.info("💬 Checking for replies...")
            # Your reply checking logic here
            # Example: self.reply_handler.check_mentions()
            logger.info("✅ Replies checked")
        except Exception as e:
            logger.error(f"❌ Failed to check replies: {e}")
    
    def daily_scrape(self):
        """Scrape news and trending topics"""
        try:
            logger.info("🔍 Running daily scrape...")
            # Your scraping logic here
            logger.info("✅ Scraping complete")
        except Exception as e:
            logger.error(f"❌ Failed to scrape: {e}")
    
    def setup_schedule(self):
        """Configure the posting schedule"""
        
        # Post tweets every 4 hours (6 times per day)
        schedule.every(4).hours.do(self.post_regular_tweet)
        
        # Post market updates twice daily at specific times
        schedule.every().day.at("09:00").do(self.post_market_update)
        schedule.every().day.at("21:00").do(self.post_market_update)
        
        # Check for replies every 30 minutes
        schedule.every(30).minutes.do(self.check_replies)
        
        # Daily scraping at 6 AM
        schedule.every().day.at("06:00").do(self.daily_scrape)
        
        # Heartbeat every 30 minutes for monitoring
        schedule.every(30).minutes.do(lambda: logger.info("❤️ Heartbeat - Bot is alive"))
        
        # Log all scheduled jobs
        logger.info("✅ Schedule configured:")
        logger.info("   📝 Regular tweets: Every 4 hours")
        logger.info("   📊 Market updates: 9:00 AM & 9:00 PM daily")
        logger.info("   💬 Reply checks: Every 30 minutes")
        logger.info("   🔍 News scraping: 6:00 AM daily")
        logger.info("   ❤️ Heartbeat: Every 30 minutes")
        
        # Log next run times
        jobs = schedule.get_jobs()
        logger.info(f"📅 {len(jobs)} jobs scheduled")
        for job in jobs:
            logger.info(f"   Next run: {job.next_run}")
    
    def run(self):
        """Main scheduler loop"""
        self.setup_schedule()
        logger.info("🚀 Scheduler running...")
        logger.info(f"⏰ Current time: {datetime.now()}")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

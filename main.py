"""
Crypto Twitter Bot - Main Entry Point
"""
import os
import sys
import logging
import signal
import threading
from datetime import datetime

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)
logger.info(f"Python version: {sys.version}")
logger.info(f"Project root: {PROJECT_ROOT}")

# Import components
try:
    from core.tweet_manager import TweetManager
    from core.reply_handler import ReplyHandler
    from core.thread_builder import ThreadBuilder
    from core.scheduler import SmartScheduler
    from analytics.tracker import AnalyticsTracker
    from analytics.dashboard import Dashboard
    logger.info("✅ All imports successful!")
except ImportError as e:
    logger.error(f"❌ Import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

class BotOrchestrator:
    def __init__(self):
        self.running = False
        signal.signal(signal.SIGTERM, self.shutdown)
        signal.signal(signal.SIGINT, self.shutdown)
    
    def initialize(self):
        try:
            logger.info("🚀 Initializing Crypto Twitter Bot...")
            
            self.tweet_manager = TweetManager()
            logger.info("✅ Tweet Manager initialized")
            
            self.reply_handler = ReplyHandler(self.tweet_manager)
            logger.info("✅ Reply Handler initialized")
            
            self.thread_builder = ThreadBuilder(self.tweet_manager)
            logger.info("✅ Thread Builder initialized")
            
            self.scheduler = SmartScheduler(
                self.tweet_manager,
                self.reply_handler,
                self.thread_builder
            )
            logger.info("✅ Scheduler initialized")
            
            self.analytics = AnalyticsTracker()
            logger.info("✅ Analytics initialized")
            
            self.dashboard = Dashboard()
            logger.info("✅ Dashboard initialized")
            
            self.running = True
            logger.info("✅ All components initialized!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Init failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def start_web_server(self):
        """Start Flask server only if not running under gunicorn"""
        # Check if running under gunicorn
        if 'gunicorn' in os.getenv('SERVER_SOFTWARE', '').lower() or \
           os.getenv('GUNICORN_CMD_ARGS') or \
           'gunicorn' in ' '.join(sys.argv):
            logger.info("🌐 Running under gunicorn - skipping Flask server startup")
            return
        
        def run_server():
            try:
                from web.app import app
                port = int(os.getenv('PORT', 10000))
                logger.info(f"🌐 Starting web server on port {port}...")
                app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
            except Exception as e:
                logger.error(f"Web server error: {e}")
        
        web_thread = threading.Thread(target=run_server, daemon=True)
        web_thread.start()
        logger.info("✅ Web server started")
    
    def run(self):
        if not self.initialize():
            logger.error("❌ Failed to initialize")
            sys.exit(1)
        
        self.start_web_server()
        
        print("\n" + "="*50)
        print("🤖 CRYPTO TWITTER BOT - ONLINE 🚀")
        print("="*50)
        print(f"⏰ Started: {datetime.now()}")
        print(f"🌐 Health: /health endpoint active")
        print("="*50 + "\n")
        
        try:
            self.scheduler.run()
        except KeyboardInterrupt:
            self.shutdown()
    
    def shutdown(self, signum=None, frame=None):
        if not self.running:
            return
        
        logger.info("🛑 Shutting down...")
        self.running = False
        sys.exit(0)

if __name__ == '__main__':
    bot = BotOrchestrator()
    bot.run()

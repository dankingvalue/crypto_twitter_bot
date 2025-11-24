import logging

logger = logging.getLogger(__name__)

class Dashboard:
    def __init__(self):
        logger.info("Dashboard initialized")
    
    def print_daily_report(self):
        logger.info("📊 Daily report generated")

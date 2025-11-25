"""Content generator for crypto tweets"""
import random
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self):
        self.crypto_topics = [
            "Bitcoin", "Ethereum", "Solana", "Cardano", "Polygon",
            "DeFi", "NFTs", "Web3", "Smart Contracts", "Layer 2"
        ]
        
        self.market_terms = [
            "bullish momentum", "consolidation phase", "key resistance level",
            "strong support", "breakout potential", "market correction",
            "accumulation zone", "price discovery", "volatility spike"
        ]
        
        self.general_insights = [
            "The crypto market never sleeps 🌙",
            "Building in a bear market pays off in a bull market 📈",
            "DYOR is not just advice, it's a survival strategy 🔍",
            "Smart contracts are reshaping finance as we know it ⚡",
            "Decentralization is the future of the internet 🌐"
        ]
        
    def generate_regular_tweet(self):
        """Generate a regular crypto insight tweet"""
        templates = [
            f"📊 {random.choice(self.crypto_topics)} showing {random.choice(self.market_terms)} today. Market watching closely. #Crypto",
            f"💡 Quick take: {random.choice(self.general_insights)} #CryptoTwitter",
            f"🔥 {random.choice(self.crypto_topics)} ecosystem continues to evolve. Innovation never stops in crypto. #Web3",
            f"⚡ The {random.choice(self.crypto_topics)} network is seeing increased activity. Adoption is key. #Blockchain",
            f"🌟 {random.choice(self.general_insights)} Stay informed, stay ahead. #CryptoNews"
        ]
        
        tweet = random.choice(templates)
        logger.info(f"Generated tweet: {tweet[:50]}...")
        return tweet
    
    def generate_market_update(self):
        """Generate a market analysis tweet"""
        time_of_day = "Morning" if datetime.now().hour < 12 else "Evening"
        
        templates = [
            f"📈 {time_of_day} Market Update:\n\n"
            f"{random.choice(self.crypto_topics)} shows {random.choice(self.market_terms)}\n"
            f"Key levels to watch 👀\n\n"
            f"#Crypto #MarketAnalysis",
            
            f"🌅 {time_of_day} Crypto Roundup:\n\n"
            f"• {random.choice(self.crypto_topics)}: {random.choice(self.market_terms)}\n"
            f"• Market sentiment: Cautiously optimistic\n"
            f"• Volume: Moderate\n\n"
            f"#CryptoMarket",
            
            f"💼 {time_of_day} Market Brief:\n\n"
            f"{random.choice(self.general_insights)}\n\n"
            f"Focus: {random.choice(self.crypto_topics)}\n"
            f"Trend: {random.choice(self.market_terms)}\n\n"
            f"#Bitcoin #Ethereum"
        ]
        
        tweet = random.choice(templates)
        logger.info(f"Generated market update: {tweet[:50]}...")
        return tweet
    
    def generate_thread(self, topic=None):
        """Generate a thread of tweets"""
        topic = topic or random.choice(self.crypto_topics)
        
        thread = [
            f"🧵 Thread: Understanding {topic} in 2024\n\n1/5",
            f"2/5 {topic} has evolved significantly. The ecosystem is growing faster than ever. Key developments to watch:",
            f"3/5 Innovation in {topic} is driven by community and technology. Real-world adoption is increasing.",
            f"4/5 Challenges remain: scalability, regulation, and mainstream adoption. But progress is undeniable.",
            f"5/5 Bottom line: {topic} is here to stay. The question isn't if, but how fast adoption will scale. 🚀"
        ]
        
        return thread

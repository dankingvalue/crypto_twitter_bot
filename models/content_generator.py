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

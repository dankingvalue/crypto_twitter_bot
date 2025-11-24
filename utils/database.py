"""
Database models and connection
"""

import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

engine = create_engine(
    DATABASE_URL or 'sqlite:///data/bot.db',
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
) if DATABASE_URL else create_engine('sqlite:///data/bot.db')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    
    id = Column(Integer, primary_key=True)
    tweet_id = Column(String(50), unique=True, index=True)
    content = Column(Text)
    posted_at = Column(DateTime, default=datetime.utcnow)
    engagement_score = Column(Float, default=0.0)
    likes = Column(Integer, default=0)
    retweets = Column(Integer, default=0)
    replies = Column(Integer, default=0)
    impressions = Column(Integer, default=0)
    is_thread = Column(Boolean, default=False)
    thread_id = Column(String(50), nullable=True)
    content_type = Column(String(50))
    hashtags = Column(JSON)

class Reply(Base):
    __tablename__ = 'replies'
    
    id = Column(Integer, primary_key=True)
    reply_id = Column(String(50), unique=True)
    original_tweet_id = Column(String(50))
    original_author = Column(String(100))
    reply_content = Column(Text)
    replied_at = Column(DateTime, default=datetime.utcnow)
    sentiment = Column(String(20))

class ScrapedContent(Base):
    __tablename__ = 'scraped_content'
    
    id = Column(Integer, primary_key=True)
    source = Column(String(100))
    title = Column(Text)
    content = Column(Text)
    url = Column(Text)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    relevance_score = Column(Float, default=0.0)
    used = Column(Boolean, default=False)
    category = Column(String(50))

class BotMetrics(Base):
    __tablename__ = 'bot_metrics'
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    total_tweets = Column(Integer, default=0)
    total_replies = Column(Integer, default=0)
    total_followers = Column(Integer, default=0)
    engagement_rate = Column(Float, default=0.0)
    top_performing_tweet = Column(String(50))
    daily_impressions = Column(Integer, default=0)

class ContentQueue(Base):
    __tablename__ = 'content_queue'
    
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    content_type = Column(String(50))
    scheduled_time = Column(DateTime)
    posted = Column(Boolean, default=False)
    posted_at = Column(DateTime, nullable=True)
    priority = Column(Integer, default=5)
    generated_by = Column(String(50))
    metadata = Column(JSON)

class EngagementPattern(Base):
    __tablename__ = 'engagement_patterns'
    
    id = Column(Integer, primary_key=True)
    hour_of_day = Column(Integer)
    day_of_week = Column(Integer)
    avg_engagement = Column(Float)
    tweet_count = Column(Integer)
    best_content_type = Column(String(50))

def get_db_session():
    return SessionLocal()

def init_db():
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Database initialized")

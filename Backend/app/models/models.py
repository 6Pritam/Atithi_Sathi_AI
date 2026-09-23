from sqlalchemy import Column, Integer, String, Text, Float, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    description = Column(Text)
    rating = Column(Float)
    review_count = Column(Integer)
    image_url = Column(String)
    distance_info = Column(String)
    amenities = Column(JSON) # List of amenities
    base_price = Column(Float)
    
    rooms = relationship("Room", back_populates="hotel")

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(String, primary_key=True, index=True)
    hotel_id = Column(String, ForeignKey("hotels.id"))
    name = Column(String, index=True)
    max_guests = Column(Integer)
    price_per_night = Column(Float)
    currency = Column(String, default="INR")
    amenities = Column(JSON)
    cancellation_policy = Column(String)
    
    hotel = relationship("Hotel", back_populates="rooms")

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    messages = relationship("Message", back_populates="conversation")

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(String, ForeignKey("conversations.id"), index=True)
    sender = Column(String) # 'user' or 'ai'
    content = Column(Text)
    message_type = Column(String, default="text")
    attached_data = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    conversation = relationship("Conversation", back_populates="messages")

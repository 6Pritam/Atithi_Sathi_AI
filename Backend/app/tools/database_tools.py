from sqlalchemy.orm import Session
from app.models.models import Hotel, Room
import json
from typing import List, Optional
from datetime import datetime
import httpx
from app.core.config import SERPAPI_API_KEY

def search_hotels(db: Session, location: str = None, amenities: List[str] = None, max_price: float = None, minimum_rating: float = None):
    """
    Search for hotels based on criteria.
    """
    query = db.query(Hotel)
    
    if location:
        query = query.filter(Hotel.location.ilike(f"%{location}%"))
    if minimum_rating:
        query = query.filter(Hotel.rating >= minimum_rating)
    if max_price:
        query = query.filter(Hotel.base_price <= max_price)
        
    hotels = query.all()
    
    results = []
    for hotel in hotels:
        # Basic filtering for amenities if provided
        if amenities and hotel.amenities:
            if not all(any(a.lower() in ha.lower() for ha in hotel.amenities) for a in amenities):
                continue
                
        results.append({
            "id": hotel.id,
            "name": hotel.name,
            "location": hotel.location,
            "rating": hotel.rating,
            "base_price": hotel.base_price,
            "amenities": hotel.amenities,
            "image_url": hotel.image_url,
            "distance_info": hotel.distance_info,
            "review_count": hotel.review_count,
            "description": hotel.description
        })
        
    return {"hotels": results, "count": len(results)}

def get_hotel_details(db: Session, hotel_id: str):
    """
    Get detailed information about a specific hotel including rooms.
    """
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel:
        return {"error": "Hotel not found"}
    
    rooms = db.query(Room).filter(Room.hotel_id == hotel_id).all()
    room_list = [{
        "id": r.id,
        "name": r.name,
        "max_guests": r.max_guests,
        "price_per_night": r.price_per_night,
        "currency": r.currency,
        "amenities": r.amenities,
        "cancellation_policy": r.cancellation_policy
    } for r in rooms]
    
    return {
        "id": hotel.id,
        "name": hotel.name,
        "location": hotel.location,
        "description": hotel.description,
        "rating": hotel.rating,
        "review_count": hotel.review_count,
        "image_url": hotel.image_url,
        "distance_info": hotel.distance_info,
        "amenities": hotel.amenities,
        "base_price": hotel.base_price,
        "rooms": room_list
    }

def get_hotel_policy(db: Session, hotel_id: str, policy_type: str):
    """
    Get specific policies for a hotel.
    """
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel:
        return {"error": "Hotel not found"}
        
    # In a real app this would be a separate table or JSON column. 
    # For now we'll mock generic policies for demonstration based on the hotel.
    policies = {
        "check_in": "Check-in time is 2:00 PM.",
        "check_out": "Check-out time is 11:00 AM.",
        "breakfast": "Breakfast is served from 7:00 AM to 10:30 AM." if "Breakfast" in str(hotel.amenities) else "Breakfast is not included.",
        "cancellation": "Cancellations made 48 hours before check-in are fully refundable.",
        "pets": "Pets are not allowed on the property."
    }
    
    return {
        "hotel_name": hotel.name,
        "policy_type": policy_type,
        "policy_details": policies.get(policy_type.lower(), "Policy details not available.")
    }

def check_availability(db: Session, hotel_id: str, check_in: str, check_out: str, adults: int):
    """
    Deterministic mock availability logic.
    """
    try:
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        if check_in_date >= check_out_date:
            return {"error": "check_out must be after check_in"}
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD"}
        
    if adults < 1:
        return {"error": "adults must be at least 1"}
        
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel:
        return {"error": "Hotel not found"}
        
    rooms = db.query(Room).filter(Room.hotel_id == hotel_id, Room.max_guests >= adults).all()
    
    if not rooms:
        return {"available": False, "rooms": []}
        
    room_list = [{
        "category": r.name,
        "price_per_night": r.price_per_night,
        "currency": r.currency,
        "max_guests": r.max_guests,
        "amenities": r.amenities,
        "cancellation_policy": r.cancellation_policy
    } for r in rooms]
    
    return {
        "available": True,
        "hotel_name": hotel.name,
        "check_in": check_in,
        "check_out": check_out,
        "adults": adults,
        "rooms": room_list
    }

def search_web(query: str):
    """
    Search the web using SerpApi.
    """
    if not SERPAPI_API_KEY:
        return {"error": "SERPAPI_API_KEY is not configured."}
        
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }
    
    try:
        with httpx.Client() as client:
            response = client.get(url, params=params, timeout=15.0)
            response.raise_for_status()
            data = response.json()
            
            results = []
            if "organic_results" in data:
                for res in data["organic_results"][:3]:
                    results.append({
                        "title": res.get("title"),
                        "snippet": res.get("snippet"),
                        "link": res.get("link")
                    })
            if not results:
                return {"message": "No relevant results found."}
                
            return {"results": results}
    except Exception as e:
        return {"error": f"Failed to search web: {str(e)}"}

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "get_hotel_details",
            "description": "Get detailed information about a specific hotel by ID, including its rooms and basic amenities.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hotel_id": {
                        "type": "string",
                        "description": "The ID of the hotel."
                    }
                },
                "required": ["hotel_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_hotels",
            "description": "Search for hotels based on location, amenities, price, or rating.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location or city to search for (e.g. 'Bengaluru')."
                    },
                    "amenities": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of desired amenities (e.g., ['Pool', 'Wi-Fi'])."
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Maximum base price per night in INR."
                    },
                    "minimum_rating": {
                        "type": "number",
                        "description": "Minimum user rating (1-5)."
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_hotel_policy",
            "description": "Get specific policies for a hotel, like check_in, check_out, breakfast, cancellation, or pets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hotel_id": {
                        "type": "string",
                        "description": "The ID of the hotel."
                    },
                    "policy_type": {
                        "type": "string",
                        "enum": ["check_in", "check_out", "breakfast", "cancellation", "pets"],
                        "description": "The type of policy to retrieve."
                    }
                },
                "required": ["hotel_id", "policy_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": "Check if rooms are available for specific dates and number of guests.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hotel_id": {
                        "type": "string",
                        "description": "The ID of the hotel."
                    },
                    "check_in": {
                        "type": "string",
                        "description": "Check-in date in YYYY-MM-DD format."
                    },
                    "check_out": {
                        "type": "string",
                        "description": "Check-out date in YYYY-MM-DD format."
                    },
                    "adults": {
                        "type": "integer",
                        "description": "Number of adults staying."
                    }
                },
                "required": ["hotel_id", "check_in", "check_out", "adults"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Use this tool to search the internet for live information, weather, flights, or attractions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to look up on the web."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

from app.models.database import engine, Base, SessionLocal
from app.models.models import Hotel, Room
import os

def seed():
    print("Initializing database schema...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    hotels_data = [
        {
            "id": "h_1",
            "name": "The Grand Horizon Hotel & Spa",
            "location": "Indiranagar, BLR",
            "description": "Halasuru Lake enclave • 8 mins to Central Business District",
            "rating": 4.8,
            "review_count": 1240,
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuAlLgmZwdK0o8dUpgdDbD9ICJLF6ctMY3SuG6N3D-84lXPrdH9tdiAx8jPHydr3y_6OMfMzpAcYV3n9PmZ_bOTd7wo8a5oFY773U0cVvjiTNepM34dAVMp4u_wG2lza0e38mdorgBOInbhGy8nJjMkSevIuEHohgbFZfH5N0uGDF43bako2KW8v0sd6CPos7hx_KjPTFF0wmCpoMfDp3F2086yinvqx3svKyU876nCkfYPmjmtndJp7SQ",
            "distance_info": "Halasuru Lake enclave • 8 mins to Central Business District",
            "amenities": ["Chef's Breakfast Included", "High-Speed Wi-Fi (150 Mbps)", "Temperature-Controlled Lap Pool", "24/7 Concierge"],
            "base_price": 7200
        },
        {
            "id": "h_2",
            "name": "The Royal Heritage Sanctuary",
            "location": "Palace Grounds, BLR",
            "description": "Palace Road enclave • Heritage colonial acreage",
            "rating": 4.9,
            "review_count": 890,
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuA3W7LA2tpAMGSpKcmJ8FjuReNCSuPJdraOcakgCw_bbiZ9VMO-5Lzca-X-HTjH0xKR6jukb_-a1xaGhlXf6VgNFb-OiwcI0lszp2LomkjRHFJ_e9d1MWz7WjNWQhO91qdRR0TZkBhFzWoxQGzNimIlSmWGpl0Gwy3RK3R58LgUKGlSsDnbiM4QTKtXUN-1Vq4i8ELD4tLuqmg7X_CHQSItLMysZJwcUQfcFAvlHM7xAo6MWDj0F6CugA",
            "distance_info": "Palace Road enclave • Heritage colonial acreage",
            "amenities": ["Artisanal Breakfast", "Olympic Pool", "Ayurvedic Spa", "Private Verandahs"],
            "base_price": 11500
        }
    ]

    rooms_data = [
        {
            "id": "r_1_1",
            "hotel_id": "h_1",
            "name": "Executive Garden Deluxe",
            "max_guests": 2,
            "price_per_night": 7200,
            "currency": "INR",
            "amenities": ["King Bed", "Wi-Fi", "Garden View", "Bathtub"],
            "cancellation_policy": "Free cancellation 24h before check-in"
        },
        {
            "id": "r_1_2",
            "hotel_id": "h_1",
            "name": "Lakeview Suite",
            "max_guests": 3,
            "price_per_night": 12500,
            "currency": "INR",
            "amenities": ["King Bed", "Wi-Fi", "Lake View", "Jacuzzi", "Living Area"],
            "cancellation_policy": "Non-refundable"
        },
        {
            "id": "r_2_1",
            "hotel_id": "h_2",
            "name": "Heritage Classic Room",
            "max_guests": 2,
            "price_per_night": 11500,
            "currency": "INR",
            "amenities": ["Queen Bed", "Wi-Fi", "Antique Furniture", "Balcony"],
            "cancellation_policy": "Free cancellation 48h before check-in"
        },
        {
            "id": "r_2_2",
            "hotel_id": "h_2",
            "name": "Royal Verandah Suite",
            "max_guests": 4,
            "price_per_night": 22000,
            "currency": "INR",
            "amenities": ["2 King Beds", "Wi-Fi", "Private Verandah", "Butler Service"],
            "cancellation_policy": "Free cancellation 48h before check-in"
        }
    ]

    hotel_count = 0
    room_count = 0

    # Seed Hotels (idempotent)
    for h_data in hotels_data:
        existing = db.query(Hotel).filter(Hotel.id == h_data["id"]).first()
        if existing:
            # Update
            for key, value in h_data.items():
                setattr(existing, key, value)
        else:
            # Create
            new_hotel = Hotel(**h_data)
            db.add(new_hotel)
            hotel_count += 1
            
    # Seed Rooms (idempotent)
    for r_data in rooms_data:
        existing = db.query(Room).filter(Room.id == r_data["id"]).first()
        if existing:
            # Update
            for key, value in r_data.items():
                setattr(existing, key, value)
        else:
            # Create
            new_room = Room(**r_data)
            db.add(new_room)
            room_count += 1

    db.commit()
    
    total_hotels = db.query(Hotel).count()
    total_rooms = db.query(Room).count()
    
    db.close()
    
    print("\nSeed completed successfully.")
    print(f"Hotels inserted/updated: {hotel_count} (Total: {total_hotels})")
    print(f"Rooms inserted/updated: {room_count} (Total: {total_rooms})")
    print("Database: atithi_saathi.db")

if __name__ == "__main__":
    seed()

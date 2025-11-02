from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://mongo_db:27017"
DB_NAME = "fastapi_db"

client = AsyncIOMotorClient(MONGO_URL)
database = client[DB_NAME]
users_collection = database["users"]
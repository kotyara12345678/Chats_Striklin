from app.database import users_collection
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserDAO:

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        data = await users_collection.find_one(filter_by)
        if not data:
            return None
        data["id"] = str(data["_id"])
        return data

    @classmethod
    async def get_user_by_email(cls, email: str):
        return await cls.find_one_or_none(email=email)

    @classmethod
    async def add(cls, name: str, email: str, hashed_password: str):
        user_doc = {
            "name": name,
            "email": email,
            "hashed_password": hashed_password,
        }
        result = await users_collection.insert_one(user_doc)
        user_doc["_id"] = result.inserted_id
        user_doc["id"] = str(result.inserted_id)
        return user_doc

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
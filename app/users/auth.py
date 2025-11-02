from passlib.context import CryptContext
from pydantic import EmailStr
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.config import get_auth_data
from app.users.dao import UserDAO


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=366)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encoded_jwt = jwt.encode(to_encode, auth_data["secret_key"], algorithm=auth_data['algorithm'])
    return encoded_jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(email: str, password: str):
    user = await UserDAO.find_one_or_none(email=email)
    if not user:
        return None
    if not UserDAO.verify_password(password, user['hashed_password']):
        return None
    return user
from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, timezone
from app.config import get_auth_data
from app.exeptions import TokenExpiredException, NoUserIdExeption, TokenNoFoundException
from app.users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise TokenExpiredException()
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=auth_data['algorithms'])
    except JWTError:
        raise NoUserIdExeption()

    expire: str = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise TokenExpiredException()

    user_id: str = payload.get('sub')
    if not user_id:
        raise NoUserIdExeption()

    user = await UserDAO.find_one_or_none_by_id(int(user_id))
    if not user:
        raise NoUserIdExeption(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user
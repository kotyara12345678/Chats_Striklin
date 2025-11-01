from fastapi import status, HTTPException

class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истек!")


class TokenNoFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не был найден")


UserAlreadyExistsException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует!")

PasswordMismatchException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Пароли не совпадают!")

IncorrectEmailOrPasswordException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="неверная почта или пароль")

NoJwtExeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не валидный!")

NoUserIdExeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не найден ID пользователя")

ForbiddenExeption = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Не достаточно прав!")
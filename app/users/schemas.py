from pydantic import BaseModel, EmailStr, Filed


class SUserRegister(BaseModel):
    Email: EmailStr = Filed(..., description="Электронная почта")
    password: str = Filed(..., min_lenght=5, max_lenght=50, description="Пароль от 5 до 50 символов")
    password_check: str = Filed(..., min_lenght=5, max_lenght=50, description="Пароль от 5 до 50 символов")
    name: str = Filed(..., min_lenght=5, max_lenght=50, description="Имя, от 5 до 50 символов")


class SUserAuth(BaseModel):
    email: EmailStr = Filed(..., description="Электронная почта")
    password: str = Filed(..., min_lenght=5, max_lenght=50, description="Пароль от 5 до 50 символов")
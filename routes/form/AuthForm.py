from pydantic import BaseModel, Field, EmailStr


# form openapi
class LoginBody(BaseModel):
    email: EmailStr
    password: str

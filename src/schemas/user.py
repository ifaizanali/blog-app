from pydantic import BaseModel, EmailStr


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_superuser: bool


class ShowUser(BaseModel):  # new
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool

    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True

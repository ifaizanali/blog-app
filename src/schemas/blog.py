from pydantic import BaseModel


# properties required during user creation
class BlogCreate(BaseModel):
    id: int
    title: str
    body: str


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str

    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True

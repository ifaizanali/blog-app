from fastapi import APIRouter
from src.apis import blog, login, user

api_router = APIRouter()
api_router.include_router(blog.blog_router, prefix="/blog", tags=["Blog Routes"])
api_router.include_router(user.router, prefix="/user", tags=["User Routes"])
api_router.include_router(login.router, prefix="/login", tags=["login"])

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.models.user import User
from src.db.session import get_db
from src.schemas.blog import ShowBlog, BlogCreate
from src.db.Helpers.blog import create_new_blog, get_all_blogs, retreive_blog, delete_blog_by_id, update_blog_by_id
from src.apis.login import get_current_user_from_token
from typing import List

blog_router = APIRouter()


@blog_router.get("/", response_model=List[ShowBlog])
async def home(db: Session = Depends(get_db)):
    blogs = get_all_blogs(db=db)
    return blogs


@blog_router.post("/create-blog/", response_model=ShowBlog)
async def create_job(blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    blog = create_new_blog(blog=blog, db=db, owner_id=current_user.id)
    return blog


@blog_router.get('/get/{id}', response_model=ShowBlog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this id {id} does not exist")
    return blog


@blog_router.put("/update/{id}")
def update_job(id: int, blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    existing_blog = retreive_blog(id, db)
    if not existing_blog:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} does not exist")
    if existing_blog.owner_id == current_user.id or current_user.is_superuser:
        update_blog_by_id(id=id, blog=blog, db=db, owner_id=current_user)
        return {"msg": "Successfully updated data."}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@blog_router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} does not exist")
    if blog.owner_id == current_user.id or current_user.is_superuser:
        delete_blog_by_id(id=id, db=db)
        return {"msg": "Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"You are not permitted!!!!")

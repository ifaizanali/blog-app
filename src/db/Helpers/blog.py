from sqlalchemy.orm import Session
from src.models.blog import Blog
from src.schemas.blog import BlogCreate
from fastapi import HTTPException, status


def retreive_blog(id: int, db: Session):
    item = db.query(Blog).filter(Blog.id == id).first()
    return item


def create_new_blog(blog=BlogCreate, db=Session, owner_id=1):
    print(owner_id)
    blog = Blog(**blog.dict(),
                owner_id=owner_id
                )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def get_all_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def update_blog_by_id(id: int, blog: BlogCreate, db: Session):
    existing_blog = db.query(Blog).filter(Blog.id == id)
    if not existing_blog.first():
        return 0
    print(blog.__dict__)
    existing_blog.update(blog.__dict__)
    db.commit()
    return blog.__dict__


def delete_blog_by_id(id: int, db: Session):
    existing_blog = db.query(Blog).filter(Blog.id == id)
    if not existing_blog.first():
        return 0
    existing_blog.delete(synchronize_session=False)
    db.commit()


from src.db.base_class import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="blogs")

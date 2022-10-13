from datetime import datetime

from pydantic import BaseModel


class SessionData(BaseModel):
    username: str
    login_time: datetime
    
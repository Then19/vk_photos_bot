from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from bot.schemas import BaseModel
from bot.settings import settings


class User(BaseModel):
    telegram_id: int
    user_name: str
    token: UUID
    limit: int
    refs_count: int
    blocked_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def new_user(telegram_id: int, user_name: str) -> "User":
        return User(
            telegram_id=telegram_id,
            user_name=user_name,
            token=uuid4(),
            limit=settings.default_limit,
            refs_count=0,
            created_at=datetime.now().astimezone(),
            updated_at=datetime.now().astimezone()
        )

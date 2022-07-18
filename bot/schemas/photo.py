from datetime import datetime
from typing import Optional
from uuid import UUID

from bot.schemas import BaseModel


class VkPhoto(BaseModel):
    telegram_id: int
    user_name: str
    image_id: UUID
    chat_id: int
    chat_name: Optional[str]
    image_url: str
    image_path: Optional[str]
    image_date: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    def get_text_for_message(self):
        return f'<a href="{self.image_url}">{self.image_id}</a>\n' \
           f'Чат: {self.chat_name}\n' \
           f'Отправитель: {self.user_name}\n' \
           f'Дата: {self.image_date.strftime("%d.%m.%y %H:%M")}'

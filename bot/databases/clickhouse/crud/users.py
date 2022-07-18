from typing import Optional

from aiogram.types import Message
from sqlalchemy import func, tuple_
from sqlalchemy.orm import Session

from bot.databases.clickhouse.modeles.user import UserORM
from bot.schemas.user import User


def get_user(db: Session, message: Message) -> User:
    data = db.query(UserORM).filter(
        UserORM.telegram_id == message.from_user.id,
        tuple_(UserORM.telegram_id, UserORM.updated_at).in_(
            db.query(UserORM.telegram_id, func.max(UserORM.updated_at)).group_by(UserORM.telegram_id)
        )
    ).first()

    if not data:
        user = User.new_user(telegram_id=message.from_user.id, user_name=message.from_user.first_name)
        table = UserORM.__table__
        db.execute(table.insert(), [user.dict(), ])
        return user

    return User.from_orm(data)

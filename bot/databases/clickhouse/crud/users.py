from typing import Optional

from sqlalchemy import func, tuple_
from sqlalchemy.orm import Session

from bot.databases.clickhouse.modeles.user import UserORM
from bot.schemas.user import User


def get_user_by_telegram_id(db: Session, telegram_id: str, user_name: str) -> User:
    data = db.query(UserORM).filter(
        UserORM.telegram_id == telegram_id,
        tuple_(UserORM.telegram_id, UserORM.updated_at).in_(
            db.query(UserORM.telegram_id, func.max(UserORM.updated_at)).group_by(UserORM.telegram_id)
        )
    ).first()

    if not data:
        user = User.new_user(telegram_id=telegram_id, user_name=user_name)
        table = UserORM.__table__
        db.execute(table.insert(), [user.dict(), ])
        return user

    return User.from_orm(data)

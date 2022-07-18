from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    clickhouse_dsn: str
    admin_id: str
    default_limit: int = 75000


settings = Settings()

from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    clickhouse_dsn: str
    admin_id: str
    api_url: str
    default_limit: int = 30000


settings = Settings()

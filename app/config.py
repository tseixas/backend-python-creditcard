from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = "127.0.0.1"
    db_name: str = "creditcard"
    db_user: str = "postgres"
    db_password: str = "postgres"
    secret_key: str = "34fc16eb6fd5afaaa9b61aec70e5cef05b80c91f2dc502025b9ed9bd6100d897"
    algotithm: str = "HS256"
    token_expire_minutes: int = 30


settings = Settings()

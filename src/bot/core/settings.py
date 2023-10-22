import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    debug: bool = False
    secret_word: str = 'Бруня'
    logging_level: int = logging.DEBUG
    logging_format: str = '%(asctime)s, %(name)s, %(levelname)s, %(message)s'
    logging_dir: str = './src/bot/data/logs'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

from bot.core.logger import logger      # noqa

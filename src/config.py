from dataclasses import dataclass

from environs import Env

env = Env()
env.read_env(".env")


@dataclass
class Config:
    api_key = env.str("API_KEY")

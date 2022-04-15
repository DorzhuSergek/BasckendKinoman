from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str,
                    default="415d07709fbe02fc6fe48a3ea06e815830ffcef0e090ec4ff1e548cf81a8d449")

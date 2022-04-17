import datetime
import statistics
from fastapi import HTTPException, Request
from passlib.hash import pbkdf2_sha256
from jose import jwt
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from fastapi.security import HTTPBearer


def verify_password(password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() +
                      datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        encode_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return encode_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        exp = HTTPException(
            status_code=statistics.HTTP_403_FORBIDDEN, detail="Invalid auth token")
        if credentials:
            token = decode_access_token(credentials.credentials)
            if token is None:
                raise exp
            return credentials.credentials
        else:
            raise exp

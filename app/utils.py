from datetime import datetime, timedelta
import jwt

from uuid import uuid4

def encode_token(data: dict, exp: timedelta) -> str:

    token = jwt.encode(
        {
            **data,
            "jti": uuid4().hex,
            "exp": datetime.now() + timedelta(days=3)
        },
        key="secret",
        algorithm="HS256",
    )

    return token


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(
            token,
            key="secret",
            algorithms=["HS256"],
        )
        return payload
    except jwt.PyJWTError:
        return None
from datetime import datetime, timedelta
import jwt

def encode_token(data: dict, exp: timedelta) -> str:

    token = jwt.encode(
        {**data, "exp": datetime.now() + timedelta(days=3)},
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
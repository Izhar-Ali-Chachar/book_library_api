from redis.asyncio import Redis

_blocked_tokens = Redis(host='localhost', port=6379, db=0, decode_responses=True)

async def black_list_token(jti: str):
    await _blocked_tokens.set(jti, "blacklisted")

async def is_token_blacklisted(jti: str) -> bool:
    exists = await _blocked_tokens.exists(jti)
    return bool(exists)

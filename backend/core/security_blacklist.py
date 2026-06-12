from backend.core.redis import redis_client


def blacklist_token(token: str, exp_seconds: int):
    redis_client.setex(
        f"blacklist: {token}",
        exp_seconds,
        "1"
    )

def is_blacklisted(token: str) -> bool:
    return redis_client.get(f"blacklist: {token}") is not None
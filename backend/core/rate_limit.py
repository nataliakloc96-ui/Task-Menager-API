from fastapi import HTTPException
from backend.core.redis import redis_client


def rate_limit(ip: str, limit: int = 5, window: int = 60):
    key = f"rate: {ip}"

    current = redis_client.get(key)

    if current and int(current) >= limit:
        raise HTTPException(
            status_code=429,
            detail="Too many requests"
        )
    
    pipe = redis_client.pipeline()
    pipe.incr(key)
    pipe.expire(key, window)
    pipe.execute()
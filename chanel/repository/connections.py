import json
from typing import Any, Dict
from aioredis import Redis, create_redis_pool


class RedisConnection:
    redis: Redis = None

    @classmethod
    async def initialize(cls, connection_info):
        if cls.redis and not cls.redis.closed:
            return cls.redis

        cls.redis = await create_redis_pool(**connection_info)

        return cls.redis

    @classmethod
    async def destroy(cls):
        if cls.redis:
            cls.redis.close()
            await cls.redis.wait_closed()

        cls.redis = None

    @classmethod
    async def set(cls, key: str, value: Dict[str, Any]) -> None:
        dumped_value = json.dumps(value)
        await cls.redis.set(key, dumped_value)

    @classmethod
    async def delete(cls, key: str) -> None:
        await cls.redis.delete(key)

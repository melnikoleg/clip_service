from typing import AsyncGenerator, List

from fastapi import Depends
from starlette.requests import Request

from clip_service.settings import settings


async def get_redis_pool(
    request: Request,
) -> AsyncGenerator[Redis, None]:  # pragma: no cover
    """
    Returns connection pool.

    You can use it like this:

    >>> from redis.asyncio import ConnectionPool, Redis
    >>>
    >>> async def handler(redis_pool: ConnectionPool = Depends(get_redis_pool)):
    >>>     async with Redis(connection_pool=redis_pool) as redis:
    >>>         await redis.get('key')

    I use pools so you don't acquire connection till the end of the handler.

    :param request: current request.
    :returns:  redis connection pool.
    """
    return request.app.state.redis_pool



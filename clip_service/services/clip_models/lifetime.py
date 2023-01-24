from fastapi import FastAPI

from clip_service.services.clip_models.clip_service import ClipService


def init_clip_service(app: FastAPI) -> None:  # pragma: no cover
    """
    Creates connection pool for redis.

    :param app: current fastapi application.
    """
    app.state.clip_service = ClipService()


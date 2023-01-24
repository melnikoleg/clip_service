from fastapi.routing import APIRouter

from clip_service.web.api import docs, clip_endpoint, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(
    clip_endpoint.router,
    prefix="/get_clip_image_vector_from_bytes",
    tags=["get_clip_image_vector_from_bytes"],
)

import base64
from io import BytesIO

from fastapi import APIRouter, Request

from clip_service.web.api.clip_endpoint.schema import OutMessage, InputMessage
from PIL import Image

router = APIRouter()
from loguru import logger


@router.post("/", response_model=OutMessage)
async def get_clip_image_vector_from_bytes(
    incoming_message: InputMessage, request: Request
):

    meme_bytes = incoming_message.meme_bytes
    meme_url = incoming_message.object_name
    # logger.debug(f"meme_bytes: {meme_bytes}")
    logger.debug(f"type meme_bytes: {type(meme_bytes)}")

    image = Image.open(BytesIO(base64.b64decode(meme_bytes)))

    image_vector = request.app.state.clip_service.get_image_features(image)
    image_vector = next(iter(image_vector))
    image_vector = image_vector.tolist() if image_vector.any() else []
    logger.debug(f"image_vector: {image_vector} meme_url {meme_url}")

    return {"image_vector": image_vector, "object_name": meme_url}

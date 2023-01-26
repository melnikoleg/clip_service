from io import BytesIO

from fastapi import APIRouter, Request, UploadFile, File, Form

from clip_service.web.api.clip_endpoint.schema import OutMessage
from PIL import Image

router = APIRouter()


@router.post("/", response_model=OutMessage)
async def get_clip_image_vector_from_bytes(
    request: Request,
    object_name: str = Form(...),
    meme_bytes: UploadFile = File(...),
):

    meme_bytes = meme_bytes.file.read()
    image = Image.open(BytesIO(meme_bytes))
    image_vector = request.app.state.clip_service.get_image_features(image)
    image_vector = next(iter(image_vector))
    image_vector = image_vector.tolist() if image_vector.any() else []

    return {"image_vector": image_vector, "object_name": object_name}

from typing import List, Any

from pydantic import BaseModel


class InputMessage(BaseModel):
    """Simple message model."""

    meme_file: Any
    object_name: Any


class OutMessage(BaseModel):
    """Simple message model."""

    image_vector: Any

    object_name: str

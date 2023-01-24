import os

import numpy as np

from clip_service.services.clip_onnx import ClipOnnx
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from PIL import Image

from clip_service.settings import settings

try:
    from torchvision.transforms import InterpolationMode

    BICUBIC = InterpolationMode.BICUBIC
except ImportError:
    BICUBIC = Image.BICUBIC


class ClipService:
    def __init__(self):
        self.visual_path = settings.MODEL_PATH
        self.textual_path = None
        self.onnx_model = ClipOnnx(None)
        self.onnx_model.textual_flag = False
        self.onnx_model.load_onnx(
            visual_path=self.visual_path,
            textual_path=self.textual_path,
            logit_scale=100.0000,
        )  # model.logit_scale.exp()
        self.onnx_model.start_sessions(providers=["CPUExecutionProvider"])

    def get_image_features(self, image: Image):

        image = self._transform()(image).unsqueeze(0).cpu()
        image_onnx = image.detach().cpu().numpy().astype(np.float32)
        return self.onnx_model.encode_image(image=image_onnx)

    @staticmethod
    def _convert_image_to_rgb(image):
        return image.convert("RGB")

    def _transform(self, n_px: int = 384):
        return Compose(
            [
                Resize(n_px, interpolation=BICUBIC),
                CenterCrop(n_px),
                self._convert_image_to_rgb,
                ToTensor(),
                Normalize(
                    (0.48145466, 0.4578275, 0.40821073),
                    (0.26862954, 0.26130258, 0.27577711),
                ),
            ]
        )

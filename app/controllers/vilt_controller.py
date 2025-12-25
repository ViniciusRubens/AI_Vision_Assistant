from fastapi import UploadFile
from PIL import Image
import io
from app.services.vilt_service import vilt_service

class Controller:
    @staticmethod
    async def process_image_query(text: str, file: UploadFile):
        
        image_contents = await file.read()
        image = Image.open(io.BytesIO(image_contents)).convert("RGB")
        
        # Calls service
        result = vilt_service.predict(text, image)
        return result
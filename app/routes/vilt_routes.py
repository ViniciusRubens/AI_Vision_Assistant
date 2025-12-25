from fastapi import APIRouter, UploadFile, File, Form
from app.controllers.vilt_controller import Controller
from app.schemas.vilt_schema import Response

router = APIRouter(prefix = "/api", tags = ["ViLT API"])

@router.post("/predict", response_model = Response)
async def predict_description(text: str = Form(...), image: UploadFile = File(...)):
    answer = await Controller.process_image_query(text, image)
    return Response(response = answer)
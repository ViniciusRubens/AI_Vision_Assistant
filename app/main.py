from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import vilt_routes

app = FastAPI(title = "Vision-and-Language Transformer (ViLT) API")

# https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

# Middlewares CORS
# Allows the browser to access the API without security blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Routes
app.include_router(vilt_routes.router)

# Frontend
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")
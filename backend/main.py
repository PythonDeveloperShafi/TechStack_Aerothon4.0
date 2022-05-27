from fastapi import FastAPI, status
from src.schemas import title
from src.config import aerothon_config
from fastapi.middleware.cors import CORSMiddleware
from src.creates3url import create_presigned_url

app = FastAPI(title=aerothon_config.PROJECT_NAME, version=aerothon_config.PROJECT_VERSION)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/files", status_code=status.HTTP_200_OK)
async def files(request:title):
    bucket_name = "aerothon4.0"
    object_name = f"{request.feTitle.lower()}-{request.beTitle.lower()}.zip"
    return create_presigned_url(bucket_name, object_name)
        

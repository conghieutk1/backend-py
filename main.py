from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Depends, APIRouter, File, UploadFile, HTTPException
import uvicorn
from service import predict
from utils import save_fastapi_request_file, delete_file
app = FastAPI()

@app.get("/")
def get():
    return {"message": "App is running"}

router = APIRouter(
    prefix="/classify",
    tags=["classify"]
)
@router.post("/predict")

async def create_upload_file(file: UploadFile = File(...)):
    contents = save_fastapi_request_file(file)
    try:
        result = predict(contents)
        return JSONResponse({'message': 'success', 'data': result})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        delete_file(contents)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
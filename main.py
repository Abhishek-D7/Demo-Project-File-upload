import shutil
from fastapi import FastAPI, UploadFile
app = FastAPI()

@app.post("/upload")
async def upload_file(uploaded_file: UploadFile):
    print(uploaded_file.file)
    print(uploaded_file.filename)
    print(uploaded_file.content_type)
    with open(uploaded_file.filename, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return {"filename": uploaded_file.filename, "message": "Saved with stream method"}


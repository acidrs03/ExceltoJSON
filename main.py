from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.filename.endswith(".xlsx"):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        json_path = convert_to_json(file_path)
        return FileResponse(json_path, media_type='application/json', filename=os.path.basename(json_path))
    return {"error": "File format not supported"}

def convert_to_json(file_path):
    # Load the Excel data
    data = pd.read_excel(file_path)

    # Convert to JSON format
    data_json = data.to_json(orient='records')

    # Save JSON to a file
    json_filename = os.path.splitext(file_path)[0] + '.json'
    with open(json_filename, 'w') as f:
        f.write(data_json)
    
    return json_filename

@app.post("/clear")
async def clear_files():
    try:
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        return JSONResponse(content={"status": "All files cleared"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5101)

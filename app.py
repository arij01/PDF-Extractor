from fastapi import FastAPI, File, UploadFile
import pdfplumber
import language_tool_python
import os

import uvicorn

# Initializing FastAPI and language tool
app = FastAPI()
tool = language_tool_python.LanguageTool('en-US')

# Directory for uploaded files
UPLOAD_DIR = "C:/Users/21626/Downloads/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text: {e}"

# Function to correct spelling/grammars
def correct_text(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# Upload Endpoint
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

   
    extracted_text = extract_text_from_pdf(file_path)

    
    corrected_text = correct_text(extracted_text)

    return {
        "extracted_text": extracted_text,
        "corrected_text": corrected_text
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
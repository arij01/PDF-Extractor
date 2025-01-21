from fastapi import FastAPI, File, UploadFile
import pdfplumber
import language_tool_python
import io
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Initializing FastAPI and language tool
app = FastAPI()
tool = language_tool_python.LanguageTool('en-US')

# Function to extract text from PDF
def extract_text_from_pdf(file_bytes):
    try:
        with io.BytesIO(file_bytes) as pdf_file:
            with pdfplumber.open(pdf_file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""  
        return text
    except Exception as e:
        return f"Error extracting text: {e}"

# Function to correct spelling/grammars
def correct_text(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Upload Endpoint
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    
    # file_path = f"{UPLOAD_DIR}/{file.filename}"
    # with open(file_path, "wb") as f:
    #     f.write(await file.read())
    content = await file.read()

   
    extracted_text = extract_text_from_pdf(content)

    
    corrected_text = correct_text(extracted_text)

    return {
        # "extracted_text": extracted_text,
        "corrected_text": corrected_text
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
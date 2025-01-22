from fastapi import FastAPI, File, UploadFile
import pdfplumber
import language_tool_python
import io
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from langdetect import detect

# Initializing FastAPI and language tool
app = FastAPI()
tool_en = language_tool_python.LanguageTool('en-US')
tool_fr = language_tool_python.LanguageTool('fr')

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

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
    try:
        language = detect(text)
        if language == 'fr':
            corrected_text = tool_fr.correct(text)
        else:
            corrected_text = tool_en.correct(text)
        return corrected_text
    except Exception as e:
        print(f"Error correcting text: {e}")
        return text


# Upload Endpoint
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    
    content = await file.read()

   
    extracted_text = extract_text_from_pdf(content)

    
    corrected_text = correct_text(extracted_text)

    return {
        # "extracted_text": extracted_text,
        "corrected_text": corrected_text
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
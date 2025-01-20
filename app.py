from fastapi import FastAPI, File, UploadFile
import pdfplumber
import language_tool_python
import os

# Initialize FastAPI app and language tool
app = FastAPI()
tool = language_tool_python.LanguageTool('en-US')

# Directory for uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Correct the extracted text
    corrected_text = correct_text(extracted_text)

    return {
        "extracted_text": extracted_text,
        "corrected_text": corrected_text
    }


def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using pdfplumber."""
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text: {e}"


def correct_text(text):
    """Correct spelling/grammar using language_tool_python."""
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

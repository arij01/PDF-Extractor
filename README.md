# PDF-Extractor
PDF-Extractor is a web application that allows users to upload PDF files, extract text from them, and correct the text using language tools. The frontend is built with React, and the backend is built with FastAPI.

## Project Structure

```
pdf-extractor/
├── app.py
├── frontend/
│   ├── .gitignore
│   ├── package.json
│   ├── public/
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── README.md
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── reportWebVitals.js
│   │   └── setupTests.js
│   └── .gitignore
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x
- FastAPI
- pdfplumber
- language_tool_python
- uvicorn
- langdetect

### Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/pdf-extractor.git
cd pdf-extractor
```
2. Install requirements:

```sh
pip install fastapi pdfplumber language_tool_python uvicorn langdetect
```
## Running the Application

1. Start the backend server:

```sh
uvicorn app:app --reload
```
2. Start the frontend development server:

```sh
cd frontend
npm start
```
3. Open your browser and navigate to http://localhost:3000 to view the application.

## Usage

### Uploading a PDF

1. Drag and drop a PDF file into the designated area or click to select a file.
2. Click the "Submit" button to upload the file.
3. Wait for the text extraction and correction process to complete.
4. The corrected text will be displayed on the screen.

### Correcting Text

The application uses `language_tool_python` to correct the text extracted from the PDF. It supports both English and French languages. The language is automatically detected using `langdetect`.
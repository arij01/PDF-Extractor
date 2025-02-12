# PDF-Extractor
![Screenshot 2025-01-22 133005](https://github.com/user-attachments/assets/49f08561-500f-4997-b925-47f264565f6a)

## About

PDF-Extractor is a web application that allows users to upload PDF files, extract text from them, and correct the text using language tools. The frontend is built with React, and the backend is built with FastAPI. This application supports both English and French languages.

## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.12.3
- FastAPI
- pdfplumber
- language_tool_python
- uvicorn
- langdetect

### Installation

1. Clone the repository:

  ```sh
  git clone https://github.com/arij01/PDF-Extractor.git
  cd PDF-Extractor
  ```
2. Install requirements:

  ```sh
  pip install -r requirements.txt
  ```
## Running the Application

1. Start the backend server:

  ```sh
  uvicorn app:app --reload
  ```
2. Install the required npm packages:
  ```sh
  npm install
  ```
3. Start the frontend development server:

  ```sh
  cd frontend
  npm start
  ```
3. Open your browser and navigate to http://localhost:3000 to view the application.

## Usage

A sample PDF file is provided in the `sample` directory. You can use this file to test the application.

### Uploading a PDF

1. Open the application in your browser.
2. Drag and drop a PDF file into the designated area or click to select a file.
3. Click the "Submit" button to upload the file.
4. Wait for the text extraction and correction process to complete.
5. The corrected text will be displayed on the screen.

### Correcting Text

The application uses `language_tool_python` to correct the text extracted from the PDF. The language is automatically detected using `langdetect`.

import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import ClipLoader from "react-spinners/ClipLoader";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [correctedText, setCorrectedText] = useState("");
  const [loading, setLoading] = useState(false);

  // Handle file selection
  const handleFileChange = (acceptedFiles) => {
    setFile(acceptedFiles[0]);
  };

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      alert("Please select a file to upload.");
      return;
    }

    setLoading(true); 
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("File upload failed.");
      }

      const data = await response.json();
      setCorrectedText(data.corrected_text); 
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while uploading the file.");
    } finally {
      setLoading(false); 
    }
  };

  const { getRootProps, getInputProps } = useDropzone({
    accept: ".pdf",
    onDrop: handleFileChange,
  });

  return (
    <div className="container">
      <h1>PDF Extractor</h1>

      <form onSubmit={handleSubmit} className="form">
        <div {...getRootProps()} className="dropzone">
          <input {...getInputProps()} />
          <p>Drag & drop a PDF file here, or click to select one</p>
        </div>
        {file && <p className="file-name">Selected file: {file.name}</p>}
        <button type="submit" className="submit-button" disabled={loading}>
          Submit
        </button>
      </form>

      {loading && (
        <div className="loading">
          <ClipLoader color="blue" loading={loading} size={50} />
          <span>Processing your PDF... Please wait.</span>
        </div>
      )}

      {correctedText && (
        <div className="result">
          <h2>Extracted and Corrected Text</h2>
          <textarea value={correctedText} readOnly rows="10" className="result-textarea" />
        </div>
      )}
    </div>
  );
}

export default App;
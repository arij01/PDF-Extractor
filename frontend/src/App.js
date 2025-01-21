import React, { useState } from "react";
import ClipLoader from "react-spinners/ClipLoader"; // Import spinner

function App() {
  const [file, setFile] = useState(null);
  const [correctedText, setCorrectedText] = useState("");
  const [loading, setLoading] = useState(false); // Track loading state

  // Handle file selection
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      alert("Please select a file to upload.");
      return;
    }

    setLoading(true); // Start loading
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
      setCorrectedText(data.corrected_text); // Set the corrected text
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while uploading the file.");
    } finally {
      setLoading(false); // Stop loading
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>PDF Text Correction</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <label>
          Upload your PDF:
          <input
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            style={{ margin: "10px 0" }}
          />
        </label>
        <br />
        <button
          type="submit"
          style={{ padding: "10px 20px", cursor: "pointer" }}
          disabled={loading} // Disable button when loading
        >
          Submit
        </button>
      </form>

      {loading && (
        <div style={{ marginBottom: "20px", display: "flex", alignItems: "center" }}>
          <ClipLoader color="blue" loading={loading} size={50} />
          <span style={{ marginLeft: "10px", color: "blue" }}>Processing your PDF... Please wait.</span>
        </div>
      )}

      {correctedText && (
        <div>
          <h2>Corrected Text:</h2>
          <textarea
            value={correctedText}
            readOnly
            rows="10"
            cols="50"
            style={{ width: "100%", padding: "10px" }}
          />
        </div>
      )}
    </div>
  );
}

export default App;

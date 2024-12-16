import React, { useState } from "react";
import "./App.css"; // Ensure to include the updated CSS file

function App() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const checkNumber = () => {
    if (!number) {
      setResult("Please enter a number.");
      return;
    }

    setLoading(true);

    fetch("http://localhost:5000/check_number", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ num: parseInt(number) }),
    })
      .then((response) => response.json())
      .then((data) => {
        const resultText = `Is Prime: ${
          data.is_prime ? "Yes" : "No"
        }, Already Used: ${data.has_been_used ? "Yes" : "No"}`;
        setResult(resultText);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error:", error);
        setResult("Error occurred while checking the number.");
        setLoading(false);
      });
  };

  return (
    <div className="App">
      <div className="App-container">
        <h1 className="App-header">Prime Number Checker</h1>
        <div className="App-input-container">
          <input
            type="number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            placeholder="Enter a number"
            className="App-input"
          />
          <button onClick={checkNumber} disabled={loading} className="App-button">
            {loading ? "Checking..." : "Check Number"}
          </button>
        </div>
        <p className="App-result">{result}</p>
      </div>
    </div>
  );
}

export default App;

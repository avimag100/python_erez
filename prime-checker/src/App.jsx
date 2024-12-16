import React, { useState } from "react";

function App() {
  // שמירה על הערך שהוזן בשדה
  const [number, setNumber] = useState("");
  const [result, setResult] = useState("");

  // פונקציה לבדיקת אם המספר ראשוני והאם הוא כבר נבדק
  const checkNumber = () => {
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
      })
      .catch((error) => {
        console.error("Error:", error);
        setResult("Error occurred while checking the number.");
      });
  };

  return (
    <div>
      <h1>Prime Number Checker</h1>
      <input
        type="number"
        value={number}
        onChange={(e) => setNumber(e.target.value)} // עדכון ערך השדה
        placeholder="Enter a number"
      />
      <button onClick={checkNumber}>Check Number</button>
      <p>{result}</p>
    </div>
  );
}

export default App;

function checkNumber() {
  const num = document.getElementById("numberInput").value;
  fetch("http://localhost:5000/check_number", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ num: parseInt(num) }),
  })
    .then((response) => response.json())
    .then((data) => {
      const resultText = `Is Prime: ${
        data.is_prime ? "Yes" : "No"
      }, Already Used: ${data.has_been_used ? "Yes" : "No"}`;
      document.getElementById("result").innerText = resultText;
    });
}

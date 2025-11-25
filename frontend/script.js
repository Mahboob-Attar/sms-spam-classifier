async function checkSpam() {
  const msg = document.getElementById("msg").value.trim();
  const box = document.getElementById("output");
  const btn = document.querySelector("button");

  if (!msg) {
    alert("Please enter a message!");
    return;
  }

  // Show loading state
  box.style.background = "#228be6"; 
  box.style.color = "white";
  box.innerText = "⏳ Checking...";
  btn.disabled = true;
  btn.innerText = "Checking...";

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg }),
    });

    if (!res.ok) {
      throw new Error("Server error: " + res.status);
    }

    const data = await res.json();

    if (data.prediction === "Spam") {
      box.style.background = "#e03131"; 
      box.innerText = "🚨 SPAM MESSAGE!";
    } else {
      box.style.background = "#2f9e44"; 
      box.innerText = "✅ NOT SPAM";
    }

  } catch (err) {
    console.error(err);
    box.style.background = "#fa5252"; 
    box.innerText = "❌ Error connecting to server!";
  }

  // Reset button
  btn.disabled = false;
  btn.innerText = "Check";
}

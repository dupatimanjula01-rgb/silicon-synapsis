function updateFields() {
  const count = document.getElementById("count").value;
  const container = document.getElementById("participants");
  container.innerHTML = "";

  for (let i = 1; i <= count; i++) {
    container.innerHTML += `
      <h4>Participant ${i}</h4>
      <input placeholder="Name" id="name${i}" /><br>
      <input placeholder="Roll No" id="roll${i}" /><br>
      <input placeholder="Phone" id="phone${i}" /><br><br>
    `;
  }
}

updateFields();

async function submitForm() {
  const count = document.getElementById("count").value;

  const data = {
    competition: competitionId,
    number_of_participants: count,
  };

  for (let i = 1; i <= count; i++) {
    data[`participant_${i}_name`] = document.getElementById(`name${i}`).value;
    data[`participant_${i}_roll`] = document.getElementById(`roll${i}`).value;
    data[`participant_${i}_phone`] = document.getElementById(`phone${i}`).value;
  }

  const res = await fetch("http://127.0.0.1:8000/api/registrations/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (res.ok) {
    alert("Registered successfully!");
  } else {
    alert("Error submitting registration");
  }
}

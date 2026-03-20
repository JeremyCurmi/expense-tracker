const loadBtn = document.getElementById("load");
const tokenInput = document.getElementById("token");
const totalEl = document.getElementById("total");
const countEl = document.getElementById("count");
const rowsEl = document.getElementById("rows");

const loadExpenses = async () => {
  const token = tokenInput.value.trim();
  if (!token) {
    alert("Paste a JWT token first.");
    return;
  }

  const res = await fetch("/expenses", {
    headers: { Authorization: `Bearer ${token}` },
  });

  if (!res.ok) {
    alert("Failed to load expenses. Check token.");
    return;
  }

  const data = await res.json();
  const total = data.reduce((sum, item) => sum + Number(item.amount), 0);

  totalEl.textContent = `€${total.toFixed(2)}`;
  countEl.textContent = `${data.length}`;

  rowsEl.innerHTML = "";
  data.slice(0, 10).forEach((item) => {
    const row = document.createElement("div");
    row.className = "row";
    row.innerHTML = `
      <span class="muted">${new Date(item.date).toLocaleDateString()}</span>
      <span>${item.description || item.category}</span>
      <span>€${Number(item.amount).toFixed(2)}</span>
    `;
    rowsEl.appendChild(row);
  });
};

loadBtn.addEventListener("click", loadExpenses);

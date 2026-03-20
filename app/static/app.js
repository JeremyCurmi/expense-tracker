const loadBtn = document.getElementById("load");
const tokenInput = document.getElementById("token");
const totalEl = document.getElementById("total");
const countEl = document.getElementById("count");
const netEl = document.getElementById("net");
const cashflowEl = document.getElementById("cashflow");
const rowsEl = document.getElementById("rows");
const categoriesEl = document.getElementById("categories");

const formatMoney = (value) => `€${value.toFixed(2)}`;

const buildCategoryBars = (items) => {
  const totals = new Map();
  items.forEach((item) => {
    const key = item.category || "uncategorized";
    totals.set(key, (totals.get(key) || 0) + Number(item.amount));
  });

  const sorted = Array.from(totals.entries()).sort((a, b) => b[1] - a[1]).slice(0, 4);
  const max = sorted[0] ? sorted[0][1] : 0;

  categoriesEl.innerHTML = "";
  sorted.forEach(([category, total]) => {
    const row = document.createElement("div");
    row.className = "bar";
    row.innerHTML = `
      <span>${category}</span>
      <div class="rail"><div class="fill" style="width:${max ? (total / max) * 100 : 0}%"></div></div>
      <em>${formatMoney(total)}</em>
    `;
    categoriesEl.appendChild(row);
  });
};

const buildRows = (items) => {
  rowsEl.innerHTML = "";
  items.slice(0, 10).forEach((item) => {
    const row = document.createElement("div");
    row.className = "row";
    row.innerHTML = `
      <span class="muted">${new Date(item.date).toLocaleDateString()}</span>
      <span>${item.description || item.category}</span>
      <span>${formatMoney(Number(item.amount))}</span>
    `;
    rowsEl.appendChild(row);
  });
};

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

  totalEl.textContent = formatMoney(total);
  countEl.textContent = `${data.length}`;
  netEl.textContent = formatMoney(total * -1);
  cashflowEl.textContent = formatMoney(total);

  buildCategoryBars(data);
  buildRows(data);
};

loadBtn.addEventListener("click", loadExpenses);

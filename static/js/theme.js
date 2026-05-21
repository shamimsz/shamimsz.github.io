const toggle = document.querySelector("[data-theme-toggle]");
const label = document.querySelector("[data-theme-label]");

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem("theme", theme);
  if (label) {
    label.textContent = theme === "dark" ? "Light" : "Dark";
  }
}

if (toggle) {
  setTheme(document.documentElement.dataset.theme || "light");
  toggle.addEventListener("click", () => {
    const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    setTheme(nextTheme);
  });
}

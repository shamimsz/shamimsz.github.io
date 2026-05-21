const toggle = document.querySelector("[data-theme-toggle]");

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem("theme", theme);
  toggle?.setAttribute("aria-label", theme === "dark" ? "Switch to light theme" : "Switch to dark theme");
}

if (toggle) {
  setTheme(document.documentElement.dataset.theme || "light");
  toggle.addEventListener("click", () => {
    const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    setTheme(nextTheme);
  });
}

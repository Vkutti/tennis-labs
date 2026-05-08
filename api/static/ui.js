document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const pageLoader = document.getElementById("page-loader");
  body.classList.add("transition-enabled");
  requestAnimationFrame(() => {
    body.classList.add("is-ready");
  });

  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    form.addEventListener("submit", () => {
      const submitButton = form.querySelector('button[type="submit"]');
      if (submitButton) {
        submitButton.disabled = true;
        submitButton.classList.add("is-loading");

        const buttonLabel = submitButton.querySelector(".button-label");
        if (buttonLabel) {
          buttonLabel.textContent = "Running Simulation...";
        }
      }

      if (pageLoader) {
        pageLoader.classList.add("visible");
        pageLoader.setAttribute("aria-hidden", "false");
      }

      body.classList.add("is-leaving");
    });
  });
});

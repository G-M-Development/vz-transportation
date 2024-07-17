export default (() => {
  const URL_API = "https://api.3rdparty.com";
  const form = document.getElementById("contact-us-form");
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    let isValid = true;

    const nameInput = document.getElementById("name");
    if (nameInput.value.trim() === "") {
      nameInput.classList.add("error");
      isValid = false;
    } else {
      nameInput.classList.remove("error");
    }

    const emailInput = document.getElementById("email");
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value)) {
      emailInput.classList.add("error");
      isValid = false;
    } else {
      emailInput.classList.remove("error");
    }

    const commentInput = document.getElementById("comment");
    if (commentInput.value.trim() === "") {
      commentInput.classList.add("error");
      isValid = false;
    } else {
      commentInput.classList.remove("error");
    }

    if (isValid) {
      const formData = new FormData();
      formData.append("name", nameInput.value.trim());
      formData.append("email", emailInput.value.trim());
      formData.append("comment", commentInput.value.trim());
      formData.append("subject", "Brokerage Application");

      console.log(formData);
      form.reset();
    }

    fetch(`${URL_API}/send-email`, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        console.log("Success:", data);
        alert("Form submitted successfully");

        form.reset();

        const formInputs = form.querySelectorAll("input, textarea");
        formInputs.forEach((input) => {
          input.classList.remove("error");
        });
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Form submission failed");
      });
  });
})();

export default (() => {
  const URL_API = "https://api.3rdparty.com";
  const form = document.getElementById("form-mechanic");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    let isValid = true;

    const lastNameInput = document.getElementById("lastName");
    const firstNameInput = document.getElementById("firstName");
    const phoneInput = document.getElementById("phone");
    const datepickerInput = document.getElementById("datepicker");
    const commentInput = document.getElementById("comment");

    if (lastNameInput.value.trim() === "") {
      lastNameInput.classList.add("error");
      isValid = false;
    } else {
      lastNameInput.classList.remove("error");
    }

    if (firstNameInput.value.trim() === "") {
      firstNameInput.classList.add("error");
      isValid = false;
    } else {
      firstNameInput.classList.remove("error");
    }

    const telPattern =
      /\b(?:(?:\+1[-.\s]?)|(?:1[-.\s]?))?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/;
    if (!telPattern.test(phoneInput.value)) {
      phoneInput.classList.add("error");
      isValid = false;
    } else {
      phoneInput.classList.remove("error");
    }

    if (datepickerInput.value.trim() === "") {
      datepickerInput.classList.add("error");
      isValid = false;
    } else {
      datepickerInput.classList.remove("error");
    }

    if (commentInput.value.trim() === "") {
      commentInput.classList.add("error");
      isValid = false;
    } else {
      commentInput.classList.remove("error");
    }

    if (isValid) {
      const formData = new FormData();

      formData.append("LastName", lastNameInput.value.trim());
      formData.append("FirstName", firstNameInput.value.trim());
      formData.append("phone", phoneInput.value.trim());
      formData.append("dateOfBirth", datepickerInput.value.trim());
      formData.append("comment", commentInput.value.trim());
      formData.append("subject", "APPLICATION FOR MECHANIC");

      fetch(`${URL_API}/send-email`, {
        method: "POST",
        body: formData,
      })
        .then((response) => response.text())
        .then((data) => {
          alert("Form submitted successfully");

          form.reset();

          const formInputs = form.querySelectorAll("input, textarea");
          formInputs.forEach((input) => {
            input.classList.remove("error");
          });
        })
        .catch((error) => {
          alert("Form submission failed");
        });
    }
  });
})();

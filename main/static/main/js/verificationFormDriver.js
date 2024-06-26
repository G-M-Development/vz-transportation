import { URL_API } from "./config";

export default (() => {
  const form = document.getElementById("form-drivers");
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    let isValid = true;

    const lastNameInput = document.getElementById("lastName");

    if (lastNameInput.value.trim() === "") {
      lastNameInput.classList.add("error");
      isValid = false;
    } else {
      lastNameInput.classList.remove("error");
    }

    const firstNameInput = document.getElementById("firstName");
    if (firstNameInput.value.trim() === "") {
      firstNameInput.classList.add("error");
      isValid = false;
    } else {
      firstNameInput.classList.remove("error");
    }

    const phoneInput = document.getElementById("tel");

    const telPattern = /\b(?:(?:\+1[-.\s]?)|(?:1[-.\s]?))?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/;
    if (!telPattern.test(phoneInput.value)) {
      phoneInput.classList.add("error");
      isValid = false;
    } else {
      phoneInput.classList.remove("error");
    }

    const datepickerInput = document.getElementById("datepicker");
    if (datepickerInput.value.trim() === "") {
      datepickerInput.classList.add("error");
      isValid = false;
    } else {
      datepickerInput.classList.remove("error");
    }

    const experienceInput = document.getElementById("experience");
    if (experienceInput.value.trim() === "") {
      experienceInput.classList.add("error");
      isValid = false;
    } else {
      experienceInput.classList.remove("error");
    }

    const ssnInput = document.getElementById("ssn");
    if (ssnInput.files.length === 0) {
      alert("Please upload SSN photo");
      isValid = false;
    }

    const cdlInput = document.getElementById("cdl");
    if (cdlInput.files.length === 0) {
      alert("Please upload CDL photo");
      isValid = false;
    }

    const medicalInput = document.getElementById("medical");
    if (medicalInput.files.length === 0) {
      alert("Please upload Medical photo");
      isValid = false;
    }

    if (isValid) {
      const formData = new FormData();
      formData.append("LastName", lastNameInput.value.trim());
      formData.append("FirstName", firstNameInput.value.trim());
      formData.append("phone", phoneInput.value.trim());
      formData.append("dateOfBirth", datepickerInput.value.trim());
      formData.append("experience", experienceInput.value.trim());
      formData.append("images", ssnInput.files[0]);
      formData.append("images", cdlInput.files[0]);
      formData.append("images", medicalInput.files[0]);
      formData.append("subject", "APPLICATION FOR DRIVERS");

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
    }
  });
})();

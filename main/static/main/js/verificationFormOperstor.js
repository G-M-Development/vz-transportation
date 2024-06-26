import { URL_API } from "./config";
export default (() => {
  const form = document.getElementById("form-operator");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    let isValid = true;

    const FirstNameInput = document.getElementById("FirstName");
    if (FirstNameInput.value.trim() === "") {
      FirstNameInput.classList.add("error");
      isValid = false;
    } else {
      FirstNameInput.classList.remove("error");
    }

    const LastNameInput = document.getElementById("LastName");
    if (LastNameInput.value.trim() === "") {
      LastNameInput.classList.add("error");
      isValid = false;
    } else {
      LastNameInput.classList.remove("error");
    }

    const phoneInput = document.getElementById("phone");
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

    const truckInput = document.getElementById("truck");
    if (truckInput.value.trim() === "") {
      truckInput.classList.add("error");
      isValid = false;
    } else {
      truckInput.classList.remove("error");
    }

    const experienceInput = document.getElementById("experience");
    if (experienceInput.value.trim() === "") {
      experienceInput.classList.add("error");
      isValid = false;
    } else {
      experienceInput.classList.remove("error");
    }

    const checkedElement = document.querySelector('input[name="truck"]:checked');
    const allTruckInputs = document.querySelectorAll('input[type="radio"]');
    if (!checkedElement) {
      isValid = false;
      allTruckInputs.forEach((input) => {
        input.classList.add("error");
      });
    } else {
      allTruckInputs.forEach((input) => {
        input.classList.remove("error");
      });
    }

    const ssnInput = document.getElementById("ssn");
    const cdlInput = document.getElementById("cdl");
    const medicalInput = document.getElementById("medical");

    if (ssnInput.files.length === 0) {
      ssnInput.classList.add("error");
      isValid = false;
    } else {
      ssnInput.classList.remove("error");
    }

    if (cdlInput.files.length === 0) {
      cdlInput.classList.add("error");
      isValid = false;
    } else {
      cdlInput.classList.remove("error");
    }

    if (medicalInput.files.length === 0) {
      medicalInput.classList.add("error");
      isValid = false;
    } else {
      medicalInput.classList.remove("error");
    }

    if (isValid) {
      const formData = new FormData();
      formData.append("FirstName", FirstNameInput.value.trim());
      formData.append("LastName", LastNameInput.value.trim());
      formData.append("phone", phoneInput.value.trim());
      formData.append("dateOfBirth", datepickerInput.value.trim());
      formData.append("truck", truckInput.value.trim());
      formData.append("experience", experienceInput.value.trim());
      formData.append("preferredTruck", checkedElement.value);
      formData.append("images", ssnInput.files[0]);
      formData.append("images", cdlInput.files[0]);
      formData.append("images", medicalInput.files[0]);
      formData.append("subject", "APPLICATION FOR OWNER OPERATOR");

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

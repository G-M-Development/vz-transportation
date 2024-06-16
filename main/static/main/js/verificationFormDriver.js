export default (() => {
  const form = document.getElementById('form-drivers');
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    let isValid = true;

    const lastNameInput = document.getElementById('lastName');

    if (lastNameInput.value.trim() === '') {
      lastNameInput.classList.add('error');
      isValid = false;
    } else {
      lastNameInput.classList.remove('error');
    }

    const firstNameInput = document.getElementById('firstName');
    if (firstNameInput.value.trim() === '') {
      firstNameInput.classList.add('error');
      isValid = false;
    } else {
      firstNameInput.classList.remove('error');
    }

    const phoneInput = document.getElementById('tel');

    const telPattern =
      /\b(?:(?:\+1[-.\s]?)|(?:1[-.\s]?))?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/;
    if (!telPattern.test(phoneInput.value)) {
      phoneInput.classList.add('error');
      isValid = false;
    } else {
      phoneInput.classList.remove('error');
    }

    const datepickerInput = document.getElementById('datepicker');
    if (datepickerInput.value.trim() === '') {
      datepickerInput.classList.add('error');
      isValid = false;
    } else {
      datepickerInput.classList.remove('error');
    }

    const experienceInput = document.getElementById('experience');
    if (experienceInput.value.trim() === '') {
      experienceInput.classList.add('error');
      isValid = false;
    } else {
      experienceInput.classList.remove('error');
    }

    if (isValid) {
      const formData = {
        lastNameInput: lastNameInput.value.trim(),
        firstNameInput: firstNameInput.value.trim(),
        phoneInput: phoneInput.value.trim(),
        datepickerInput: datepickerInput.value.trim(),
        experienceInput: experienceInput.value.trim(),
      };
      console.log(formData);
      form.reset();
    }
  });
})();

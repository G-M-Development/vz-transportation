export default (() => {
  const form = document.getElementById('form-mechanic');

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

    const phoneInput = document.getElementById('phone');

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

    const commentInput = document.getElementById('comment');
    if (commentInput.value.trim() === '') {
      commentInput.classList.add('error');
      isValid = false;
    } else {
      commentInput.classList.remove('error');
    }

    if (isValid) {
      const formData = {
        lastName: lastNameInput.value.trim(),
        firstName: firstNameInput.value.trim(),
        phone: phoneInput.value.trim(),
        datepicker: datepickerInput.value.trim(),
        comment: commentInput.value.trim(),
      };

      console.log(formData);
      form.reset();
    }
  });
})();

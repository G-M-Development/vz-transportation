export default (() => {
  const form = document.getElementById('form-operator');
  console.log(form)
  form.addEventListener('submit', function (event) {
    event.preventDefault();
console.log("object")
    let isValid = true;

    const FirstNameInput = document.getElementById('FirstName');
    if (FirstNameInput.value.trim() === '') {
      FirstNameInput.classList.add('error');
      isValid = false;
    } else {
      FirstNameInput.classList.remove('error');
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

    const truckInput = document.getElementById('truck');
    if (truckInput.value.trim() === '') {
      truckInput.classList.add('error');
      isValid = false;
    } else {
      truckInput.classList.remove('error');
    }

    const LastNameInput = document.getElementById('LastName');
    if (LastNameInput.value.trim() === '') {
      LastNameInput.classList.add('error');
      isValid = false;
    } else {
      LastNameInput.classList.remove('error');
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
    const checkedElement = document.querySelector(
      'input[name="truck"]:checked'
    );

    const allTruckInputs = document.querySelectorAll('input[type="radio"]');

    if (!checkedElement) {
      isValid = false;
      allTruckInputs.forEach(input => {
        input.classList.add('error');
      });
    } else {
      allTruckInputs.forEach(input => {
        input.classList.remove('error');
      });
    }

    if (isValid) {
      const formData = {
        FirstName: FirstNameInput.value.trim(),
        phoneInput: phoneInput.value.trim(),
        truckInput: truckInput.value.trim(),
        LastName: LastNameInput.value.trim(),
        datepickerInput: datepickerInput.value.trim(),
        experienceInput: experienceInput.value.trim(),
        checkedElement: checkedElement.value.trim(),
      };
      console.log(formData);
      form.reset();
    }
  });
})();

export default (() => {
    const form = document.getElementById('contact-us-form');
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      let isValid = true;
  
      const nameInput = document.getElementById('name');
      if (nameInput.value.trim() === '') {
        nameInput.classList.add('error');
        isValid = false;
      } else {
        nameInput.classList.remove('error');
      }
  
      const emailInput = document.getElementById('email');
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(emailInput.value)) {
        emailInput.classList.add('error');
        isValid = false;
      } else {
        emailInput.classList.remove('error');
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
          name: nameInput.value.trim(),
          email: emailInput.value.trim(),
          commentInput: commentInput.value.trim(),
        };
        console.log(formData);
        form.reset();
      }
    });
  })();
  
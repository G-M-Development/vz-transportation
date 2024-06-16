export const spinner = {
  startLoader: () => {
    const loader = document.querySelector('.bacdrop');
    if (loader) {
      loader.classList.remove('is-hidden');
    }
  },
  stopLoader: () => {
    const loader = document.querySelector('.bacdrop');
    if (loader) {
      loader.classList.add('is-hidden');
    }
  },
};

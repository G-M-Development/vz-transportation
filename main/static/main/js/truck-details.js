export default (() => {
  var swiper = new Swiper('.mySwiper', {
    spaceBetween: 10,
    slidesPerView: 5,
    freeMode: true,
    watchSlidesProgress: true,
  });
  var swiper2 = new Swiper('.mySwiper2', {
    spaceBetween: 10,
    navigation: {
      nextEl: '.swiper-next',
      prevEl: '.swiper-prev',
    },
    thumbs: {
      swiper: swiper,
    },
  });
})();

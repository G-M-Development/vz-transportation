const truckDataArray = [
  {
    id: 1,
    title: 'Volvo: vnl series (vnl)',
    year: 2019,
    trailerCount: 3500,
    speed: 3500,
    automatic: 3500,
    frontImpact: 3500,
    price: '$4000',
    detailsUrl: './truck-details.html',
    photoUrl: '../../../img/truck.jpg',
  },
  {
    id: 2,
    title: 'Volvo: vnl series (vnl)',
    year: 2019,
    trailerCount: 3500,
    speed: 3500,
    automatic: 3500,
    frontImpact: 3500,
    price: '$4000',
    detailsUrl: './truck-details.html',
    photoUrl: '../../../img/truck.jpg',
  },
];

const truckData = {
  title: 'AMERICAN TRUCK TRACTOR VOLVO: VNL SERIES (VNL) 780 AND 670',
  images: [
    '../../../img/truck.jpg',
    '../../../img/truck.jpg',
    '../../../img/truck.jpg',
    '../../../img/truck.jpg',
    '../../../img/truck.jpg',
    '../../../img/truck.jpg',
  ],
  details: {
    year: 2019,
    speed: 3500,
    automatic: true,
    frontImpact: 3500,
  },
  cost: 4000,
  paragraphs: [
    'The Volvo VNL 780 and 670 series of American trucks are the epitome of modern technology and reliability in the transportation industry.',
    'Thanks to their impressive design, high-quality materials and advanced technology, these trucks provide a comfortable and efficient driving experience on any US road.',
    'They are equipped with powerful engines that deliver high performance and fuel efficiency. The cabs of the Volvo VNL 780 and 670 offer drivers a spacious and comfortable interior with comfortable seats, an advanced infotainment system and wide windows for a better view of the environment.',
    'These tractors meet the highest quality and safety standards, making them the ideal choice for professional drivers who value comfort and reliability in their work.',
  ],
};

function renderTruck(data) {
  const trackWrapper = document.createElement('div');
  trackWrapper.classList.add('brokerage-track');

  trackWrapper.innerHTML = `
    <img class="brokerage-track-img" src="${data.photoUrl}" alt="truck" />
    <div class="brokerage-track-progress">
      <div class="brokerage-track-progress-wrap">
        <h3 class="brokerage-track-title">${data.title}</h3>
        <ul class="brokerage-track-list">
          <li class="brokerage-track-item">
            <svg class="brokerage-track-icon" width="38" height="42">
              <use href="../../../img/sprite.svg#icon-calendar"></use>
            </svg>
            <p class="brokerage-track-text">${data.year}</p>
          </li>
          <li class="brokerage-track-item">
            <svg class="brokerage-track-icon" width="64" height="34">
              <use href="../../../img/sprite.svg#icon-trailer"></use>
            </svg>
            <p class="brokerage-track-text">${data.trailerCount}</p>
          </li>
          <li class="brokerage-track-item">
            <svg class="brokerage-track-icon" width="52" height="43">
              <use href="../../../img/sprite.svg#icon-speed"></use>
            </svg>
            <p class="brokerage-track-text">${data.speed}</p>
          </li>
          <li class="brokerage-track-item">
            <svg class="brokerage-track-icon" width="43" height="43">
              <use href="../../../img/sprite.svg#icon-automatic"></use>
            </svg>
            <p class="brokerage-track-text">${data.automatic}</p>
          </li>
          <li class="brokerage-track-item">
            <svg class="brokerage-track-icon" width="38" height="42">
              <use href="../../../img/sprite.svg#icon-front-impact"></use>
            </svg>
            <p class="brokerage-track-text">${data.frontImpact}</p>
          </li>
        </ul>
      </div>
       <div class="brokerage-track-wrap">
        <div class="brokerage-track-progress-bar">
          <svg class="brokerage-track-icon" width="60" height="48">
            <use href="../../../img/sprite.svg#icon-money"></use>
          </svg>
          <p class="brokerage-track-progress-text">${data.price}</p>
          <svg class="brokerage-track-sub-icon" width="18" height="18">
            <use href="../../../img/sprite.svg#icon-vector-2"></use>
          </svg>
        </div>
        <button class="btn" type="button" onclick="window.location.href='${data.detailsUrl}'">Details</button>
      </div>
    </div>
  `;

  return trackWrapper;
}

document.addEventListener('DOMContentLoaded', () => {
  const trackWrapper = document.getElementById('track-wrapper');

  truckDataArray.forEach(truck => {
    trackWrapper.appendChild(renderTruck(truck));
  });
});

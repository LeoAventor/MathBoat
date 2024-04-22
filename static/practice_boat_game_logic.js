let boat = document.querySelector('.boat');

function moveBoat() {
  let currentPosition = parseInt(boat.style.left, 10) || 0;
  let boatSpeed = parseInt(document.querySelector('.correct-answer').textContent.replace(': ', ''));
  currentPosition += boatSpeed;
  boat.style.left = currentPosition + 'px';
  if (currentPosition >= window.innerWidth) {
    boat.style.left = '0px';
  }
}

setInterval(moveBoat, 100);



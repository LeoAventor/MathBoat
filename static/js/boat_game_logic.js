let boat = document.querySelector('.boat');

function moveBoat() {
  let currentPosition = parseInt(boat.style.left, 10) || 0;
  let boatSpeed = parseInt(document.querySelector('.correct-streak').textContent.replace('/.+?: /', ''));
  let currentDifficulty = parseInt(document.querySelector('.correct-difficulty').textContent.replace('/.+?: /', ''));

  currentPosition += boatSpeed*2;
  boat.style.left = currentPosition + 'px';

  if (currentPosition >= window.innerWidth) {
    boat.style.left = '0px';
  }
  if (currentDifficulty === "easy") {
    boat.style.width = 25
    boat.style.height = 25
  } else if (currentDifficulty === "medium") {
    boat.style.width = 50
    boat.style.height = 50
  }
}

setInterval(moveBoat, 100);
let boat = document.querySelector('.boat');

function moveBoat() {
  let currentPosition = parseInt(boat.style.left, 10) || 0;
  let boatSpeed = parseInt(document.querySelector('.current-streak').textContent);
  let currentDifficulty = document.querySelector('.current-difficulty').textContent;

  currentPosition += boatSpeed*2;
  boat.style.left = currentPosition + 'px';

  if (currentPosition >= window.innerWidth) {
    boat.style.left = '0px';
  }
  if (currentDifficulty === "easy") {
    boat.style.width = '100px';
    boat.style.height = '100px';
  } else if (currentDifficulty === "medium") {
    boat.style.width = '200px';
    boat.style.height = '200px';
  }
}

setInterval(moveBoat, 100);
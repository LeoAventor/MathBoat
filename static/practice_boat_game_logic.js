let correctStreak = 0;
let incorrectStreak = 0;
let boatSpeed = 5; // Initial speed of the boat
let boat = document.querySelector('.boat'); // Select the boat element

// Function to move the boat
function moveBoat() {
  let currentPosition = parseInt(boat.style.left, 10) || 0;
  currentPosition += boatSpeed;
  boat.style.left = currentPosition + 'px';
  // Check if the boat has reached the right side of the webpage
  if (currentPosition >= window.innerWidth) {
    boat.style.left = '0px'; // Reset boat position to the left side
  }
}

// Function to update the boat speed based on the current status
function updateBoatSpeed(currentStatus) {
  if (currentStatus === 'correct') {
    correctStreak++;
    incorrectStreak = 0;
    boatSpeed *= 1.5; // Increase speed by 50%
  } else if (currentStatus === 'incorrect') {
    incorrectStreak++;
    correctStreak = 0;
    boatSpeed *= 0.5; // Decrease speed by 50%
  }
}

// Add event listener to the submit button to update the boat speed based on the current status
document.querySelector('.submit-button').addEventListener('click', function() {
  let currentStatus = document.querySelector('.correct-status').textContent;
  updateBoatSpeed(currentStatus);
  moveBoat();
});

// Call the moveBoat function every 100 milliseconds to animate the boat
setInterval(moveBoat, 100);
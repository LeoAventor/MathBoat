// Boat class to create and manage boats
class SmallBoat {
    constructor(id) {
      this.id = id;
      this.element = document.createElement('div');
      this.element.classList.add('small_boat');
      this.element.setAttribute('id', `small_boat-${id}`);
      this.element.style.position = 'absolute';
      this.element.style.left = `${Math.random() * window.innerWidth}px`;
      this.element.style.top = `${Math.random() * window.innerHeight}px`;
      document.body.appendChild(this.element);
  
      // Set initial direction and speed
      this.directionX = Math.random() < 0.5 ? -1 : 1;
      this.directionY = Math.random() < 0.5 ? -1 : 1;
      this.speed = Math.random() * 3 + 1;
  
      // Add click event to remove the boat
      this.element.addEventListener('click', () => {
        this.removeSmallBoat();
        setTimeout(() => this.respawnSmallBoat(), 3000);
      });
  
      this.moveSmallBoat();
    }
  
    moveSmallBoat() {
      setInterval(() => {
        let left = parseFloat(this.element.style.left);
        let top = parseFloat(this.element.style.top);
  
        // Change direction if boat reaches the edge
        if (left <= 0 || left >= window.innerWidth - this.element.offsetWidth) {
          this.directionX *= -1;
        }
        if (top <= 0 || top >= window.innerHeight - this.element.offsetHeight) {
          this.directionY *= -1;
        }
  
        // Move the boat
        this.element.style.left = `${left + this.speed * this.directionX}px`;
        this.element.style.top = `${top + this.speed * this.directionY}px`;
      }, 100);
    }
  
    removeSmallBoat() {
      this.element.remove();
    }
  
    respawnSmallBoat() {
      new SmallBoat(this.id);
    }
  }
    
      // Create 15 boats
      for (let i = 0; i < 15; i++) {
        new SmallBoat(i);
      }
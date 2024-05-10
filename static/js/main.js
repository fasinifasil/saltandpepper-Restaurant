// main.js

// Check if there's an existing timestamp in local storage
var previousTime = localStorage.getItem('timestamp');

// If there's no previous timestamp or it's been more than 24 hours, clear localStorage
var hours = 24;
var currentTime = new Date().getTime();
if (!previousTime || (currentTime - previousTime > hours * 60 * 60 * 1000)) {
    localStorage.clear();
    localStorage.setItem('timestamp', currentTime);
}

// Initialize or retrieve orders and total from localStorage
var orders = JSON.parse(localStorage.getItem('orders')) || [];

// Function to update the cart count in the navbar
function updateCart() {
    var cartCount = orders.length;
    var cartElement = document.querySelector('#cart');
    if (cartElement) {
        cartElement.textContent = cartCount.toString();
    }
}

// Call updateCart to initialize the cart count after the DOM has fully loaded
document.addEventListener('DOMContentLoaded', function() {
    updateCart();
});

function updateCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
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
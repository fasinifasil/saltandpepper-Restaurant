// border.js

// Select cart and total elements
var bcart = document.querySelector('#bcart');
var btotal = document.querySelector('#btotal');

// Function to add a burger to the cart
function addBurger(bid) {
    var burgerId = '#Bug' + bid;
    var name = document.querySelector(burgerId).innerHTML;
    var radio = 'burger' + bid;
    var pri = document.getElementsByName(radio);
    var size, price;

    // Determine size and price based on selected radio button
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    } else {
        price = pri[1].value;
        size = 'L';
    }

    // Get orders and total from localStorage or initialize if they don't exist
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;
    var cartSize=orders.length;


    // Add burger to orders
    orders.push([name, size, price]);
    localStorage.setItem('orders', JSON.stringify(orders));

    // Update total
    total += parseFloat(price);
    localStorage.setItem('total', total);

    // Update cart UI

    bt1 =   '<h6><button class="btn-danger del ml-5" onclick="removeBurger(' + cartSize +')"> x </button><h6>';


    bcart.innerHTML += '<li>' + name + ' ' + size + ' ' + price +' ₹ '+bt1+ '</li>';
    btotal.innerHTML = 'Total: ' + total.toFixed(2) + '₹';
    updateCart();
}

// Function to display the shopping cart on page load
function displayShoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;
    var cartSize=orders.length;


    // Clear previous cart content
    bcart.innerHTML = '';

    // Loop through orders and display them in the cart
    for (var i = 0; i <cartSize; i++) {
        bt1 =   '<h6><button class="btn-danger del ml-5" onclick="removeBurger(' + i +')"> x </button></h6>';


        bcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' ' + orders[i][2] +' ₹ '+bt1+  '</li>';
    }

    // Display total
    btotal.innerHTML = 'Total: ' + total.toFixed(2) + '₹';
}

// Call displayShoppingCart to initialize the cart on page load
displayShoppingCart();
function removeBurger(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = parseFloat(localStorage.getItem('total')) ;
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    displayShoppingCart();
}

var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');
function addPizza(pid) {
    var pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;
    var radio = 'pizza' + pid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    } else {
        price = pri[1].value;
        size = 'L';
    }
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;
    var cartSize=orders.length;
    orders.push([name, size, price]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);
    bt1 =   '<h6><button class="btn-danger del ml-5" onclick="removePizza(' + cartSize +')"> x </button></h6>';

    pcart.innerHTML += '<li>' + name + ' ' + size + ' ' + price + '₹'+bt1+ '</li>';
    ptotal.innerHTML = 'Total: ' + total.toFixed(2) + '₹';
    updateCart();
}

// Function to display the shopping cart on page load
function displayShoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;
    var cartSize=orders.length;
    pcart.innerHTML = '';

    // Loop through orders and display them in the cart
    for (var i = 0; i < cartSize; i++) {
        bt1 =   '<h6><button class="btn-danger del ml-5" onclick="removePizza(' + i +')"> x </button></h6>';
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' ' + orders[i][2] +' ₹ '+bt1+ '</li>';
    }

    // Display total
    ptotal.innerHTML = 'Total: ' + total.toFixed(2) + '₹';
}

// Call displayShoppingCart to initialize the cart on page load
displayShoppingCart();
function removePizza(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = parseFloat(localStorage.getItem('total')) ;
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    displayShoppingCart();
}
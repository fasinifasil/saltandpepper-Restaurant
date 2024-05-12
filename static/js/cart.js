var nam = document.querySelector('#name');
var size = document.querySelector('#size');
var price = document.querySelector('#price');
var bill = document.querySelector('#total');
var rm = document.querySelector('#rm');

function ShoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;
    var cartSize = orders.length;
    nam.innerHTML = '<h5>Name</h5>';
    size.innerHTML = '<h5>Size</h5>';
    price.innerHTML = '<h5>Price</h5>';
    rm.innerHTML = '<h5>Remove</h5>';
    for (var i = 0; i < cartSize; i++) {
        rm.innerHTML += '<h4><button class="btn-danger" onclick="removeItem(' + i + ')"> x </button></h4>';
        nam.innerHTML += '<h4>' + orders[i][0] + '</h4>';
        size.innerHTML += '<h4>' + orders[i][1] + '</h4>';
        price.innerHTML += '<h4>' + orders[i][2] + '</h4>';
    }
    bill.innerHTML = 'Total: ' + total + '₹';
}
ShoppingCart();

function removeItem(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = parseFloat(localStorage.getItem('total'));
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    ShoppingCart();
}
var note = document.querySelector('#message');

function orderItem() {
    var msg = note.value;
<<<<<<< HEAD
    var orders=localStorage.getItem('orders');
    var total=localStorage.getItem('total');
    var ur = '/food/order';
    var orderData = {};
    orderData['orders']=orders;
    orderData['note']=msg;
    orderData['bill']=total;
=======
    var ur = '/food/order';
    var orderData = {};
    orderData['note']=msg;
>>>>>>> 111aed1a57b15be7570ca0c0d6d944ccb3d76964
    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        success: function(data) {
<<<<<<< HEAD
            window.location.replace('/food/success');
             localStorage.setItem('orders', JSON.stringify([]));
             localStorage.setItem('total', 0);

=======
            console.log("The data was sent");
>>>>>>> 111aed1a57b15be7570ca0c0d6d944ccb3d76964
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });
}


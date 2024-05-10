//var pcart   =   document.querySelector('#pcart')
//var ptotal   =   document.querySelector('#ptotal')
//
//function addPizza(pid){
//    pizzaId = '#piz'+pid;
//    var name = document.querySelector(pizzaId).innerHTML;
//    var radio = 'pizza'+pid;
//    var pri = document.getElementsByName(radio);
//    var size;
//    if (pri[0].checked){
//        price = pri[0].value;
//        size  = 'M';
//    }
//    else{
//        price = pri[1].value;
//        size  = 'L';
//
//    }
//    var orders          =   JSON.parse(localStorage.getItem('orders'));
//    var total           =   localStorage.getItem('total');
//    var cartSize        =   orders.length;
//
//    //saving item into local storage
//    orders[cartSize]    =   [name,size,price]
//    localStorage.setItem('orders',JSON.stringify(orders));
//    total = Number(total)+Number(price);
//    localStorage.setItem('total',total);
//    //updating number of item in shopping cart
//    var cart = document.querySelector('#cart');
//    cart.innerHTML =orders.length;
//    ptotal.innerHTML = 'Total : ' +total+ '$';
//    pcart.innerHTML += '<li>'+name+ ' '+size+ ' '+price+'</li>';
//}
//

// order.js
var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

function addPizza(pid) {
    var pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;
    var radio = 'pizza' + pid;
    var pri = document.getElementsByName(radio);
    var size;
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    } else {
        price = pri[1].value;
        size = 'L';
    }
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total')
    var cartSize = orders.length;

    // Saving item into local storage
    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders', JSON.stringify(orders));
    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // Updating number of items in shopping cart
    var cart = document.querySelector('#cart');
    cart.innerHTML = orders.length;
    ptotal.innerHTML = 'Total : ' + total + '₹';
    pcart.innerHTML += '<li>' + name + ' ' + size + ' ' + price + '</li>';
}


function pshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total')
    var cartSize = orders.length;
    pcart.innerHTML='';
    for(let i=o;i<cartSize;i++)
    {
    pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' ' + orders[i][2] + '</li>';

    }
    ptotal.innerHTML = 'Total : ' + total + '₹';

    }

pshoppingCart();
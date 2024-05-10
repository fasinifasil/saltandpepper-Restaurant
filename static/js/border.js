var bcart   =   document.querySelector('#bcart')
var btotal   =   document.querySelector('#btotal')

function addBurger(bid){
    burgerId = '#Bug'+bid;
    var name = document.querySelector(burgerId).innerHTML;
    var radio = 'burger'+bid;
    var pri = document.getElementsByName(radio);
    var size;
    if (pri[0].checked){
        price = pri[0].value;
        size  = 'M';
    }
    else{
        price = pri[1].value;
        size  = 'L';

    }
    var orders          =   JSON.parse(localStorage.getItem('orders'));
    var total           =   localStorage.getItem('total');
    var cartSize        =   orders.length;

    //saving item into local storage
    orders[cartSize]    =   [name,size,price]
    localStorage.setItem('orders',JSON.stringify(orders));
    total = Number(total)+Number(price);
    localStorage.setItem('total',total);
    //updating number of item in shopping cart
    var cart = document.querySelector('#cart');
    cart.innerHTML =orders.length;
    btotal.innerHTML = 'Total : ' +total+ '$';
    bcart.innerHTML += '<li>'+name+ ' '+size+ ' '+price+'</li>';
}

function bshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total')
    var cartSize = orders.length;
    pcart.innerHTML='';
    for(let i=0;i<cartSize;i++)
    {
    bcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' ' + orders[i][2] + '</li>';

    }
    btotal.innerHTML = 'Total : ' + total + '₹';

    }

bshoppingCart();
document.addEventListener('DOMContentLoaded', function () {
    updateCartButtons();
});

function updateCartButtons() {
    for (var id in cart) {
        if (cart[id].quantity > 0) {
            var button = document.getElementById('add-to-cart-' + id);
            if (button) {
                button.innerText = 'Added to Cart';
                button.disabled = true;
            }
        }
    }
}

var updateBtns = document.getElementsByClassName('update-cart');
for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action:', action);
        
        if (user == 'AnonymousUser') {
            addCookieItem(productId, action);
        } else {
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...');

    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then((data) => {
        console.log('data:', data);
        document.getElementById('cart-total').innerText = data.cartItems;
        updateCartUI(productId, action);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function addCookieItem(productId, action) {
    console.log('User is not authenticated');

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 };
        } else {
            cart[productId]['quantity'] += 1;
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1;

        if (cart[productId]['quantity'] <= 0) {
            console.log('Remove Item');
            delete cart[productId];
        }
    }
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";

    document.getElementById('cart-total').innerText = getCartItemsCount();
    updateCartUI(productId, action);
}

function getCartItemsCount() {
    var itemsCount = 0;
    for (var key in cart) {
        itemsCount += cart[key].quantity;
    }
    return itemsCount;
}

function updateCartUI(productId, action) {
    var cartRow = document.querySelector(`[data-product="${productId}"]`).closest('.cart-row');

    if (action == 'remove') {
        cartRow.remove();
    }

    if (document.querySelectorAll('.cart-row').length == 0) {
        document.querySelector('.cart-items').innerHTML = '<p>Your cart is empty.</p>';
    }
}

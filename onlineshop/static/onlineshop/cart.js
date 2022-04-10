if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

/*var updateBtns = document.getElementsByClassName("update-cart")

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var articleId = this.dataset.article
        var action = this.dataset.action
        console.log('articleId:', articleId, 'action:', action)

        console.log('User', user)
        if (user == 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            console.log('User is logged in, sending data..')
        }
    })
}

function updateUserOrder(articleId, action) {
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'articleId': articleId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
        })
}*/

function ready() {
    let addToCartButtons = document.getElementsByClassName("addbutton")
    for (let i = 0; i < addToCartButtons.length; i++) {
        let button = addToCartButtons[i]
        button.addEventListener('click', addToCartClicked)
    }
    function addToCartClicked(event) {
        let button = event.target
        let singleItem = button.parentElement
        let title = singleItem.getElementsByClassName('producttitle')[0].innerText
        let price = singleItem.getElementsByClassName('productprice')[0].innerText
        let imageSrc = singleItem.getElementsByClassName('productimage')[0].src
        console.log(title, price, imageSrc)
        addItemToCart(title, price, imageSrc)
    }

    function addItemToCart(title, price, imageSrc) {
        let cartRow = document.createElement('div')
        cartRow.innerText = title
        let cartItems = ""
        cartItems = document.getElementsByClassName('cart-items')[0]
        cartItems.append(cartRow)
    }
}
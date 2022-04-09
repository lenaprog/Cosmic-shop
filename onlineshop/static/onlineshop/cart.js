var updateBtns = document.getElementsByClassName("update-cart")

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
}

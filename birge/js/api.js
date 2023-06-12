// функция для получения товаров с сервера
function getProducts() {
    fetch('https://your-api-url/products')
        .then(response => response.json())
        .then(products => displayProducts(products));
}

// функция для отправки отзыва на сервер
function postReview(review) {
    fetch('https://your-api-url/reviews', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(review)
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
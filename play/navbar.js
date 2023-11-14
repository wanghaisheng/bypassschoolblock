document.addEventListener('DOMContentLoaded', (event) => {
    fetch('/nav.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
                alert('err')
            }
            return response.text();
        })
        .then(data => {
            document.body.insertAdjacentHTML('afterbegin', data);
        })
        .catch(error => {
            alert('err')
            console.error('There has been a problem with your fetch operation: ', error);
        });
});
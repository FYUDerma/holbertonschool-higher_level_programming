function SayHello () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const helloElement = document.getElementById('hello');
    fetch(url)
    .then(response => response.text())
    .then(data => {
        helloElement.textContent = data;
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', SayHello);
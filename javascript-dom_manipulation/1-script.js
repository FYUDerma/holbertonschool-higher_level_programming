function changeHeaderColor() {
    const element = document.querySelector('header')
    element.style.color = '#FF0000';
}

const redHeaderElement = document.getElementById('red_header');

redHeaderElement.addEventListener('click', changeHeaderColor);
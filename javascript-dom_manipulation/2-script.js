function add_class() {
    document.querySelector('header').classList.add('red');
}

const redHeaderElement = document.getElementById('red_header');

redHeaderElement.addEventListener('click', add_class);
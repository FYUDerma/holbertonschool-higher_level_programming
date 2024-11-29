function changeTheText() {
    const header = document.querySelector('header');
    header.innerHTML = 'New Header!!!';
}

const updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', changeTheText);
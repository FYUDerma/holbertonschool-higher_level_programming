function toggle_classes() {
    const header = document.querySelector('header');
    header.classList.toggle('green');
    header.classList.toggle('red');
}

const headerElement = document.getElementById('toggle_header');
headerElement.addEventListener('click', toggle_classes);
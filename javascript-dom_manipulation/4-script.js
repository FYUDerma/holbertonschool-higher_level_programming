function listOfElement () {
    const list = document.querySelector('.my_list')
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
}

const listElement = document.getElementById('add_item');

listElement.addEventListener('click', listOfElement);
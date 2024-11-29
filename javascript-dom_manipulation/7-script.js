function StarWarsMovie () {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const list = document.querySelector('#list_movies');

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const films = data.results;
        films.forEach(film => {
            const newItem = document.createElement('li');
            newItem.textContent = film.title;
            list.appendChild(newItem);
        });
    })
    .catch(error => console.log('Error while fetching: ' + error.message));
}

StarWarsMovie();
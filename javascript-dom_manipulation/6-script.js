function starWarsCharacter() {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
    const characterElement = document.getElementById('character');

    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network not responding; ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        const characterName = data.name;
        characterElement.textContent = characterName;
    })
    .catch(error => {
        console.log('Error while fetch: ' + error.message);
        characterElement.textContent = 'No character found';
    });
}

starWarsCharacter();
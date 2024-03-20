document.getElementById('find-movie-btn').addEventListener('click', function() {
    const description = document.getElementById('movie-description').value;
    if (description) {
        fetch('http://127.0.0.1:5050/get_movie', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({description: description})
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('movie-result').innerHTML = `
                <h2>${data.Movie_Title}</h2>
                <p>${data.Movie_Description}</p>
            `;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please enter a movie description.');
    }
});

document.getElementById('find-movie-btn').addEventListener('click', function() {
    const description = document.getElementById('movie-description').value;
    const loadingElement = document.getElementById('loading');
    const resultElement = document.getElementById('movie-result');

    if (description) {
        loadingElement.style.display = 'block'; // Show loading message
        resultElement.innerHTML = ''; // Clear previous results if any

        fetch('https://find-a-movie-rkxhgscj6q-uc.a.run.app/get_movie', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({description: description})
        })
        .then(response => response.json())
        .then(data => {
            loadingElement.style.display = 'none'; // Hide loading message
            resultElement.innerHTML = `
                <h2>${data.Movie_Title}</h2>
                <p>${data.Movie_Description}</p>
            `;
        })
        .catch(error => {
            console.error('Error:', error);
            loadingElement.style.display = 'none'; // Hide loading message in case of error
            alert('An error occurred while fetching movie details.');
        });
    } else {
        alert('Please enter a movie description.');
    }
});

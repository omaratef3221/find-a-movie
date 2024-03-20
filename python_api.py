from flask import Flask, request, jsonify
from movies import movie_rag
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_movie', methods=['POST'])
def get_movie():
    movie_description = request.json['description']
    movie_obj = movie_rag(REVIEWS_CHROMA_PATH = 'chroma_data', device='cpu')
    vector_db = movie_obj.load_vector_database()

    movies = movie_obj.get_movie(movie_description,  vector_db)

    movie_title = "Movie Name: " + movies[0].metadata["title"]
    movie_description = "Movie Description: " + movies[0].page_content
    return jsonify({'Movie_Title': movie_title,
                    'Movie_Description': movie_description})


if __name__ == '__main__':
    app.run(debug=True, port=5050)
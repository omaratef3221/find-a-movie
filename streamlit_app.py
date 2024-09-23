import warnings
warnings.filterwarnings('ignore', category=UserWarning)
import streamlit as st
import pandas as pd
from movies import *
import io



movie_obj = movie_rag(REVIEWS_CHROMA_PATH = 'chroma_data', device='cpu')
vector_db = movie_obj.load_vector_database()

def main():
    st.title("Find My Movie!")
    amount = st.number_input("Enter the number of movies:", min_value=1, value=5, step=1)
    movie_description = st.text_input("Write the movie description", value="")

    
    movies = movie_obj.get_movie(movie_description,  vector_db, k = amount)

    # movie_title = "Movie Name: " + movies[0].metadata["title"]
    # movie_description = "Movie Description: " + movies[0].page_content
    print(movies)
    if st.button("Get the closest movies.", ):
        for i in movies:
            st.success(f"Movie Name: {i.metadata['title']}", icon= "🎬")
            st.success(f"Movie Description: {i.page_content}", icon= "📜")
            
if __name__ == '__main__':
    main()
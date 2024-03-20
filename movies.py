import pandas as pd
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DataFrameLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

class movie_rag:
    def __init__(self, df = None, device = None, main_column = "description", embeddings = "hf", REVIEWS_CHROMA_PATH = "chroma_data"):
        self.df = df
        self.main_column = main_column
        self.chroma_path = REVIEWS_CHROMA_PATH
        if device:
            self.device = device
        else:
            self.device = "cpu"
        if df:
            self.df = self.df.dropna()
            self.df = self.df.drop_duplicates()
        else:
            pass
        
        if embeddings == "hf":
            self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                            model_kwargs={'device': self.device})
        else:
            raise("Sorry only HuggingFaceEmbeddings are supported")
    
    def create_vector_database(self):
        REVIEWS_CHROMA_PATH = "chroma_data"
        
        loader = DataFrameLoader(self.df, page_content_column="description")
        descriptions = loader.load()

        reviews_vector_db = Chroma.from_documents(
            descriptions, self.embeddings, persist_directory=self.chroma_path
        )
        return reviews_vector_db
    
    def load_vector_database(self):
        reviews_vector_db = Chroma(persist_directory=self.chroma_path, embedding_function=self.embeddings)
        return reviews_vector_db
    
    def get_movie(self, description, vector_db, k = 5):
        return vector_db.similarity_search(description, k=k)
    
                    

        
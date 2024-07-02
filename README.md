
# Find-A-Movie

Welcome to the Find-A-Movie application, a powerful tool designed to recommend movies based on textual descriptions. Our app harnesses cutting-edge natural language processing technologies (RAG - Retrieval Augmented Generation) to provide an intuitive movie discovery experience.

Explore our live application: [Find-A-Movie](https://find-a-movie.streamlit.app/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Find-A-Movie is a web application that matches users with movies that closely align with the descriptions they provide. Utilizing the power of language models and vector similarity, our system can parse and understand complex descriptions, making the search for the perfect movie as easy as typing a sentence.

## Features

- **Natural Language Understanding**: Leverage language models to parse and comprehend user input.
- **Vector Similarity Search**: Utilize vector databases for efficient and relevant recommendations.
- **User-Friendly Interface**: Experience a clean and simple web interface that is easy to navigate.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python), Gunicorn
- **NLP Library**: LangChain, HuggingFace Embeddings
- **Database**: Chroma Vector Database
- **Deployment**: Google Cloud Run

## Project Structure

```
/
├── chroma_data/         # Vector database for movie descriptions
├── website/             # Static files for the frontend (HTML/CSS/JS)
├── Dockerfile           # Container configuration for the Flask API
├── movies.py            # Core recommendation algorithms
├── python_api.py        # Flask API routes and server configuration
└── streamlit_app.py     # Streamlit application
```

## Getting Started

### Prerequisites

- Python 3.9 or later
- Docker (for containerization and deployment)

### Installation

1. Clone the repository:
   ```shell
   ssh git clone https://github.com/omaratef3221/find-a-movie.git
   cd find-a-movie
   ```

2. Install the required Python packages:
   ```shell
   pip install Flask gunicorn pandas langchain flask-cors sentence-transformers chromadb langchain-community
   ```

3. Run the Streamlit app:
   ```shell
   streamlit run streamlit_app.py
   ```

4. For Flask API, navigate to the \`website/\` folder and change the API address in the JavaScript files to \`localhost\`.

## Usage

To find a movie, simply:

1. Navigate to the web application.
2. Enter a description of the movie you're thinking about in the text area.
3. Click on the "Find Movie" button to see the recommendations.

## Deployment

### Docker

To deploy using Docker:

1. Build the Docker image:
   ```shell
   docker build -t find-a-movie .
   ```

2. Run the Docker container:
   ```shell
   docker run -p 5000:5000 find-a-movie
   ```

## Contributing

We welcome contributions from the community! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank the developers and researchers whose work made this project possible. Special thanks to the creators of LangChain, HuggingFace, and ChromaDB.

---

We hope you enjoy using Find-A-Movie! For any questions or feedback, please feel free to open an issue or contact us.

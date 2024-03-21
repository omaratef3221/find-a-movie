# Find-A-Movie

Welcome to the Find-A-Movie application, a simple tool designed to recommend movies based on textual descriptions. the app harnesses cutting-edge natural language processing technologies (RAG - Retrieval Augmented Generation) to provide an intuitive movie discovery experience.

Explore our live application: [Find-A-Movie](https://find-a-movie-f506a.web.app/)

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
- **Deployment**: Google Cloud Run, Firebase Hosting

## Project Structure

Certainly! Here is a full README.md for your GitHub project with markdown formatting. This README provides an introduction to the project, instructions for setup, usage, and deployment, as well as additional relevant information. You can copy and paste this directly into your GitHub repository's README file.

markdown
Copy code
# Find-A-Movie

Welcome to the Find-A-Movie application, a powerful tool designed to recommend movies based on textual descriptions. Our app harnesses cutting-edge natural language processing technologies to provide an intuitive movie discovery experience.

Explore our live application: [Find-A-Movie](https://find-a-movie-f506a.web.app/)

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
- **Deployment**: Google Cloud Run, Firebase Hosting

## Project Structure

/
├── chroma_data/ # Vector database for movie descriptions

├── website/ # Static files for the frontend (HTML/CSS/JS)

├── Dockerfile # Container configuration for the Flask API

├── movies.py # Core recommendation algorithms

└── python_api.py # Flask API routes and server configuration


## Getting Started

### Prerequisites

- Python 3.9 or later
- Docker (for containerization and deployment)
- Node.js and npm (for deploying to Firebase)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/omaratef3221/find-a-movie.git
   cd find-a-movie

2. pip install Flask gunicorn pandas langchain flask-cors sentence-transformers chromadb langchain-community

3. python python_api.py

4. Change the address in JS to localhost


## Usage

To find a movie, simply:

Navigate to the web application.
Enter a description of the movie you're thinking about in the text area.
Click on the "Find Movie" button to see the recommendations

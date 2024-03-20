# 1 
FROM python:3.9-slim

# 2
RUN pip install --no-cache-dir Flask gunicorn pandas langchain flask-cors sentence-transformers chromadb --quiet

RUN pip install -U langchain-community scikit-learn --quiet

# 3
COPY . /app
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 python_api:app
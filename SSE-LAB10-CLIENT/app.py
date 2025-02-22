from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# URL of the first service (book API)
# BOOK_SERVICE_URL = "http://sse-lab-10.aph2g7fherfkfscm.uksouth.azurecontainer.io:8080/books"

# Get BOOK_SERVICE_URL from environment variable
BOOK_SERVICE_URL = os.getenv("BOOK_SERVICE_URL")

if not BOOK_SERVICE_URL:
    raise ValueError("Error: BOOK_SERVICE_URL is not set in environment variables")

@app.route('/')
def index():
    return render_template('index.html')  # Render search form

@app.route('/search', methods=['GET'])
def search_books():
     # Get query parameters
    genre = request.args.get('genre')
    book_id = request.args.get('id')

    # Construct request params dynamically
    params = {}
    if genre:
        params['genre'] = genre
    if book_id:
        params['id'] = book_id

    try:
        response = requests.get(BOOK_SERVICE_URL, params=params, timeout=5)
        response.raise_for_status()
        books = response.json()
    except requests.RequestException as e:
        return render_template('index.html', error=str(e))

    return render_template('index.html', books=books)  # Pass books to template


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7070)
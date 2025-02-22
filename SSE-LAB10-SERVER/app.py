from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample book data (from the given gist)
BOOKS = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]


@app.route("/")
def home():
    return "Hello, this is a Dockerized Flask app!"


# @app.route("/books", methods=["GET"])
# def get_books():
#     return jsonify(books)  # Convert the list of dictionaries to JSON and return it

@app.route('/books', methods=['GET'])
def get_books():
    genre = request.args.get('genre')
    book_id = request.args.get('id')

    filtered_books = BOOKS

    if genre:
        filtered_books = [book for book in filtered_books if genre.lower() in book['genre'].lower()]

    if book_id:
        filtered_books = [book for book in filtered_books if str(book['id']) == book_id]

    return jsonify(filtered_books)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
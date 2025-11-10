# Software Engineering Practice

This repository contains coursework lab tasks for the **Software System Engineering** module.

## Project Structure

```
Software-Engineering-Practice/
├── SSE-LAB2/           # Basic Flask app with CI/CD
├── SSE-LAB5/           # Enhanced Flask app with GitHub API integration
├── SSE-LAB10-CLIENT/   # Dockerized client microservice
├── SSE-LAB10-SERVER/   # Dockerized server microservice
└── README.md
```

## SSE-LAB2: Flask Web Application with CI/CD Pipeline

A basic Flask web application demonstrating fundamental web development concepts and continuous integration.

**Features:**
- Simple web form for name and age input
- Query processing for mathematical operations and knowledge questions
- Automated testing with pytest
- CI/CD pipeline with GitHub Actions
- Code formatting with flake8

**Key Files:**
- [`SSE-LAB2/src/app.py`](SSE-LAB2/src/app.py) - Main Flask application
- [`SSE-LAB2/src/app_test.py`](SSE-LAB2/src/app_test.py) - Unit tests
- [`SSE-LAB2/.github/workflows/build.yml`](SSE-LAB2/.github/workflows/build.yml) - CI/CD configuration

**Running the Application:**
```bash
cd SSE-LAB2
pip install -r requirements.txt
flask --app src/app.py run
```

**Testing:**
```bash
pytest ./src/*.py
```


## SSE-LAB5: Advanced Flask Application with External APIs

An enhanced Flask application integrating with GitHub API and News API, featuring repository analysis and news display.

**Features:**
- GitHub repository analysis and display
- Latest commit information retrieval
- Programming language detection
- Top 5 Tesla news articles from NewsAPI
- Enhanced UI with tabular data presentation
- Comprehensive testing suite

**Key Files:**
- [`SSE-LAB5/src/app.py`](SSE-LAB5/src/app.py) - Enhanced Flask application with API integrations
- [`SSE-LAB5/src/templates/helloGit.html`](SSE-LAB5/src/templates/helloGit.html) - GitHub data display template
- [`SSE-LAB5/requirements.txt`](SSE-LAB5/requirements.txt) - Dependencies including requests library

**APIs Used:**
- GitHub API: `https://api.github.com/users/{username}/repos`
- News API: `https://newsapi.org/v2/everything`

**Running the Application:**
```bash
cd SSE-LAB5
pip install -r requirements.txt
flask --app src/app.py run
```

## SSE-LAB10: Dockerized Microservices Architecture

A microservices-based application demonstrating containerization and service communication using Docker.

### Book API Service

A RESTful API service providing book information with filtering capabilities.

**Features:**
- RESTful API for book data
- Genre and ID-based filtering
- JSON response format
- Dockerized deployment

**Endpoints:**
- `GET /books` - Retrieve all books
- `GET /books?genre={genre}` - Filter by genre
- `GET /books?id={id}` - Filter by book ID

**Running with Docker:**
```bash
cd SSE-LAB10-SERVER
docker build -t book-server .
docker run -p 8080:8080 book-server
```

### Book Search Interface

A web interface for searching books using the book API service.

**Features:**
- User-friendly search interface
- Real-time API communication
- Error handling and display
- Environment-based service URL configuration

**Environment Variables:**
- `BOOK_SERVICE_URL` - URL of the book API service

**Running with Docker:**
```bash
cd SSE-LAB10-CLIENT
docker build -t book-client .
docker run -p 7070:7070 -e BOOK_SERVICE_URL="http://localhost:8080/books" book-client
```

---

### Acknowledgement

- **Program:** MSc Computing, Imperial College London
- **Module:** Software System Engineering 
- **Assignment:** Web Development and DevOps Laboratory Series


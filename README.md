# Basic-Devops-CICD

This project demonstrates a simple CI/CD pipeline using GitHub Actions and Docker with a minimal Flask app.

## Features
- Python + Flask microservice
- Dockerized application
- CI pipeline with GitHub Actions

## Usage
```bash
docker build -t flask-devops-app .
docker run -p 5000:5000 flask-devops-app
```

Then visit `http://localhost:5000` in your browser.

## CI/CD
On push to `main`, GitHub Actions will:
- Install Python dependencies
- Run basic (placeholder) tests
- Build Docker image
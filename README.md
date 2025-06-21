# secure-movie-service
A microservice for fetching movie details with integrated security across design, build, and deploy stages

# Secure Movie Service

A secure microservice for fetching and serving movie details, designed with integrated security best practices across design, development, and deployment stages.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Architecture](#architecture)
- [Security Controls](#security-controls)
- [Development](#development)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Secure Movie Service is a Python FastAPI microservice that provides movie details via REST API endpoints. The service emphasizes security through automated static code analysis, container vulnerability scanning, secure secrets management, and best practices in containerization and deployment.

---

## Features

- FastAPI-based REST API with asynchronous support
- Secure coding standards enforced by Bandit and CodeQL scans
- Containerized with multi-stage Docker build and security best practices
- Automated vulnerability scanning of code and containers (Bandit, Trivy, CodeQL)
- Designed for deployment with non-root containers and minimal attack surface
- Prepared for integration with secure secrets management and authentication

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (for containerization)
- Git

### Installation

1.  Clone the repository:
       bash
       git clone https://github.com/ramkumargithub/secure-movie-service.git
   cd secure-movie-service
2.  Create and activate a Python virtual environment:
       python -m venv venv
       source venv/bin/activate   # Linux/macOS
       venv\Scripts\activate      # Windows
3.  Install dependencies:
       pip install -r requirements.txt
4. Run the FastAPI app locally:
       uvicorn app.main:app --reload
5. Open your browser at http://127.0.0.1:8000/docs to access the interactive API documentation.


**### Architecture**

The service uses FastAPI to serve REST endpoints for movie data. It follows a modular design separating app logic, database access, and security controls.
The Docker container runs the app as a non-root user using a minimal base image. Automated CI/CD pipelines scan code and container images for vulnerabilities.

**### Security Controls**

Refer to SECURITY_CONTROLS.md for detailed security measures implemented, including:
	•	Static and dynamic code analysis
	•	Container security best practices
	•	Secure secrets management
	•	CI/CD integration with automated security checks

**### Development**

	•	Follow PEP8 and Python security best practices.
	•	Use GitHub Actions workflows to run Bandit, Trivy, and CodeQL scans automatically.
	•	Avoid committing secrets or sensitive data to the repository.

**### Docker**

Build the Docker image:
  docker build -t secure-movie-service .
Run the container:
  docker run -p 8000:8000 secure-movie-service
The service will be available at http://localhost:8000.

**### CI/CD Pipeline**

The project integrates security scanning into GitHub Actions with:
	•	Bandit for Python security checks
	•	Trivy for container vulnerability scans
	•	CodeQL for advanced static code analysis

These checks run automatically on every push or pull request to the main branch.

**### Contributing**

Contributions are welcome! Please follow these guidelines:
	•	Ensure all tests and security scans pass before submitting PRs.
	•	Keep dependencies up to date and check for vulnerabilities.
	•	Follow secure coding and containerization best practices.

**### Cyber Security Tests covered**

SQL Injection => test_sql_injection_in_genre
XSS => test_xss_attack_vector_in_genre
Path Traversal => test_path_traversal_in_movie_id
Type Coercion/Errors => test_type_error_in_movie_id
Rate Limiting Abuse => test_rate_limiting_on_movies_endpoint
Unauthorized Access => test_unauthorized_access_to_protected_movie




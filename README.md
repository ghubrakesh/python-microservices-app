[![Python application test with GitHub Actions](https://github.com/ghubrakesh/python-microservices-app/actions/workflows/devops.yml/badge.svg)](https://github.com/ghubrakesh/python-microservices-app/actions/workflows/devops.yml)

# wikify- A Python Microservices Web Application

This is a Python **microservices** application built with FastAPI that allows you to _search_ for Wikipedia pages and _retrieve_ page summaries. It provides a simple API for interacting with Wikipedia data.

## GitHub Workflows
1. **Continuous Integration (CI)**: Whenever changes are pushed to the repository, a CI workflow is triggered to automatically build and test the application. This ensures that each microservice functions correctly and maintains code quality.
2. **Docker Containerization**: Docker containers are used to package each microservice independently. GitHub Workflows automate the building and publishing of Docker images, allowing for easy deployment and scaling of microservices.
3. **Deployment**: With the help of GitHub Workflows, microservices can be automatically deployed to your chosen hosting environment (e.g., Kubernetes, AWS, or a container orchestration platform).
4. **Monitoring and Logging**: Each microservice can be configured with its monitoring and logging solutions. GitHub Workflows can be extended to integrate with observability tools for better visibility into the performance of each microservice.


## Getting Started

To run this project locally, follow these steps:
1. Clone the repository:
```bash
git clone <repository_url>
cd python-microservices-app
```
  
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:
```bash
python main.py
```
## Access the API in your browser or using a tool like curl or Postman.

#### API Endpoints
**Home**: Get instructions on how to use the API.
```sql
GET /
```
**Search for Pages**: Search for Wikipedia pages by providing a query.
```sql
GET /search/{query}
```
**Fetch Page Summary**: Get a summary of a Wikipedia page by providing its name.
```sql
GET /wiki/{name}
```
### Usage Examples
To search for pages related to "_Python_":
```
GET /search/Python
```

To fetch a summary of the "Python (programming language)" page:
```
GET /wiki/Python
```

### Dependencies:
1. **FastAPI**: A modern, fast web framework for building APIs with Python.
2. **uvicorn**: ASGI server for running FastAPI applications.
3. **wikipedia-api**: Python wrapper for the Wikipedia API.

**_Thank You_**

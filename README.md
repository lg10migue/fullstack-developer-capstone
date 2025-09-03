# Fullstack Developer Capstone Project

Fullstack application for managing car dealership inventory and reviews, built with Django (backend), Node.js microservices, and a React frontend.

-   Backend: [server/djangoapp](server/djangoapp)
-   Microservices: [server/database](server/database), [server/carsInventory](server/carsInventory)
-   Frontend: [server/frontend](server/frontend)
-   CI: [.github/workflows/main.yml](.github/workflows/main.yml)
-   K8s: [server/deployment.yaml](server/deployment.yaml)
-   Linting: [server/ruff.toml](server/ruff.toml)

## Project Structure

```
server/
  djangoapp/        # Django app (API, business logic)
  database/         # Node.js + MongoDB seeding + review/dealership APIs
  carsInventory/    # Inventory microservice (Node.js)
  frontend/         # React app (Register, Dealers, Post Review, etc.)
  Dockerfile        # Django container
  deployment.yaml   # K8s deployment
.github/workflows/main.yml # CI
```

## Prerequisites

-   Python 3.x
-   Node.js and npm
-   Docker and Docker Compose (optional, recommended)
-   MongoDB (via Docker Compose in microservices)

## Quick Start

### 1) Backend (Django)

```sh
cd server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Environment variables are read from [server/djangoapp/.env](server/djangoapp/.env). Ensure required keys are set.

### 2) Microservices (Node.js)

-   Database service (seeds MongoDB from JSON on startup and starts API):

    -   Code: [server/database/app.js](server/database/app.js)
    -   Models: [server/database/review.js](server/database/review.js), [server/database/dealership.js](server/database/dealership.js)
    -   Run with Docker Compose:
        ```sh
        cd server/database
        docker-compose up --build
        ```
    -   Or run locally:
        ```sh
        npm install
        node app.js
        ```
    -   Notes:
        -   Connects to MongoDB at mongodb://mongo_db:27017/ (Docker network).
        -   On start, wipes and re-inserts JSON data (reviews/dealerships).

-   Inventory service:
    -   Code: [server/carsInventory/app.js](server/carsInventory/app.js)
    -   Run with Docker Compose:
        ```sh
        cd server/carsInventory
        docker-compose up --build
        ```
    -   Or run locally:
        ```sh
        npm install
        node app.js
        ```

### 3) Frontend (React)

```sh
cd server/frontend
npm install
npm start
```

Key routes/components:

-   Dealer page: [Dealer.jsx](server/frontend/src/components/Dealers/Dealer.jsx)
-   Post review: [PostReview.jsx](server/frontend/src/components/Dealers/PostReview.jsx)
-   Register: [Register.jsx](server/frontend/src/components/Register/Register.jsx)
-   Static pages (served by Django): [server/frontend/static](server/frontend/static) (e.g., [Home.html](server/frontend/static/Home.html), [About.html](server/frontend/static/About.html), [Contact.html](server/frontend/static/Contact.html))

## API Overview (used by the frontend)

Django endpoints (referenced in the React components):

-   GET /djangoapp/dealer/:id
    -   See usage in [Dealer.jsx](server/frontend/src/components/Dealers/Dealer.jsx)
-   GET /djangoapp/reviews/dealer/:id
    -   See usage in [Dealer.jsx](server/frontend/src/components/Dealers/Dealer.jsx)
-   POST /djangoapp/add_review
    -   Expected payload (from [PostReview.jsx](server/frontend/src/components/Dealers/PostReview.jsx)):
        ```json
        {
            "name": "string",
            "dealership": 1,
            "review": "string",
            "purchase": true,
            "purchase_date": "YYYY-MM-DD",
            "car_make": "string",
            "car_model": "string",
            "car_year": 2020
        }
        ```
-   GET /djangoapp/get_cars
    -   Returns CarModels with CarMake and CarModel (see [PostReview.jsx](server/frontend/src/components/Dealers/PostReview.jsx))

Database microservice (Node.js/Mongo):

-   Seeds data from JSON and exposes review/dealership endpoints (see [server/database/app.js](server/database/app.js))

## Docker

-   Django image: [server/Dockerfile](server/Dockerfile)
-   Microservices: use each service’s docker-compose:
    -   [server/database/docker-compose.yml](server/database/docker-compose.yml)
    -   [server/carsInventory/docker-compose.yml](server/carsInventory/docker-compose.yml)

Example:

```sh
cd server/database && docker-compose up --build
cd ../carsInventory && docker-compose up --build
```

## Kubernetes

A sample deployment is provided in [server/deployment.yaml](server/deployment.yaml). Adjust images, environment variables, and services before applying to your cluster.

## CI

GitHub Actions workflow in [.github/workflows/main.yml](.github/workflows/main.yml).

## Troubleshooting

-   CORS: Node services enable CORS; ensure Django/React run on expected hosts/ports.
-   MongoDB: If running Node services locally, update the Mongo URI in [server/database/app.js](server/database/app.js) to point to your local Mongo or run via Docker Compose.

## License

Apache 2.0 — see [LICENSE](LICENSE).

## Contributing

Open issues and PRs are welcome.

## Acknowledgements

-   [Full Stack Application Development Capstone Project | Coursera](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/)
-   [Create React App](https://github.com/facebook/create-react-app)
-   [Django](https://www.djangoproject.com/)
-   [Node.js](https://nodejs.org/)

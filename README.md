# TIM EVENTS API

Welcome to the TIM EVENTS API project! This API provides endpoints for managing events and related entities such as speakers.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Testing](#testing)
5. [API Documentation](#api-documentation)
6. [Contributing](#contributing)
7. [License](#license)

## Getting Started

To get started with the TIM EVENTS API, follow the instructions below to set up the project locally.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ezeisraeljohn/tim-events-api.git
    cd tim-events-api
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Ensure you have a PostgreSQL or MySQL database set up. Update the database settings in the `database.py` file.

    ```python
    DATABASE_URL = "postgresql://username:password@localhost/dbname"
    ```

5. **Apply the migrations:**

    ```bash
    alembic upgrade head
    ```

6. **Run the server:**

    ```bash
    uvicorn main:app --reload
    ```

## Usage

Once the server is running, you can interact with the API using tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/).

## Testing

You can test the API endpoints using Postman. Import the collection directly using the following link:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/34635068-a0413fa3-3793-48cb-ba0e-abf62855e6c5?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D34635068-a0413fa3-3793-48cb-ba0e-abf62855e6c5%26entityType%3Dcollection%26workspaceId%3D617fdc8a-a7fd-4ab3-9956-411b17ec4c5a)

## API Documentation

For detailed API documentation, visit the [Swagger UI](http://localhost:8000/docs) or the [ReDoc](http://localhost:8000/redoc) endpoints provided by FastAPI.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`.
5. Push to the branch: `git push origin my-feature-branch`.
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

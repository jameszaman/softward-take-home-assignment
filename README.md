# Softward Take Home Assignment
This project is a RESTful API built using FastAPI and MongoDB that allows users to create, retrieve, update and delete properties and tenants.

## Prerequisites
- Docker
- Docker Compose

## Getting Started
1. Pull the docker image:
```bash
docker pull jameszaman/softward_test_james
```
2. Create a .env file in the  directory where you wish to run your project from and fill it with the necessary environment variables.

`MONGO_URI:` You should URI of your own mongodb project, but for testing purposes you may use the provided URI in example. But Keep in mind that other people may use the same URI making it unstuitable for any proper usage.

`MONGDB_NAME:` Give whatever name you want your database to be.

`API_PREFIX:`:  What your API endpoint route will start with.

`API_KEY`: Set this to whatever you want to be used as an API key when using any private routes.

### EXAMPLE

This is an example .env that you may wish to use.

```bash
MONGO_URI=mongodb+srv://softward:rF0Rjw7f7NaI8bUl@main.zuaqlr2.mongodb.net/?retryWrites=true&w=majority
MONGO_DB_NAME=softward
API_PREFIX=/api/v1
API_KEY=4dbe98d6d20871f32e3ebaa782ec645b452a41c87f61ee287cc138fa8c5ba795
```
3. from terminal navigate to the folder where you put your .env and run the command
```bash
docker run --env-file .env -p 8000:8000 softward_test_james
```
4. Visit `http://localhost:8000` in your browser to access the Swagger UI documentation and test the endpoints.

5. From there click on any endpoint that you would like to try. 
![Endpoint Image](docs/image_1.png)

6. At the right side you will find button `Try it out`
![Endpoint Image](docs/image_2.png)

7. Fill in the necessary parameters and press `Execute`
![Endpoint Image](docs/image_3.png)

## Folder Structure

The project has the following folder structure:
```
.
├── api
│   ├── __init__.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── connector.py
│   │   ├── properties.py
│   │   └── tenants.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── properties.py
│   │   └── tenants.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── properties.py
│   │   └── tenants.py
│   └── utils
│       ├── __init__.py
│       └── authenticate.py
├── config.py
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt

```
- `api`: contains the main application code.

- `api/database`: contains the database-related code.

- `api/models`: contains the Pydantic models used for validation and 
serialization.
- `api/routes`: contains the API routes and their handlers.

- `api/utils`: contains utility modules.

- `config.py`: contains configuration variables for the application.

- `Dockerfile`: used for building the Docker image for the application.

- `main.py`: the entry point of the application.

- `README.md`: a file with instructions and information about the project.

- `requirements.txt`: contains the Python dependencies required by the project.


## API Endpoints
- `GET /`: Redirects / route to /docs where you may test the documentation.

- `GET /health`: Checks to make sure that the API server is running.

- `GET /API_PREFIX/properties`: returns a list of all properties.

- `POST /API_PREFIX/properties`: creates a new property.

- `GET /API_PREFIX/properties/{id}`: returns a single property by ID.

- `PUT /API_PREFIX/properties/{id}`: updates a property by ID.

- `DELETE /API_PREFIX/properties/{id}`: deletes a property by ID.

- `GET /API_PREFIX/tenants/{property_id}`: creates a new tenant.

- `POST /API_PREFIX/tenants/{property_id}`: creates a new tenant.

- `PUT /API_PREFIX/tenants/{property_id}/{tenant_email}`: updates a tenant by ID.

- `DELETE /API_PREFIX/tenants/{property_id}/{tenant_email}`: deletes a tenant by ID.

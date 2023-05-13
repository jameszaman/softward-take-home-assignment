# Softward Take Home Assignment
This project is a RESTful API built using FastAPI and MongoDB that allows users to create, retrieve, update and delete properties and tenants.

## Prerequisites
- Docker
- Docker Compose

## Getting Started
1. Run the following command to pull the docker image to your system:
```bash
docker pull jameszaman/softward_test_james
```
2. Create a .env file in any directory and fill it with the necessary environment variables.

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
3. from terminal navigate to the folder where you put your .env and run the following command

```bash
docker run --env-file .env -p 8000:8000 jameszaman/softward_test_james
```
4. A server has been started. Visit `http://localhost:8000` in your browser to access the Swagger UI documentation and test the endpoints.

5. From there click on any endpoint that you would like to try. 
![Endpoint Image](docs/image_1.png)

6. At the right side you will find button `Try it out`
![Endpoint Image](docs/image_2.png)

7. Fill in the necessary parameters 
![Endpoint Image](docs/image_3.png)

8. Press `Execute` to run.
![Endpoint Image](docs/image_4.png)

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

- `GET /API_PREFIX/tenants/`: You can get all the tenants that exist or you can provide a specific email to retrieve data about a specific tenant.

## Deployment Steps
### 1. Create an AWS Account
You should first create an account if you do not have one already, create one at https://aws.amazon.com/.

### 2. Create an EC2 instance for the load balancer
After that Go to the EC2 dashboard and click on "Launch Instance". Select an Amazon Machine Image (AMI) and the instance type that meets your needs. Configure the instance details such as the number of instances, network settings, and storage. Make sure to create a security group that allows incoming traffic on port 80 and 443. When all that is done Launch the instance.

### 3. Set up the load balancer
Now you should create a new load balancer in the EC2 dashboard. Configure the load balancer with the necessary settings such as the load balancer type, listeners, target groups, and security groups. Add the EC2 instances created in Step 2 to the target group.

### 4. Set up the web servers
For each web server you need Create an EC2 instance. Install Docker and Docker Compose on each web server. Pull the Docker image for the application from your Docker Hub repository. Create a Docker Compose file that defines the services and their configuration, including the MongoDB connection details. Run the Docker Compose file to start the application.

### 5. Set up the MongoDB database
You need to a MongoDB instance in the EC2 dashboard. After that configure the MongoDB instance with the necessary settings such as storage, network access, and security. Lastly create a user for the application with the necessary permissions.

### 6. Configure the application
Update the configuration file with the MongoDB connection details. Set up environment variables to store the secret keys, tokens, and other sensitive information.

### 7. Test the application
You should test the application to make sure it is working as expected by accessing from the browser by either using the IP address or domain name.

### 8. Set up backups and monitoring
It is a good idea to configure regular backups of the MongoDB database. You may set up monitoring and logging to ensure the application is performing well and any issues are quickly identified.
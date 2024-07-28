# Infrastructure Engineer Task

## Overview

This application processes customer order data to generate various revenue statistics. It includes functionality for:

- Calculating monthly revenue
- Calculating revenue per product
- Calculating revenue per customer
- Identifying the top 10 customers by revenue

## Project Structure

- `app.py`: Main application script containing the logic for data processing.
- `test.py`: Script containing unit tests for the application.
- `requirements.txt`: Python dependencies required for the application.
- `orders.csv`: Example dataset used for development purposes.
- `Dockerfile`: Dockerfile for building the application container.
- `Dockerfile.test`: Dockerfile for building the test environment container.
- `docker-compose.yml`: Docker Compose configuration to manage multi-container deployment.
- `README.md`: This documentation file.
- `.dockerignore`: hides files from image
- `.gitignore`: hides files from git

## Instructions

### Prerequisites

- Docker
- Docker Compose (optional)

### Setup and Running the Application with Docker Compose

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build the Docker Images**:

   ```bash
   docker-compose build
   ```

3. **Run the Application**:

   ```bash
   docker-compose up app
   ```

4. **Access the Application**:
   The application does not have a web interface. Instead, it processes data and outputs results to the console.

### Running Tests with Docker Compose

1. **Build the Test Image**:

   ```bash
   docker-compose build test
   ```

2. **Run the Tests**:
   ```bash
   docker-compose run test
   ```

### Deployment with Docker Compose

To deploy the application along with the testing environment, use the following command:

````bash
docker-compose up

### Running the Application Without Docker Compose

1. **Build the Docker Image for the Application:**
    ```bash
    docker build -t myapp -f Dockerfile .
    ```
2. Run the Application Container:
    ```bash
    docker run --rm myapp
    ```
3. **Build the Docker Image for the Testing Environment:**
    ```bash
    docker build -t myapp-test -f Dockerfile.test .
    ```
4. **Run the Tests:**
    ```bash
    docker run --rm myapp-test
    ```
## Example Dataset
The orders.csv file is included as an example dataset to demonstrate the application's functionality. It contains synthetic data for development and testing purposes.

Advanced Skills Demonstration
For infrastructure-focused roles, extra points can be earned by demonstrating advanced skills such as:

Deploying the project on Docker Swarm:

Independently deploying each technology, including:
Databases (PostgreSQL or MySQL)
Redis
Other relevant services
Implementing CI/CD pipelines, Infrastructure as Code (IaC), containerization, orchestration, and cloud platforms.

Additional Information
This application is designed to be easily deployable and scalable using Docker and Docker Compose. It can be extended to integrate more complex infrastructure setups such as Kubernetes, CI/CD pipelines, and cloud deployments.

For any queries or issues, please contact:

```Agnivesh Kumar
Email: agniveshkumar15@gmail.com
LinkedIn: Agnivesh Kumar
GitHub: ImCYMBIOT```


````

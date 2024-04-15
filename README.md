# Event Management System: RESTful Service for Finding Nearby Events

This project offers a user-friendly RESTful service for discovering events happening near you. It leverages a CSV dataset for event information and provides an API to search events based on your location and desired date.

## Features and Functionality

### Data Ingestion

* **Event Upload API:** A dedicated `/addevent/` endpoint allows authorized users to submit events by providing details like name, city, date, time, and geospatial coordinates (latitude and longitude).

### Event Discovery

* **Event Search API:** The powerful `/search_events/` endpoint empowers users to find events based on their current location (latitude and longitude) and a specific date. The service returns a comprehensive list of relevant events:
    - Occurring within a specified window (e.g., the next 14 days by default) from the provided date.
    - Sorted chronologically (earliest events first) for optimal planning.

Each event response includes:

    - **Event Name:** Clearly identifies the event.
    - **City:** Indicates the location where the event takes place.
    - **Date:** Provides the date information for the event.
    - **Weather Information (External API):** Integrates real-time weather data from a reliable external API to enhance the user experience.
    - **Distance from User Location (External API):** Calculates the distance between the user's current location and the event venue using an external distance calculation API, ensuring accurate distance information.

## Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/Gl1tchk0ng/Event_gg.git](https://github.com/Gl1tchk0ng/Event_gg.git)
```
## Installing Requirements

To install the required packages, navigate to the folder where you have cloned the repository, open it in your IDE, and run the following command:

```bash
pip install -r requirements.txt
```
### CSV Data Upload

The CSV file which needs to be loaded into a database is also present in the repository.

#### Docker Installation

Install Docker from [here](<https://docs.docker.com/engine/install/>) if not already installed, and then execute the following Docker commands:

1. Pull the PostgreSQL image:
   
   ```bash
   docker pull postgres
   ```

2. **Run PostgreSQL Container**:
   
   ```bash
   docker run --name <docker_container_id> -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
   ```
3. **Access PostgreSQL Container's Bash**:

   ```bash
   docker exec -it <docker_container_id> bash
   ```
4. **Log in to PostgreSQL**:
   
   ```bash
   psql -U postgres
   ```
5. **Create Database**:
   
   ```bash
   create database d1;
   ```
6. **Connect Database to Project**:

   Update the `settings.py` file in the project's root directory (core) to connect to the database using environment variables. Refer to the environment variables listed below. After configuring the database connection, make model migrations using the `django-admin makemigrations` and `django-admin migrate` commands in the project repository.

7. **Copy CSV Data**:
   
   Use the following command to copy the CSV file from your local system to the Docker container:

   ```bash
   docker cp <local_system_file_location> <docker_container_id>:/tmp/dataset
   ```
8.  **Load CSV Data into Database**:
   
   Execute the following command to load data from the CSV file into the database:

   ```bash
   psql -U postgres -d d1 -c "COPY dataloader_eventdata (event_name, city_name, date, time, latitude, longitude) FROM '/tmp/dataset' DELIMITER ',' CSV HEADER;"
  ```
9. ***Now all the endpoints can be accessed and the operations can be done as per requirement***
### Environment Variables Initialization



In the root directory (core), create a file named `.env` and paste the following environment variables:

```plaintext
calculatorurl=External API URL that calculates the distance from the user to the event
weatherurl=External API URL that calculates the weather at the event
DATABASE_NAME=<Replace_with_your_database_name>
DATABASE_USER=postgres
DATABASE_PASSWORD=<your_password>
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
## Running the Server

Run the server and follow the link 
```bash 
python manage.py runserver
```
For all available URL options demo and expected results,https://github.com/Gl1tchk0ng/Event_gg/assets/155849958/316e2ab7-baed-4d53-b4ce-93c934ce779b

## Teach stack info
### Tech stack
- Django
- HTML
- PostgreSQL
### Stack Pros and Cons
#### Pros
- Robust security and scalability are the main reasons for preferring Django over other web dev frameworks
- PostgreSQL is a Relational Database and can be scaled with ease and maintainability is easy compared to nonrelational DBs
#### Cons
- Async support for the DB (Django-ORM)is not yet available for real-time running so the performance factor is hindered when compared with node or any other JS framework or FastAPI (Since the project is focused on the async calling of DB items for the most part using celery or Django_channels was not an option but for other real-time connections like if the ORM is changed to something like SQLAlchemy then the performance might have increased a bit.)
- Django HTML Template Engine(jinja2) is shit (Using React would be a better option)
#### Pagination was not supported by the HTML and Django Templating due to the DB retrieval's non-async support, which led to multiple different functions. I mean I ain't saying it was impossible but on the frontend part it was not directly possible still working on a workaround but on the postman testing have achieved the pagination.

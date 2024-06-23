# HBnB API

This repository contains a RESTful API for managing various entities like users, countries, cities, amenities, and places. The API is built using Flask and stores data in JSON files for persistence.

## Features

- Manage users with the ability to create, retrieve, update, and delete user data.
- Handle country data, including retrieval of all countries and specific country details.
- Manage cities, linking them to countries and supporting CRUD operations.
- Handle amenities, including creating, retrieving, updating, and deleting amenities.
- Manage places, including linking them to cities, hosts, and amenities with full CRUD operations.

## Getting Started

### Setting Up Locally

To set up and run the HBnB API on your local machine, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/boughanmiyoussef/holbertonschool-hbnb.git
    ```

2. Navigate to the project directory and set up a virtual environment:

    ```bash
    cd hbnb-api
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    flask run
    ```

5. Access the API at [http://localhost:5000](http://localhost:5000).

## Usage

### Users

- **Create a User**

    ```bash
    curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{
        "email": "youssef@email.com",
        "first_name": "Youssef",
        "last_name": "Boughanmi"
    }' | jq
    ```

- **Retrieve All Users**

    ```bash
    curl -X GET http://127.0.0.1:5000/users | jq
    ```

- **Retrieve a Specific User**

    ```bash
    curl -X GET http://127.0.0.1:5000/users/{user_id} | jq
    ```

- **Update a User**

    ```bash
    curl -X PUT http://127.0.0.1:5000/users/{user_id} -H "Content-Type: application/json" -d '{
        "email": "armorhero@email.com",
        "first_name": "Armor",
        "last_name": "Hero"
    }' | jq
    ```

- **Delete a User**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/users/{user_id} | jq
    ```

### Countries

- **Create a Country**

    ```bash
    curl -X POST http://127.0.0.1:5000/countries -H "Content-Type: application/json" -d '{
        "name": "Tunisia",
        "code": "TN"
    }' | jq
    ```

- **Retrieve All Countries**

    ```bash
    curl -X GET http://127.0.0.1:5000/countries | jq
    ```

- **Retrieve a Specific Country**

    ```bash
    curl -X GET http://127.0.0.1:5000/countries/{country_code} | jq
    ```

### Cities

- **Create a City**

    ```bash
    curl -X POST http://127.0.0.1:5000/cities -H "Content-Type: application/json" -d '{
        "name": "Tunis",
        "country_code": "TN"
    }' | jq
    ```

- **Retrieve All Cities**

    ```bash
    curl -X GET http://127.0.0.1:5000/cities | jq
    ```

- **Retrieve a Specific City**

    ```bash
    curl -X GET http://127.0.0.1:5000/cities/{city_id} | jq
    ```

- **Update a City**

    ```bash
    curl -X PUT http://127.0.0.1:5000/cities/{city_id} -H "Content-Type: application/json" -d '{
        "name": "Sousse",
        "country_code": "TN"
    }' | jq
    ```

- **Delete a City**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/cities/{city_id} | jq
    ```

### Amenities

- **Create an Amenity**

    ```bash
    curl -X POST http://127.0.0.1:5000/amenities -H "Content-Type: application/json" -d '{
        "name": "Sauna"
    }' | jq
    ```

- **Retrieve All Amenities**

    ```bash
    curl -X GET http://127.0.0.1:5000/amenities | jq
    ```

- **Retrieve a Specific Amenity**

    ```bash
    curl -X GET http://127.0.0.1:5000/amenities/{amenity_id} | jq
    ```

- **Update an Amenity**

    ```bash
    curl -X PUT http://127.0.0.1:5000/amenities/{amenity_id} -H "Content-Type: application/json" -d '{
        "name": "Sauna And Spa"
    }' | jq
    ```

- **Delete an Amenity**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/amenities/{amenity_id} | jq
    ```

### Places

- **Create a Place**

    ```bash
    curl -X POST http://127.0.0.1:5000/places -H "Content-Type: application/json" -d '{
        "name": "The One",
        "description": "The Largest Mansion.",
        "address": "Bel Air, TN",
        "city_id": "<city-id>",
        "latitude": 5000,
        "longitude": 4000,
        "host_id": "<user-id>",
        "number_of_rooms": 7,
        "number_of_bathrooms": 6,
        "price_per_night": 200,
        "max_guests": 100,
        "amenity_ids": ["<amenity-id>"]
    }' | jq
    ```

- **Retrieve All Places**

    ```bash
    curl -X GET http://127.0.0.1:5000/places | jq
    ```

- **Retrieve a Specific Place**

    ```bash
    curl -X GET http://127.0.0.1:5000/places/{place_id} | jq
    ```

- **Update a Place**

    ```bash
    curl -X PUT http://127.0.0.1:5000/places/{place_id} -H "Content-Type: application/json" -d '{
        "name": "The Two",
        "description": "The Second Largest Mansion.",
        "address": "Beverly Hills, TN",
        "city_id": "<city-id>",
        "latitude": 4000,
        "longitude": 5000,
        "host_id": "<user-id>",
        "number_of_rooms": 27,
        "number_of_bathrooms": 40,
        "price_per_night": 300,
        "max_guests": 100,
        "amenity_ids": ["<amenity-id>"]
    }' | jq
    ```

- **Delete a Place**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/places/{place_id} | jq
    ```

## Running the Server

To run the Flask server, use the following command:
```bash
flask run
```

Ensure you have Flask installed in your virtual environment and that you are in the directory where your `app.py` file is located.

## Data Persistence

The data for users, countries, cities, amenities, and places are persisted in JSON files. These files are updated whenever a create, update, or delete operation is performed on any entity.

## Testing the API

You can use tools like `curl`, Postman, or any other API testing tool to interact with the endpoints and verify their functionality.

# Restaurant Pizza Api

<hr>

# Models
- You need to create the following relationships:

    - A ```Restaurant``` has many Pizzas through RestaurantPizza
    - A ``Pizza`` has many Restaurants through RestaurantPizza
    -A ``RestaurantPizza`` belongs to a Restaurant and belongs to a Pizza

<p> Start by running migrations and test feed the db through flask shell </p>

        >>> flask db upgrade
        >>> flask db revision --autogenerate -m "your messo"
        >>> flask db upgrade

or

        >>> flask db upgrade
        >>> flask db migrate
        >>> flask db upgrade


## Validations

<h2>RestaurantPizza model</h2>

- must have a price between 1 and 30
  
<h2>Restaurant Model</h2>

- must have a name less than 50 words in length
- must have a unique name

## Routes

- routes returns JSON data in the format specified along with the appropriate HTTP verb.

### GET ```/restaurants```

- Returns JSON data in the format below:


      [
        {
          "id": 1,
          "name": "Dominion Pizza",
          "address": "Good Italian, Ngong Road, 5th Avenue"
        },
        {
          "id": 2,
          "name": "Pizza Hut",
          "address": "Westgate Mall, Mwanzi Road, Nrb 100"
        }
      ]
### GET ```/restaurants/:id```
- Restaurant exists, it returns JSON data in the format below:

      {
        "id": 1,
        "name": "Dominion Pizza",
        "address": "Good Italian, Ngong Road, 5th Avenue",
        "pizzas": [
          {
            "id": 1,
            "name": "Cheese",
            "ingredients": "Dough, Tomato Sauce, Cheese"
          },
          {
            "id": 2,
            "name": "Pepperoni",
            "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
          }
        ]
      }

- If the Restaurant does not exist, returns the following JSON data, along with the appropriate HTTP status:

      {
        "error": "Restaurant not found"
      }

### DELETE ```/restaurants/:id```

- If the Restaurant exists, it removes it from the database, along with any RestaurantPizzas that are associated with it (a RestaurantPizza belongs to a Restaurant, so it deletes the RestaurantPizzas before the Restaurant can be deleted).


- After deleting the Restaurant, it returns an empty response body, along with the appropriate HTTP status code.

- If the Restaurant does not exist, it should return the following JSON data, along with the appropriate HTTP status code:

      {
        "error": "Restaurant not found"
      }

### GET ```/pizzas```
- Returns JSON data in the format below:

      [
        {
          "id": 1,
          "name": "Cheese",
          "ingredients": "Dough, Tomato Sauce, Cheese"
        },
        {
          "id": 2,
          "name": "Pepperoni",
          "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
        }
      ]

### POST ```/restaurant_pizzas```

- This route creates a new RestaurantPizza that is associated with an existing Pizza and Restaurant. It accepts an object with the following properties in the body of the request:

      {
        "price": 5,
        "pizza_id": 1,
        "restaurant_id": 3
      }
  
- If the RestaurantPizza is created successfully, it sends back a response with the data related to the Pizza:

      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      }

- If the RestaurantPizza is not created successfully, it returns the following JSON data, along with the appropriate HTTP status code:

      {
        "errors": ["validation errors"]
      }
from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantpizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

class Display(Resource):
    def get(self):
        return make_response(
            jsonify({
                "message":"Message welcome to Restaurant Pizza api"
            }), 200
        )
api.add_resource(Display, "/")


class Restaurants(Resource):
    def get(self):
        return make_response(
            jsonify([
                {
                    "id": restau.id,
                    "name": restau.name,
                    "address": restau.address
                } for restau in Restaurant.query.all()
            ]), 200
        )
api.add_resource(Restaurants, "/restaurants")


class SingleRestaurant(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id = id).first_or_404()
        return make_response(
            jsonify(
                {
                    "id": restaurant.id,
                    "name": restaurant.name,
                    "address": restaurant.address,
                    "pizzas": (
                        [{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in restaurant.pizzas_associate]
                        if len(restaurant.pizzas_associate) > 0
                        else [{"message": "No pizzas for this restaurant"}]
                    )
                }
            ), 200
        )
api.add_resource(SingleRestaurant, "/restaurants/<int:id>")


class Pizzas(Resource):
    def get(self):
        return make_response(
            jsonify([
                {
                    "id": pizz.id,
                    "name": pizz.name,
                    "ingredients": pizz.ingredients
                } for pizz in Pizza.query.all()
            ]), 200
        )
api.add_resource(Pizzas, '/pizzas')

class Payment():
    #code goes here
    pass

class RestauPizza(Resource):
    def post(self):
        data = request.get_json()
        pizzs = Pizza.query.filter_by(id=data['pizza_id']).first()
        res = Restaurant.query.filter_by(id=data['restaurant_id']).first()

        if not pizzs or not res:
            return make_response(
                jsonify(
                {"message": "Pizza or restaurant not found"}
            ), 404
            )

        new_obj = RestaurantPizza(
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id'],
            price=data['price']
        )

        pizz = Pizza.query.filter_by(id=new_obj.pizza_id).all()

        return make_response(jsonify([{
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        } for pizza in pizz]), 201)

api.add_resource(RestauPizza, "/restaurant_pizzas")

if __name__ == '__main__':
    app.run(debug=True)

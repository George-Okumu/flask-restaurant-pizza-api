from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Restaurant

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

if __name__ == '__main__':
    app.run(debug=True)

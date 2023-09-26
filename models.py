from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 to 30")
        
        return price

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    pizzas_associate = db.relationship('Pizza', secondary="restaurant_pizzas", back_populates='restaurants_associate')

    @validates('name')
    def validate_name(self, key, name):
        if len(name) >= 50:
            raise ValueError("Name must be less than 50")
        
        if Restaurant.query.filter(Restaurant.name == name).first():
            raise ValueError("Name must be unique")
        
        return name
    

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    """

    backref='pizzas': This parameter creates a reverse 
    relationship from Restaurant to Pizza. 
    When you access Restaurant objects, you can use this reverse relationship 
    to access the associated Pizza objects. 
    The 'pizzas' argument specifies the name of this reverse relationship.
    
    """
    restaurants_associate = db.relationship('Restaurant', secondary="restaurant_pizzas", back_populates='pizzas_associate')






    



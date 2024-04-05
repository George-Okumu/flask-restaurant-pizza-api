from flask import Flask
from flask_migrate import Migrate
from models.item import db, Item
from routes.item import item_routes
from routes.home import home_routes

app = Flask(__name__) # creating an instance of flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.sqlite3'

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(item_routes)
app.register_blueprint(home_routes)



if '__name__' == "__main__":
    app.run()


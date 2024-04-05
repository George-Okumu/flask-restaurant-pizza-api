from flask import Blueprint
from models.item import Item


item_routes = Blueprint("item_routes", __name__)

@item_routes.route("/allitems")
def get_all_items():
    return [{
        "id": item.id,
        "name": item.name,
        "price": item.price
    } for item in Item.query.all()], 200


@item_routes.route("/singleitem/<int:id>")
def get_single_item(id):
    item_found = Item.query.filter_by(id = id).first()
    
    if item_found:
        return {
            "id": item_found.id,
            "name": item_found.name,
            "price": item_found.price
        }, 200
    else:
        return {"message": "Item not found"}, 404
from email import message
from flask import  request
import uuid
from db import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemGetSchema, ItemOptionalQuerySchema, ItemQuerySchema, ItemSchema, SuccessMessageSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/Usuarios")
class Item(MethodView):

    def __init__(self):
        self.db = ItemDatabase()

    @blp.response(200, ItemGetSchema(many=True))
    @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self, args):
        Documento = request.args.get('Documento')
        if Documento is None:
           
            return self.db.get_items()
        else:
            result = self.db.get_item(Documento)
            if result is None:
                 abort(404, message= f"documento no existe '{Documento}'" )
            return result

    

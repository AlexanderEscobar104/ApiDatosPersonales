from marshmallow import Schema, fields 


class ItemSchema(Schema):
    documento = fields.Str(required=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    correo = fields.Str(required=True)
    telefono = fields.Str(required=True)
    



class ItemGetSchema(Schema):
    Id = fields.Str(dump_only=True)
    Documento = fields.Str(dump_only=True)
    Nombre = fields.Str(dump_only=True)
    Apellido = fields.Str(dump_only=True)
    Correo = fields.Str(dump_only=True)
    Telefono = fields.Str(dump_only=True)


class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only=True)

class ItemQuerySchema(Schema):
    id = fields.Str(required=True)

class ItemOptionalQuerySchema(Schema):
    id = fields.Str(required=False)






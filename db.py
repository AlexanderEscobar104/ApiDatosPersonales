import pyodbc 

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-INCE964;DATABASE=DatosPersonales;')
        self.cursor = self.conn.cursor()

    def get_items(self):
        result = []
        query = "SELECT * FROM Usuarios" 
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["Id"], item_dict["Documento"] , item_dict["Nombre"], item_dict["Apellido"], item_dict["Correo"] , item_dict["Telefono"]  = row
            result.append(item_dict)
        return result
        #print(result)
    def get_item(self, item_id):
        query = f"select * from Usuarios where Documento = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["Id"], item_dict["Documento"] , item_dict["Nombre"], item_dict["Apellido"], item_dict["Correo"] , item_dict["Telefono"]  = row
            return [item_dict]
            #print(item_dict)

    


db = ItemDatabase()
#db.get_item('2')

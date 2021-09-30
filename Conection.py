import psycopg2
from psycopg2.extras import RealDictCursor
import json
class Conection:
    def __init__(self):
        self.conex = None
        self.salida = None
    
    def execute(self, comando):
        self.conex = None
        self.salida = None
        try:
            self.conex= psycopg2.connect(host="localhost", database="blockbuster", user="root", password="P@ssw0rd")
            cur= self.conex.cursor(cursor_factory= RealDictCursor)
            cur.execute(comando)
            self.salida = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conex is not None:
                self.conex.close()

    def getSalida(self):
        if self.salida is not None:
            try:
                return json.dumps(self.salida)
            except (Exception) as error:
                return "Error JSON"
        return "No hay nada"
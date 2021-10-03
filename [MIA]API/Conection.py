import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
class Conection:
    def __init__(self):
        self.salida = None
    
    def consulta(self, comando):
        conex = None
        self.salida = None
        try:
            conex= psycopg2.connect(host="localhost", database="blockbuster", user="root", password="P@ssw0rd")
            cur= conex.cursor(cursor_factory= RealDictCursor)
            cur.execute(comando)
            self.salida = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conex is not None:
                conex.close()

    def getSalida(self):
        if self.salida is not None:
            try:
                return self.salida
            except (Exception) as error:
                return "Error JSON"
        return "No hay nada"

    def crearTablas(self, comando,comentario):
        self.salida = ""
        conex = None
        try:
            conex= psycopg2.connect(host="localhost", database="blockbuster", user="root", password="P@ssw0rd")
            cur= conex.cursor()
            cur.execute(comando)
            conex.commit()
            self.salida+=comentario
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conex is not None:
                conex.close()

    def eliminarTablas(self,comando,comentario):
        self.salida = ""
        conex = None
        try:
            conex= psycopg2.connect(host="localhost", database="blockbuster", user="root", password="P@ssw0rd")
            conex.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur= conex.cursor()
            cur.execute(comando)
            conex.commit()
            self.salida+=comentario
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conex is not None:
                conex.close()
    
    def insertarDatos(self,comando,comentario):
        self.salida = ""
        conex = None
        try:
            conex= psycopg2.connect(host="localhost", database="blockbuster", user="root", password="P@ssw0rd")
            cur= conex.cursor()
            cur.execute(comando)
            conex.commit()
            self.salida+=comentario
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conex is not None:
                conex.close()
    def copiarTemporal(self):
        self.salida = ""
        conex= psycopg2.connect(host="localhost", database="blockbuster", user="root", password="P@ssw0rd")
        cur = conex.cursor()
        with open('/home/ferand20/Escritorio/Api-Blockbuster/BlockbusterData.csv', 'r') as f:
            next(f)
            cur.copy_from(f, 'temporal', sep=';',null='-')
        conex.commit()
        cur.close()
        conex.close()
        self.salida="Datos Insertados En Temporal"

    def cargarModelo(self, comando,comando2):
        self.crearTablas(comando,"Tablas Modelo Creadas\n")
        self.insertarDatos(comando2,"Datos Insertados En Modelos")


    def cargarTemporal(self, comando):
        self.crearTablas(comando,"Tabla Temporal Creadas\n")
        self.copiarTemporal()

    
    def eliminarTemporal(self, comando):
        self.eliminarTablas(comando,"Tabla Temporal Eliminada")

    def eliminarModelo(self, comando):
        self.eliminarTablas(comando,"Tablas del modelo Eliminadas")
from Conection import Conection
from flask import Flask
from flask import jsonify

app = Flask(__name__)
db = Conection()

@app.route('/', methods=['GET'])
def inicio():
    response = """
                    <h1>Practica Unica 201700858</h1>
                    <br>
                    <h3>Nombre: Elder Andrade</h3>
                    <br>
                    <h3>Carnet: 201700858</h3>
                    <br>
                    <h3>LAB MIA A+</h3>
                    """
    return response

@app.route('/consulta1', methods=['GET'])
def consulta1():
    db.consulta("""
SELECT count(pelicula.nombre) as Cantidad_de_Copias
from pelicula,inventario,tienda
where inventario.pelicula = pelicula.id
and inventario.tienda = tienda.id
and pelicula.nombre= 'SUGAR WONKA'
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta2', methods=['GET'])
def consulta2():
    db.consulta("""
select cliente.nombre,sum(renta.monto)
from cliente,renta
where cliente.id=renta.cliente
group by cliente.nombre
having  count(renta.renta) >= 40
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta3', methods=['GET'])
def consulta3():
    db.consulta("""
select 
split_part(nombre,' ',1) as nombre,
split_part(nombre,' ',2) as apellido
from actor
where split_part(nombre,' ',2) like '%son%'
order by split_part(nombre,' ',1);
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta4', methods=['GET'])
def consulta4():
    db.consulta("""
select 
split_part(actor.nombre,' ',1)as nombre,
split_part(actor.nombre,' ',2) as apellido, 
pelicula.nombre,
pelicula.anio
from pelicula,actor,reparto
where pelicula.id = reparto.pelicula
and actor.id = reparto.actor
and pelicula.descripcion like '%Crocodile%'
and pelicula.descripcion like '%Shark%'
order by split_part(actor.nombre,' ',2) asc;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta5', methods=['GET'])
def consulta5():
    db.consulta("""
select
pais.nombre,
cliente.nombre,
(count(renta.renta)*100/totales.total) as porcentaje
from cliente,renta,pais,ciudad,(
select 
pais.nombre as nombre,
count(renta.renta) as total
from renta,ciudad,pais,cliente
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
group by pais.nombre
order by pais.nombre
)as totales
where cliente.id = renta.cliente
and cliente.ciudad = ciudad.id
and ciudad.pais = pais.id
and totales.nombre = pais.nombre
group by cliente.nombre,pais.nombre,totales.total
order by porcentaje desc,pais.nombre;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta6', methods=['GET'])
def consulta6():
    db.consulta("""
select 
pais.nombre,
ciudad.nombre,
(count(cliente.nombre)*100/totales.total) as porcentaje
from pais,ciudad,cliente,(
select 
pais.nombre as nombre,
count(cliente.nombre) as total
from pais,ciudad,cliente
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
group by pais.nombre
order by pais.nombre
) as totales
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and totales.nombre = pais.nombre
group by pais.nombre,ciudad.nombre,totales.total
order by pais.nombre,ciudad.nombre;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta7', methods=['GET'])
def consulta7():
    db.consulta("""
select pais.nombre,ciudad.nombre,(count(renta.renta)/totales.total)as promedio
from cliente,pais,renta,ciudad,(
select pais.nombre as nombre,count(ciudad.nombre) as total
from pais,ciudad
where pais.id = ciudad.pais
group by pais.nombre
order by pais.nombre
) as totales
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
and pais.nombre = totales.nombre
group by pais.nombre,ciudad.nombre,totales.total
order by pais.nombre;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta8', methods=['GET'])
def consulta8():
    db.consulta("""
select pais.nombre
,(count(renta.renta)*100/totales.total)
from pais,ciudad,cliente,renta,pelicula,categoria,(
select pais.nombre as nombre
,count(renta.renta) as total
from pais,ciudad,cliente,renta
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
group by pais.nombre
order by pais.nombre
) as totales
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
and pelicula.id = renta.pelicula
and pelicula.categoria = categoria.id
and categoria.nombre = 'Sports'
and totales.nombre = pais.nombre
group by pais.nombre,totales.total
order by pais.nombre;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta9', methods=['GET'])
def consulta9():
    db.consulta("""
select ciudad.nombre, count(renta.renta)
from pais,ciudad,cliente,renta,(
select ciudad.nombre, count(renta.renta) as total
from pais,ciudad,cliente,renta
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
and ciudad.nombre = 'Dayton'
group by ciudad.nombre
order by count(renta.renta) desc
) as totales
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
and pais.nombre = 'United States'
group by ciudad.nombre,totales.total
having count(renta.renta) > total
order by count(renta.renta) desc;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta10', methods=['GET'])
def consulta10():
    db.consulta("""
select totales.ciudad,
max(totales.total) as Mayor_categoria,
max(totales1.total) as total_horror
from (
select ciudad.nombre as ciudad,
categoria.nombre as categoria,
count(renta.renta) as total
from pais,ciudad,cliente,renta,categoria,pelicula
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
and pelicula.id = renta.pelicula
and categoria.id = pelicula.categoria
group by ciudad.nombre,categoria.nombre
order by ciudad.nombre
) as totales,
(
select ciudad.nombre as ciudad, count(renta.renta) as total
from pais,ciudad,cliente,renta,categoria,pelicula
where pais.id = ciudad.pais
and ciudad.id = cliente.ciudad
and cliente.id = renta.cliente
and pelicula.id = renta.pelicula
and categoria.id = pelicula.categoria
and categoria.nombre = 'Horror'
group by ciudad.nombre
) as totales1
where totales.ciudad = totales1.ciudad
group by totales.ciudad
having max(totales1.total)>= max(totales.total)
order by totales.ciudad;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/eliminarTemporal', methods=['GET','DELETE'])
def eliminarTemporal():
    db.eliminarTemporal("""
                    drop table temporal;
                        """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/eliminarModelo', methods=['GET','DELETE'])
def eliminarModelo():
    db.eliminarModelo("""
drop table Traduccion;

drop table Reparto;

drop table Inventario;

drop table renta;

drop table ListaEmpleado;

drop table pelicula;

drop table empleado;

drop table cliente;

drop table tienda;

drop table ciudad;

drop table clasificacion;

drop table categoria;

drop table pais;

drop table actor;

drop table lenguaje;
                        """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/cargarTemporal', methods=['GET','POST'])
def cargarTemporal():
    db.cargarTemporal("""
                    create table temporal(
	                    NOMBRE_CLIENTE varchar,
	                    CORREO_CLIENTE varchar,
	                    CLIENTE_ACTIVO varchar,
	                    FECHA_CREACION date,
	                    TIENDA_PREFERIDA varchar,
	                    DIRECCION_CLIENTE varchar,
	                    CODIGO_POSTAL_CLIENTE varchar,
	                    CIUDAD_CLIENTE varchar,
	                    PAIS_CLIENTE varchar,
	                    FECHA_RENTA timestamp,
	                    FECHA_RETORNO timestamp,
	                    MONTO_A_PAGAR float8,
	                    FECHA_PAGO timestamp,
	                    NOMBRE_EMPLEADO varchar,
	                    CORREO_EMPLEADO varchar,
	                    EMPLEADO_ACTIVO varchar,
	                    TIENDA_EMPLEADO varchar,
	                    USUARIO_EMPLEADO varchar,
	                    CONTRASENA_EMPLEADO varchar,
	                    DIRECCION_EMPLEADO varchar,
	                    CODIGO_POSTAL_EMPLEADO varchar,
	                    CIUDAD_EMPLEADO varchar,
	                    PAIS_EMPLEADO varchar,
	                    NOMBRE_TIENDA varchar,
	                    ENCARGADO_TIENDA varchar,
	                    DIRECCION_TIENDA varchar,
	                    CODIGO_POSTAL_TIENDA varchar,
	                    CIUDAD_TIENDA varchar,
	                    PAIS_TIENDA varchar,
	                    TIENDA_PELICULA varchar,
	                    NOMBRE_PELICULA varchar,
	                    DESCRIPCION_PELICULA varchar,
	                    ANO_LANZAMIENTO int4,
	                    DIAS_RENTA int4,
	                    COSTO_RENTA float8,
	                    DURACION int4,
	                    COSTO_POR_DANO float8,
	                    CLASIFICACION varchar,
	                    LENGUAJE_PELICULA varchar,
	                    CATEGORIA_PELICULA varchar,
	                    ACTOR_PELICULA varchar
                    );
                    """)
    response = db.getSalida()
    return response

@app.route('/cargarModelo', methods=['GET','POST'])
def cargarModelo():
    db.cargarModelo("""
create table Lenguaje(
	id serial,
	nombre varchar not null,
	primary key(id)
);

create table Actor(
	id serial,
	nombre varchar not null,
	primary key(id)
);

create table Pais(
	id serial,
	nombre varchar not null,
	primary key(id)
);

create table Categoria(
	id serial,
	nombre varchar not null,
	primary key(id)
);

create table Clasificacion(
	id serial,
	nombre varchar not null,
	primary key(id)
);

create table Ciudad(
	id serial,
	nombre varchar not null,
	pais int4,
	primary key(id),
	FOREIGN KEY (pais) REFERENCES Pais (id)
);

create table Tienda(
	id serial,
	direccion varchar not null,
	codigopostal varchar,
	ciudad int4,
	primary key(id),
	FOREIGN KEY (ciudad) REFERENCES Ciudad(id)
);

create table Cliente(
	id serial,
	nombre varchar not null,
	activo varchar not null,
	creacion date not null,
	direccion varchar,
	codigopostal varchar,
	correo varchar,
	ciudad int4,
	tienda int4,
	primary key(id),
	FOREIGN KEY (ciudad) REFERENCES Ciudad(id),
	FOREIGN KEY (tienda) REFERENCES Tienda(id)
);

create table Empleado(
	id serial,
	nombre varchar not null,
	activo varchar not null,
	direccion varchar,
	codigopostal varchar,
	usurio varchar not null,
	contra varchar not null,
	correo varchar,
	ciudad int4,
	primary key(id),
	FOREIGN KEY (ciudad) REFERENCES Ciudad(id)
);

create table Pelicula(
	id serial,
	nombre varchar not null,
	descripcion varchar,
	anio int4,
	dias int4,
	costo float8,
	duracion int4,
	danio float8,
	clasificacion int2,
	categoria int2,
	primary key(id),
	FOREIGN KEY (clasificacion) REFERENCES Clasificacion(id),
	FOREIGN KEY (categoria) REFERENCES Categoria(id)
);

create table ListaEmpleado(
	id serial,
	encargado bool,
	tienda int4,
	empleado int4,
	primary key(id),
	FOREIGN KEY (tienda) REFERENCES Tienda(id),
	FOREIGN KEY (empleado) REFERENCES Empleado(id)
);

create table Renta(
	id serial,
	monto float8,
	pago timestamp,
	renta timestamp,
	retorno timestamp,
	cliente int4,
	pelicula int4,
	empleado int4,
	primary key(id),
	FOREIGN KEY (cliente) REFERENCES Cliente(id),
	FOREIGN KEY (pelicula) REFERENCES Pelicula(id),
	FOREIGN KEY (empleado) REFERENCES Empleado(id)
);

create table Inventario(
	id serial,
	tienda int4,
	pelicula int4,
	primary key(id),
	FOREIGN KEY (tienda) REFERENCES Tienda(id),
	FOREIGN KEY (pelicula) REFERENCES Pelicula(id)
);

create table Reparto(
	id serial,
	pelicula int4,
	actor int4,
	primary key(id),
	FOREIGN KEY (pelicula) REFERENCES Pelicula(id),
	FOREIGN KEY (actor) REFERENCES Actor(id)
);

create table Traduccion(
	id serial,
	pelicula int4,
	lenguaje int4,
	primary key(id),
	FOREIGN KEY (pelicula) REFERENCES Pelicula(id),
	FOREIGN KEY (lenguaje) REFERENCES Lenguaje(id)
);
                    """,
                    """
insert into lenguaje(nombre)
select distinct lenguaje_pelicula
from temporal
where lenguaje_pelicula is not null;

insert into actor(nombre)
select distinct actor_pelicula
from temporal
where actor_pelicula is not null;

insert into pais(nombre)
select distinct pais_cliente
from temporal
where pais_cliente is not null;

insert into categoria(nombre)
select distinct categoria_pelicula
from temporal
where categoria_pelicula is not null;

insert into clasificacion(nombre)
select distinct clasificacion
from temporal
where clasificacion is not null;

insert into ciudad(nombre,pais)
select distinct temporal.ciudad_tienda, pais.id
from temporal,pais
where temporal.ciudad_tienda is not null and pais.nombre = temporal.pais_tienda
order by pais.id;

insert into tienda(direccion,codigopostal,ciudad)
select distinct on (temporal.direccion_tienda) temporal.direccion_tienda,temporal.codigo_postal_tienda,ciudad.id
from temporal,ciudad
where temporal.direccion_tienda is not null and ciudad.nombre = temporal.ciudad_tienda;

insert into Cliente(nombre,activo,creacion,direccion,codigopostal,correo,ciudad,tienda)
select DISTINCT on (temporal.nombre_cliente) 
temporal.nombre_cliente,
temporal.cliente_activo,
temporal.fecha_creacion,
temporal.direccion_cliente,
temporal.codigo_postal_cliente,
temporal.correo_cliente,
ciudad.id,
tienda.id
from temporal,ciudad,tienda
where nombre_cliente is not null
and ciudad.nombre=temporal.ciudad_cliente
and tienda.direccion = temporal.direccion_tienda;

insert into empleado(nombre,activo,direccion,codigopostal,usurio,contra,correo,ciudad)
select DISTINCT 
temporal.nombre_empleado,
temporal.empleado_activo,
temporal.direccion_empleado,
temporal.codigo_postal_empleado,
temporal.usuario_empleado,
temporal.contrasena_empleado,
temporal.correo_empleado,
ciudad.id
from temporal,ciudad
where nombre_empleado is not null
and ciudad.nombre = temporal.ciudad_empleado;

insert into pelicula(nombre,descripcion,anio,dias,costo,duracion,danio,clasificacion,categoria)
select distinct
temporal.nombre_pelicula,
temporal.descripcion_pelicula,
temporal.ano_lanzamiento,
temporal.dias_renta,
temporal.costo_renta,
temporal.duracion,
temporal.costo_por_dano,
clasificacion.id,
categoria.id
from temporal,clasificacion,categoria
where nombre_pelicula is not null
and clasificacion.nombre = temporal.clasificacion
and categoria.nombre = temporal.categoria_pelicula;

insert into listaempleado(encargado,tienda,empleado)
select DISTINCT
true,
tienda.id,
empleado.id
from temporal,empleado,tienda
where encargado_tienda is not null
and temporal.encargado_tienda = empleado.nombre
and temporal.direccion_tienda = tienda.direccion;

insert into renta(monto,pago,renta,retorno,cliente,pelicula,empleado)
select distinct  
temporal.monto_a_pagar,
temporal.fecha_pago,
temporal.fecha_renta,
temporal.fecha_retorno,
cliente.id,
pelicula.id,
empleado.id
from temporal,cliente,pelicula,empleado
where fecha_renta is not null
and temporal.nombre_cliente = Cliente.nombre
and temporal.nombre_pelicula = pelicula.nombre
and temporal.nombre_empleado = empleado.nombre
order by cliente.id;

insert into inventario(tienda,pelicula)
select DISTINCT 
tienda.id, 
pelicula.id
from temporal,tienda,pelicula
where temporal.nombre_pelicula is not null
and temporal.direccion_tienda is not null
and temporal.nombre_pelicula = pelicula.nombre
and temporal.direccion_tienda = tienda.direccion
order by tienda.id;

insert into reparto(pelicula,actor)
select DISTINCT 
pelicula.id, 
actor.id
from temporal,actor,pelicula
where temporal.nombre_pelicula is not null
and temporal.actor_pelicula is not null
and temporal.nombre_pelicula = pelicula.nombre
and temporal.actor_pelicula = actor.nombre
order by pelicula.id;

insert into traduccion(pelicula,lenguaje)
select DISTINCT
pelicula.id,
lenguaje.id
from temporal,pelicula,lenguaje
where temporal.nombre_pelicula is not null
and temporal.nombre_pelicula = pelicula.nombre
and temporal.lenguaje_pelicula = lenguaje.nombre;
                    """)
    response = db.getSalida()
    return response

if __name__ == '__main__':
    app.run(host='localhost',port=3000,debug=True)
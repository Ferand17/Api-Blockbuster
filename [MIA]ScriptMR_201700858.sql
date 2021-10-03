--------------- creacion de tablas ---------------

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

--------------- eliminacion de tablas ---------------

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
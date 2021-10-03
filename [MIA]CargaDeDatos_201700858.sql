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
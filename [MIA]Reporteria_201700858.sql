-------------------------- consulta 1 ----------------------------
SELECT count(pelicula.nombre) as Cantidad_de_Copias
from pelicula,inventario,tienda
where inventario.pelicula = pelicula.id
and inventario.tienda = tienda.id
and pelicula.nombre= 'SUGAR WONKA'

-------------------------- consulta 2 ----------------------------
select cliente.nombre,sum(renta.monto)
from cliente,renta
where cliente.id=renta.cliente
group by cliente.nombre
having  count(renta.renta) >= 40

-------------------------- consulta 3 ----------------------------
select 
split_part(nombre,' ',1) as nombre,
split_part(nombre,' ',2) as apellido
from actor
where split_part(nombre,' ',2) like '%son%'
order by split_part(nombre,' ',1);

-------------------------- consulta 4 ----------------------------
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

-------------------------- consulta 5 ----------------------------
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

-------------------------- consulta 6 ----------------------------
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

-------------------------- consulta 7 ----------------------------
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

-------------------------- consulta 8 ----------------------------
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

-------------------------- consulta 9 ----------------------------
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

-------------------------- consulta 10 ----------------------------
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

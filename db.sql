create if not exists db_ecommerce;
use db_ecommerce;
create table products(
	id int primary key auto_increment,
    nombre varchar(100) not null,
    precio decimal(10,2) not null,
    imagen text not null
);
create table vendedores(
    id primary key auto_increment,
    nombre varchar(100) not null,
    correo varchar(100) not null
)
select * from products;

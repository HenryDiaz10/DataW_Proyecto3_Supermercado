-- 1. Dimensiones Geográficas y de Tienda
CREATE TABLE ciudades (id INT PRIMARY KEY, ciudad VARCHAR(50));
CREATE TABLE estados (id INT PRIMARY KEY, estado VARCHAR(50));
CREATE TABLE tipos_tienda (id INT PRIMARY KEY, tipo VARCHAR(5));
CREATE TABLE clusters_tienda (id INT PRIMARY KEY, cluster_nbr INT);

CREATE TABLE tiendas (
    store_nbr INT PRIMARY KEY,
    ciudad_id INT,
    estado_id INT,
    tipo_id INT,
    cluster_id INT
);

-- 2. Dimensiones de Tiempo y Eventos
CREATE TABLE tipos_feriado (id INT PRIMARY KEY, tipo VARCHAR(50));

CREATE TABLE feriados (
    id INT PRIMARY KEY,
    fecha DATE,
    tipo_id INT,
    locale VARCHAR(50),
    locale_name VARCHAR(50),
    description VARCHAR(255),
    transferred VARCHAR(10)
);

CREATE TABLE petroleo (fecha DATE PRIMARY KEY, dcoilwtico FLOAT);

-- 3. Dimensiones de Producto
CREATE TABLE familias_producto (id INT PRIMARY KEY, familia VARCHAR(50));

CREATE TABLE productos (
    item_nbr INT PRIMARY KEY,
    familia_id INT,
    perishable INT
);

-- 4. Dimensiones Operativas
CREATE TABLE clientes (cliente_id INT PRIMARY KEY, nombre VARCHAR(100), tipo_cliente VARCHAR(50));
CREATE TABLE empleados (empleado_id INT PRIMARY KEY, store_nbr INT, nombre VARCHAR(100), cargo VARCHAR(50));
CREATE TABLE metodos_pago (metodo_id INT PRIMARY KEY, descripcion VARCHAR(50));

-- 5. Tablas de Hechos (Transaccionales)
CREATE TABLE transacciones (
    id INT PRIMARY KEY,
    fecha DATE,
    store_nbr INT,
    transacciones INT
);

CREATE TABLE ventas_detalle (
    id INT PRIMARY KEY,
    fecha DATE,
    store_nbr INT,
    item_nbr INT,
    sales FLOAT,
    onpromotion INT,
    cliente_id INT,
    metodo_id INT
);
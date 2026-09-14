-- 1. Habilitar CDC a nivel de base de datos
EXEC sys.sp_cdc_enable_db;
GO

-- 2. Habilitar CDC en la tabla específica de ventas
EXEC sys.sp_cdc_enable_table 
    @source_schema = N'dbo', 
    @source_name   = N'ventas_detalle', 
    @role_name     = NULL,
    @supports_net_changes = 1;
GO

-- 3. Inserción de prueba para simular una nueva venta
INSERT INTO ventas_detalle (id, fecha, store_nbr, item_nbr, sales, onpromotion, cliente_id, metodo_id)
VALUES (9999999, '2026-09-14', 1, 1, 10.0, 0, 1, 1);
GO

-- 4. Consultar la bitácora del sistema para verificar la captura (Debe mostrar __$operation = 2)
SELECT * FROM cdc.dbo_ventas_detalle_CT;
GO
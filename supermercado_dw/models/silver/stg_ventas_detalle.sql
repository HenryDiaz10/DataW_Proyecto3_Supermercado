{{
    config(
        materialized='incremental',
        unique_key='id_venta_detalle' -- O el campo identificador único de tus ventas
    )
}}

select
    cast(id_venta_detalle as int) as id_venta_detalle,
    cast(id_producto as int) as id_producto,
    cast(cantidad as int) as cantidad,
    cast(precio_unitario as decimal(18,2)) as precio_unitario,
    cast(fecha_transaccion as datetime) as fecha_transaccion,
    current_timestamp as dbt_updated_at
from {{ source('bronze', 'ventas_detalle') }} -- Ajusta según cómo definas tu fuente Bronze

{% if is_incremental %}
    -- Esta sección asegura que solo se carguen los registros nuevos de manera incremental
    where fecha_transaccion > (select max(fecha_transaccion) from {{ this }})
{% endif %}
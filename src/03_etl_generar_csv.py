import pandas as pd
import numpy as np

print("Cargando archivos originales...")
stores = pd.read_csv("stores.csv")
holidays = pd.read_csv("holidays_events.csv")
oil = pd.read_csv("oil.csv")
transactions = pd.read_csv("transactions.csv")
train = pd.read_csv("train.csv", nrows=100000) 

print("Generando 15 tablas normalizadas...")

# 1. Dimensiones Geográficas y de Tienda
ciudades = stores[['city']].drop_duplicates().reset_index(drop=True)
ciudades.index += 1
ciudades.to_csv("01_ciudades.csv", header=False)

estados = stores[['state']].drop_duplicates().reset_index(drop=True)
estados.index += 1
estados.to_csv("02_estados.csv", header=False)

tipos_tienda = stores[['type']].drop_duplicates().reset_index(drop=True)
tipos_tienda.index += 1
tipos_tienda.to_csv("03_tipos_tienda.csv", header=False)

clusters = stores[['cluster']].drop_duplicates().reset_index(drop=True)
clusters.to_csv("04_clusters_tienda.csv", header=False)

stores_norm = stores.copy()
stores_norm['ciudad_id'] = stores_norm['city'].map({v: k for k, v in ciudades['city'].to_dict().items()})
stores_norm['estado_id'] = stores_norm['state'].map({v: k for k, v in estados['state'].to_dict().items()})
stores_norm['tipo_id'] = stores_norm['type'].map({v: k for k, v in tipos_tienda['type'].to_dict().items()})
stores_norm[['store_nbr', 'ciudad_id', 'estado_id', 'tipo_id', 'cluster']].to_csv("05_tiendas.csv", index=False, header=False)

# 2. Dimensiones de Tiempo y Eventos
tipos_feriado = holidays[['type']].drop_duplicates().reset_index(drop=True)
tipos_feriado.index += 1
tipos_feriado.to_csv("06_tipos_feriado.csv", header=False)

holidays_norm = holidays.copy()
holidays_norm['tipo_id'] = holidays_norm['type'].map({v: k for k, v in tipos_feriado['type'].to_dict().items()})
holidays_norm.index += 1
holidays_norm[['date', 'tipo_id', 'locale', 'locale_name', 'description', 'transferred']].to_csv("07_feriados.csv", header=False)

oil.to_csv("08_petroleo.csv", index=False, header=False)

# 3. Dimensiones de Producto
familias = train[['family']].drop_duplicates().reset_index(drop=True)
familias.index += 1
familias.to_csv("09_familias_producto.csv", header=False)

productos = train[['family']].drop_duplicates().reset_index(drop=True)
productos.index += 1
productos['familia_id'] = productos['family'].map({v: k for k, v in familias['family'].to_dict().items()})
productos['perishable'] = np.random.randint(0, 2, size=len(productos))
productos[['familia_id', 'perishable']].to_csv("10_productos.csv", header=False)

# 4. Dimensiones Operativas (Sintéticos)
clientes = pd.DataFrame({'nombre': ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E'], 'tipo': ['Regular', 'VIP', 'Regular', 'Nuevo', 'VIP']})
clientes.index += 1
clientes.to_csv("11_clientes.csv", header=False)

empleados = pd.DataFrame({'store_nbr': [1, 1, 2, 2, 3], 'nombre': ['Emp 1', 'Emp 2', 'Emp 3', 'Emp 4', 'Emp 5'], 'cargo': ['Cajero', 'Supervisor', 'Cajero', 'Gerente', 'Cajero']})
empleados.index += 1
empleados.to_csv("12_empleados.csv", header=False)

metodos = pd.DataFrame({'descripcion': ['Efectivo', 'Tarjeta de Credito', 'Tarjeta de Debito', 'App', 'Transferencia']})
metodos.index += 1
metodos.to_csv("13_metodos_pago.csv", header=False)

# 5. Tablas de Hechos
transactions_norm = transactions.copy()
transactions_norm.index += 1
transactions_norm[['date', 'store_nbr', 'transactions']].to_csv("14_transacciones.csv", header=False)

train_norm = train.copy()
train_norm['item_nbr'] = np.random.randint(1, len(productos)+1, size=len(train_norm))
train_norm['cliente_id'] = np.random.randint(1, 6, size=len(train_norm))
train_norm['metodo_id'] = np.random.randint(1, 6, size=len(train_norm))
train_norm[['date', 'store_nbr', 'item_nbr', 'sales', 'onpromotion', 'cliente_id', 'metodo_id']].to_csv("15_ventas_detalle.csv", index=False, header=False)

print("¡15 Archivos CSV generados con éxito!")
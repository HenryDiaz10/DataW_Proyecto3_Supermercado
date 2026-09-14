# Configuración de Servicios Vinculados en Azure Data Factory

## 1. Descripción General
En esta etapa del proyecto de Data Warehouse para el supermercado (DW3), se establecieron los puentes de conectividad seguros necesarios dentro de **Azure Data Factory (`adfsupdw3`)**. Los servicios vinculados (*Linked Services*) permiten que la factoría de datos interactúe de forma centralizada tanto con el entorno transaccional de origen como con el almacenamiento analítico.

---

## 2. Servicios Vinculados Implementados

### A. Servicio Vinculado de Origen (Azure SQL Database)
* **Nombre:** `LS_Azure_SQL_Origen`
* **Tipo de Conector:** Azure SQL Database
* **Servidor Destino:** `henryserverdw`
* **Base de Datos:** `Sup_dw3_OLTP` (Base de datos transaccional con CDC habilitado)
* **Autenticación:** Autenticación SQL (`SQL authentication`)
* **Estado:** Conexión validada y probada exitosamente desde Azure Data Factory Studio.

### B. Servicio Vinculado de Destino (Azure Data Lake Storage Gen2)
* **Nombre:** `LS_ADLS_Destino`
* **Tipo de Conector:** Azure Data Lake Storage Gen2
* **Cuenta de Almacenamiento:** `datalakesupdw3` (Contenedores: *bronze*, *silver*, *gold*)
* **Autenticación:** Clave de cuenta / Suscripción de Azure (*Azure for Students*)
* **Estado:** Conexión validada y probada exitosamente desde Azure Data Factory Studio.

---

## 3. Siguientes Pasos
Una vez configurada la conectividad de origen y destino, el proyecto avanza hacia la creación del **Pipeline de Ingesta CDC** para automatizar el volcado de datos transaccionales hacia la capa *Bronze* del Data Lake.
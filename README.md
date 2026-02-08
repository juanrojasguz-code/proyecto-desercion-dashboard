# Proyecto: Preparación de Datos para Dashboard de Deserción Educativa (Power BI)

## 1. Descripción del Proyecto
Este proyecto tiene como objetivo integrar, limpiar y preparar datos de deserción educativa a partir de múltiples fuentes, dejando un dataset final listo para ser consumido en Power BI.

El proceso está diseñado bajo principios de reproducibilidad y documentación técnica, permitiendo que cualquier evaluador pueda ejecutar el código y replicar los resultados sin necesidad de contacto adicional con el autor.

---

## 2. Estructura del Proyecto

proyecto-desercion-dashboard/
│
├── data/
│ ├── raw/
│ │ ├── desercion_municipal.csv
│ │ └── desercion_estrato.csv
│ └── processed/
│
├── src/
│ └── data_preparation.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 3. Fuentes de Datos

- **Deserción Municipal**: Información de deserción escolar por municipio, nivel educativo, zona geográfica y año.
- **Deserción por Estrato**: Información de deserción asociada al estrato socioeconómico.

Los archivos originales se encuentran en la carpeta `data/raw/`.

---

## 4. Flujo de Procesamiento de Datos (ETL)

El proyecto sigue un flujo ETL (Extract, Transform, Load) compuesto por las siguientes etapas:

1. Carga de los archivos CSV originales.
2. Limpieza y estandarización de nombres de columnas.
3. Normalización de campos de texto (municipio).
4. Conversión de tipos de datos.
5. Cruce de bases de datos mediante el municipio.
6. Manejo de valores nulos.
7. Exportación del dataset final optimizado para Power BI.

---

## 5. Requisitos del Sistema

- Python 3.9 o superior
- Librerías especificadas en el archivo `requirements.txt`

---

## 6. Instalación de Dependencias

Desde la raíz del proyecto ejecutar:

```bash
pip install -r requirements.txt

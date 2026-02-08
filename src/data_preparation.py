import pandas as pd
import unicodedata


# -----------------------------
# Funciones auxiliares
# -----------------------------


def normalizar_texto(texto):
if pd.isna(texto):
return texto
texto = texto.upper().strip()
texto = ''.join(
c for c in unicodedata.normalize('NFD', texto)
if unicodedata.category(c) != 'Mn'
)
return texto


# -----------------------------
# Carga de datos
# -----------------------------


df_municipal = pd.read_csv('data/raw/desercion_municipal.csv')
df_estrato = pd.read_csv('data/raw/desercion_estrato.csv')


# -----------------------------
# Limpieza y estandarización
# -----------------------------


for df in [df_municipal, df_estrato]:
df.columns = df.columns.str.lower().str.replace(' ', '_')


# Normalizar municipio
df_municipal['municipio'] = df_municipal['municipio'].apply(normalizar_texto)
df_estrato['municipio'] = df_estrato['municipio'].apply(normalizar_texto)


# Conversión de tipos
if 'anio' in df_municipal.columns:
df_municipal['anio'] = df_municipal['anio'].astype(int)


# -----------------------------
# Cruce de bases
# -----------------------------


df_final = pd.merge(
df_municipal,
df_estrato,
on='municipio',
how='left'
)


# -----------------------------
# Manejo de valores nulos
# -----------------------------


df_final.fillna({
'estrato': 'NO INFORMADO'
}, inplace=True)


# -----------------------------
# Exportación
# -----------------------------


df_final.to_csv(
'data/processed/dataset_final_pbi.csv',
index=False,
encoding='utf-8-sig'
)


print('Proceso finalizado. Dataset listo para Power BI.')


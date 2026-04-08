import pandas as pd

print("=== TRANSFORM INICIADO ===")

df = pd.read_csv("compras.csv")

print("Filas antes:", len(df))

# normalizar texto
df['producto'] = df['producto'].str.lower().str.strip()

# convertir números
df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')
df['descuento'] = pd.to_numeric(df['descuento'], errors='coerce')


df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

df = df.dropna()


df = df[(df['cantidad'] > 0) & (df['precio_unitario'] > 0)]

df = df.drop_duplicates()

df['total'] = df['cantidad'] * df['precio_unitario'] * (1 - df['descuento'])

print("Filas después:", len(df))

df.to_csv("datos_limpios.csv", index=False)

print("=== TRANSFORM FINALIZADO ===")
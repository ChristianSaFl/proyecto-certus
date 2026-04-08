import pandas as pd

print("=== EXTRACT INICIADO ===")

try:
    df = pd.read_csv("compras.csv")
    print("Archivo leído correctamente")
    print("Filas:", len(df))
except Exception as e:
    print("Error al leer el archivo:", e)
    exit()

print("Columnas:", df.columns.tolist())


df.to_csv("compras_backup.csv", index=False)

print("=== EXTRACT FINALIZADO ===")
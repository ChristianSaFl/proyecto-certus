import pandas as pd

print("=== LOAD INICIADO ===")

df = pd.read_csv("datos_limpios.csv")


total_general = df['total'].sum()


gasto_producto = df.groupby('producto')['total'].sum()


gasto_proveedor = df.groupby('proveedor_id')['total'].sum()


gasto_distrito = df.groupby('distrito')['total'].sum()


gasto_almacen = df.groupby('almacen')['total'].sum()

gasto_empleado = df.groupby('empleado')['total'].sum()

print("\nTOTAL GENERAL:", total_general)
print("\nGasto por producto:\n", gasto_producto)
print("\nGasto por proveedor:\n", gasto_proveedor)
print("\nGasto por distrito:\n", gasto_distrito)
print("\nGasto por almacén:\n", gasto_almacen)
print("\nGasto por empleado:\n", gasto_empleado)


gasto_producto.to_csv("reporte_producto.csv")
gasto_proveedor.to_csv("reporte_proveedor.csv")
gasto_distrito.to_csv("reporte_distrito.csv")
gasto_almacen.to_csv("reporte_almacen.csv")
gasto_empleado.to_csv("reporte_empleado.csv")

print("Reportes generados correctamente")

print("=== LOAD FINALIZADO ===")
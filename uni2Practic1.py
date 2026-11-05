
import pandas as pd

# 1. Importar el archivo CSV
df = pd.read_csv("ventas.csv")

# 2. Mostrar los primeros 10 registros
print("\nPRIMEROS 10 REGISTROS")
print(df.head(10))

# 3. Cantidad de filas y columnas
print("\nFILAS Y COLUMNAS")
print(df.shape)
print("Registros:", df.shape[0])
print("Variables:", df.shape[1])

# 4. Nombres de las variables
print("\nNOMBRES DE COLUMNAS")
print(df.columns.tolist())

# 5. Tipos de datos
print("\nTIPOS DE DATOS")
print(df.dtypes)
print("\nINFORMACION GENERAL")
df.info()

# 6. Clasificacion de variables
print("\nVARIABLES CUALITATIVAS")
print(df.select_dtypes(include=["object", "category"]).columns.tolist())

print("\nVARIABLES CUANTITATIVAS")
print(df.select_dtypes(include="number").columns.tolist())

# 7. Clasificacion segun el tipo
print("\nCLASIFICACION")
print("Categoria: cualitativa nominal")
print("Metodo de pago: cualitativa nominal")
print("Cantidad: cuantitativa discreta")
print("Precio: cuantitativa continua")
print("Fecha: temporal (si existe)")

# 8. Tipo de estructura
print("\nTIPO DE DATASET")
print("Estructurado: los datos estan organizados en filas y columnas.")

# 9. Categorias disponibles
print("\nCATEGORIAS")
print(df["categoria"].unique())

# 10. Registros por categoria
print("\nREGISTROS POR CATEGORIA")
print(df["categoria"].value_counts())

# 11. Estadisticas descriptivas
print("\nESTADISTICAS DE PRECIO Y CANTIDAD")
print(df[["precio", "cantidad"]].describe())

# 12. Cantidad vendida por categoria
print("\nPRODUCTOS VENDIDOS POR CATEGORIA")
ventas_categoria = df.groupby("categoria")["cantidad"].sum()
print(ventas_categoria)

# PREGUNTAS FINALES

print("\nRESPUESTAS")

print("1. Registros:", df.shape[0])
print("   Variables:", df.shape[1])

print("2. Cualitativa describe caracteristicas.")
print("   Cuantitativa representa cantidades numericas.")

print("3. Cantidad es discreta porque cuenta unidades enteras.")

print("4. Metodo de pago mas utilizado:")
print(df["metodo_pago"].value_counts().idxmax())

print("5. Categoria con mas productos vendidos:")
print(ventas_categoria.idxmax())

# 6. Monto total de ventas
df["total"] = df["precio"] * df["cantidad"]
print("6. Monto total de ventas:", df["total"].sum())

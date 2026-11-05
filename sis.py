
import pandas as pd

# ==========================================
# ETAPA 1: EXTRACCIÓN DE DATOS
# ==========================================

# Cargar el archivo CSV
df = pd.read_csv("ventasETL.csv")

# Mostrar los primeros 10 registros
print("\nPRIMEROS 10 REGISTROS:")
print(df.head(10))

# Mostrar dimensiones, columnas y tipos de datos
print("\nDIMENSIONES:")
print(df.shape)

print("\nCOLUMNAS:")
print(df.columns)

print("\nINFORMACIÓN DEL DATASET:")
df.info()

# Identificar valores nulos y duplicados
print("\nVALORES NULOS POR COLUMNA:")
print(df.isnull().sum())

print("\nREGISTROS DUPLICADOS:")
print(df.duplicated().sum())

nulos_iniciales = df.isnull().sum().sum()
duplicados_iniciales = df.duplicated().sum()


# ==========================================
# ETAPA 2: TRANSFORMACIÓN DE DATOS
# ==========================================

# Eliminar registros duplicados
df = df.drop_duplicates().copy()

# Limpiar nombres de categorías y sucursales
df["categoria"] = df["categoria"].str.strip().str.title()
df["sucursal"] = df["sucursal"].str.strip().str.title()

# Convertir fechas al formato correcto
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

# Limpiar símbolos de moneda y convertir precios
df["precio_unitario"] = (
    df["precio_unitario"]
    .astype("string")
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convertir columnas numéricas
for columna in ["cantidad", "precio_unitario", "edad_cliente"]:
    df[columna] = pd.to_numeric(df[columna], errors="coerce")

# Corregir valores incorrectos
# Cantidades y precios deben ser mayores que cero
df.loc[df["cantidad"] <= 0, "cantidad"] = pd.NA
df.loc[df["precio_unitario"] <= 0, "precio_unitario"] = pd.NA

# Edades válidas entre 0 y 100 años
df.loc[
    ~df["edad_cliente"].between(0, 100),
    "edad_cliente"
] = pd.NA

# Tratar valores nulos numéricos con la mediana
for columna in ["cantidad", "precio_unitario", "edad_cliente"]:
    df[columna] = df[columna].fillna(df[columna].median())

# Completar productos faltantes
df["producto"] = df["producto"].fillna("Desconocido")

# Eliminar registros sin fecha válida
df = df.dropna(subset=["fecha"])

# Convertir cantidad y edad a enteros
df["cantidad"] = df["cantidad"].round().astype(int)
df["edad_cliente"] = df["edad_cliente"].round().astype(int)

# Crear columna de rangos de edad
df["rango_edad"] = pd.cut(
    df["edad_cliente"],
    bins=[-1, 17, 29, 59, 100],
    labels=["Menor de edad", "Joven", "Adulto", "Adulto mayor"]
)

# Crear columna total_venta
df["total_venta"] = df["cantidad"] * df["precio_unitario"]


# ==========================================
# ETAPA 3: CARGA DE DATOS
# ==========================================

# Guardar el dataset limpio
df.to_csv("ventas_limpias.csv", index=False)

print("\nARCHIVO ventas_limpias.csv GUARDADO")

# Mostrar los primeros 10 registros transformados
print("\nPRIMEROS 10 REGISTROS LIMPIOS:")
print(df.head(10))


# ==========================================
# ETAPA 4: ANÁLISIS DE RESULTADOS
# ==========================================

# Agrupar ventas por categoría
ventas_categoria = df.groupby("categoria")["total_venta"].sum()

print("\nTOTAL DE VENTAS POR CATEGORÍA:")
print(ventas_categoria)

# Identificar categoría con mayores ventas
categoria_mayor = ventas_categoria.idxmax()

print("\nCATEGORÍA CON MAYORES VENTAS:")
print(categoria_mayor)

# Respuestas de la práctica
print("\nRESPUESTAS FINALES:")

print("Valores nulos encontrados:", nulos_iniciales)
print("Registros duplicados encontrados:", duplicados_iniciales)

print("\nProblemas solucionados:")
print("- Registros duplicados eliminados")
print("- Valores nulos tratados")
print("- Cantidades y precios incorrectos corregidos")
print("- Categorías y sucursales unificadas")
print("- Fechas y números convertidos")

print("\nCategoría con mayores ventas:", categoria_mayor)

print("\nValores nulos restantes:")
print(df.isnull().sum().sum())

print("\nDuplicados restantes:")
print(df.duplicated().sum())

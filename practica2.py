import pandas as pd 
import matplotlib.pyplot as plt

# ==========================================
# PRACTICA 2 - FARMACIA
# ==========================================

# 1. CREAR DATASET
datos = {
    "Producto": [
        "Paracetamol", "Ibuprofeno", "Amoxicilina",
        "Vitamina C", "Aspirina", "Jarabe para la tos",
        "Paracetamol", "Ibuprofeno", "Vitamina C",
        "Amoxicilina", "Aspirina", "Jarabe para la tos"
    ],

    "Categoria": [
        "Analgesicos", "Analgesicos", "Antibioticos",
        "Vitaminas", "Analgesicos", "Jarabes",
        "Analgesicos", "Analgesicos", "Vitaminas",
        "Antibioticos", "Analgesicos", "Jarabes"
    ],

    "Sucursal": [
        "Centro", "Norte", "Centro",
        "Sur", "Norte", "Centro",
        "Sur", "Centro", "Norte",
        "Centro", "Sur", "Norte"
    ],

    "Precio": [
        50, 80, 120, 60, 45, 90,
        50, 80, 60, 120, 45, 90
    ],

    "Cantidad": [
        30, 20, 15, 40, 50, 10,
        25, 35, 20, 10, 30, 15
    ],

    "Stock": [
        25, 8, 5, 20, 9, 10,
        30, 7, 15, 4, 12, 6
    ],

    "Metodo_Pago": [
        "Efectivo", "Tarjeta", "Efectivo",
        "Tarjeta", "Efectivo", "Transferencia",
        "Tarjeta", "Efectivo", "Efectivo",
        "Tarjeta", "Efectivo", "Efectivo"
    ]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# ==========================================
# CALCULAR INGRESOS
# ==========================================

df["Ventas"] = df["Precio"] * df["Cantidad"]

print("==========================================")
print("       DATASET DE LA FARMACIA")
print("==========================================")

print(df)

# ==========================================
# 1. REGISTROS Y COLUMNAS
# ==========================================

print("\n1. REGISTROS Y COLUMNAS")

print("Cantidad de registros:", df.shape[0])
print("Cantidad de columnas:", df.shape[1])

# ==========================================
# 2. INGRESO TOTAL
# ==========================================

print("\n2. INGRESO TOTAL")

ingreso_total = df["Ventas"].sum()

print("Ingreso total: $", ingreso_total)

# ==========================================
# 3. SUCURSAL CON MAYORES VENTAS
# ==========================================

print("\n3. SUCURSAL CON MAYORES VENTAS")

ventas_sucursal = df.groupby("Sucursal")["Ventas"].sum()

print(ventas_sucursal)

print(
    "Sucursal con mayores ventas:",
    ventas_sucursal.idxmax()
)

# ==========================================
# 4. CATEGORIA CON MAYORES INGRESOS
# ==========================================

print("\n4. CATEGORIA CON MAYORES INGRESOS")

ingresos_categoria = df.groupby("Categoria")["Ventas"].sum()

print(ingresos_categoria)

print(
    "Categoria con mayores ingresos:",
    ingresos_categoria.idxmax()
)

# ==========================================
# 5. PRODUCTO MAS VENDIDO
# ==========================================

print("\n5. PRODUCTO MAS VENDIDO EN UNIDADES")

unidades_producto = df.groupby("Producto")["Cantidad"].sum()

print(unidades_producto)

print(
    "Producto mas vendido:",
    unidades_producto.idxmax()
)

print(
    "Unidades vendidas:",
    unidades_producto.max()
)

# ==========================================
# 6. STOCK IGUAL O MENOR A 10
# ==========================================

print("\n6. PRODUCTOS CON STOCK BAJO")

stock_bajo = df[df["Stock"] <= 10]

print(stock_bajo)

print(
    "Registros con stock igual o menor a 10:",
    len(stock_bajo)
)

# ==========================================
# 7. METODO DE PAGO MAS UTILIZADO
# ==========================================

print("\n7. METODO DE PAGO MAS UTILIZADO")

metodos = df["Metodo_Pago"].value_counts()

print(metodos)

print(
    "Metodo de pago mas utilizado:",
    metodos.idxmax()
)

# ==========================================
# 8. DECISIONES
# ==========================================

print("\n8. DECISIONES PARA LA FARMACIA")

print(
    "1. Reabastecer los productos que tengan "
    "un stock igual o menor a 10 unidades."
)

print(
    "2. Promover los productos y categorias que "
    "generan mayores ingresos para aumentar las ventas."
)

# ==========================================
# RESUMEN FINAL
# ==========================================

print("\n==========================================")
print("              RESUMEN")
print("==========================================")

print("Registros:", df.shape[0])
print("Columnas:", df.shape[1])
print("Ingreso total: $", ingreso_total)
print("Sucursal con mayores ventas:", ventas_sucursal.idxmax())
print("Categoria con mayores ingresos:", ingresos_categoria.idxmax())
print("Producto mas vendido:", unidades_producto.idxmax())
print("Registros con stock <= 10:", len(stock_bajo))
print("Metodo de pago mas utilizado:", metodos.idxmax())
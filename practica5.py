import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# ACTIVIDAD 5 - DATASET PALMER PENGUINS
# ==========================================

# 1. Importar el dataset
df = pd.read_csv("penguins.csv")


# 2. Mostrar los primeros 10 registros
print("\n--- PRIMEROS 10 REGISTROS ---")
print(df.head(10))


# 3. Mostrar las dimensiones del dataset
print("\n--- DIMENSIONES DEL DATASET ---")
print(df.shape)


# 4. Mostrar los nombres de las columnas
print("\n--- COLUMNAS ---")
print(df.columns)


# 5. Revisar los tipos de datos
print("\n--- INFORMACIÓN DEL DATASET ---")
df.info()


# 6. Obtener estadísticas generales
print("\n--- ESTADÍSTICAS GENERALES ---")
print(df.describe())


# 7. Identificar datos vacíos
print("\n--- DATOS VACÍOS ---")
print(df.isnull().sum())


# 8. Identificar registros duplicados
print("\n--- REGISTROS DUPLICADOS ---")
print(df.duplicated().sum())


# ==========================================
# 9. REALIZAR 2 FILTROS
# ==========================================

# Filtro 1: Pingüinos de la especie Adelie
filtro1 = df[df["species"] == "Adelie"]

print("\n--- PINGÜINOS ADELIE ---")
print(filtro1.head(10))


# Filtro 2: Pingüinos que pesan más de 5000 gramos
filtro2 = df[df["body_mass_g"] > 5000]

print("\n--- PINGÜINOS CON PESO MAYOR A 5000 G ---")
print(filtro2.head(10))


# ==========================================
# 10. AGRUPACIÓN CON GROUPBY
# ==========================================

promedio_especie = df.groupby("species")["body_mass_g"].mean()

print("\n--- PESO PROMEDIO POR ESPECIE ---")
print(promedio_especie)


# ==========================================
# 11. TOP 5
# ==========================================

top5 = df.sort_values("body_mass_g", ascending=False).head(5)

print("\n--- TOP 5 PINGÜINOS MÁS PESADOS ---")
print(top5[["species", "island", "body_mass_g"]])


# ==========================================
# 12. RESULTADOS ESTADÍSTICOS
# ==========================================

peso_promedio = df["body_mass_g"].mean()
peso_maximo = df["body_mass_g"].max()

print("\n--- RESULTADOS ESTADÍSTICOS ---")
print("Peso promedio:", peso_promedio, "gramos")
print("Peso máximo:", peso_maximo, "gramos")


# ==========================================
# 13. GRÁFICA 1
# Peso promedio por especie
# ==========================================




# ==========================================
# 14. GRÁFICA 2
# Cantidad de pingüinos por especie
# ==========================================

df["species"].value_counts().plot(
    kind="bar",
    title="Cantidad de pingüinos por especie"
)

plt.xlabel("Especie")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()
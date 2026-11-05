import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PRACTICA 3 - NETFLIX
# ==========================================

# 1. IMPORTAR ARCHIVO DE EXCEL
df = pd.read_excel("netflixPractica.xlsx", sheet_name="Netflix_Datos")

print("DATASET DE NETFLIX")
print(df.head())

# ==========================================
# 2. MOSTRAR PRIMEROS REGISTROS
# ==========================================

print("\nPRIMEROS REGISTROS")
print(df.head())

# ==========================================
# 3. TAMAÑO DEL DATASET
# ==========================================

print("\nTAMAÑO DEL DATASET")

print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])
print("Tamaño:", df.shape)

# ==========================================
# 4. INFORMACION DEL DATASET
# ==========================================

print("\nINFORMACION DEL DATASET")

df.info()

# ==========================================
# 5. DATOS VACIOS
# ==========================================

print("\nDATOS VACIOS")

print(df.isnull().sum())

# ==========================================
# 6. REGISTROS DUPLICADOS
# ==========================================

print("\nREGISTROS DUPLICADOS")

print("Duplicados:", df.duplicated().sum())

# ==========================================
# 7. ELIMINAR DUPLICADOS
# ==========================================

df = df.drop_duplicates()

print("\nDUPLICADOS DESPUES DE ELIMINAR")

print(df.duplicated().sum())

# ==========================================
# 8. ELIMINAR / COMPLETAR DATOS VACIOS
# ==========================================

df["País"] = df["País"].fillna("Desconocido")

df["Título"] = df["Título"].fillna("Sin título")

df["Calificacion"] = df["Calificacion"].fillna(
    df["Calificacion"].median()
)

# ==========================================
# 9. ELIMINAR ESPACIOS INNECESARIOS
# ==========================================

for columna in df.select_dtypes(include="object").columns:
    df[columna] = df[columna].str.strip()

print("\nDATOS LIMPIOS")

print(df.head())

# ==========================================
# 10. NORMALIZAR ALGUNOS DATOS
# ==========================================

df["Género"] = df["Género"].replace({
    "COMEDIA": "Comedia",
    "ROMANCE": "Romance"
})

df["Dispositivo"] = df["Dispositivo"].replace({
    "celular": "Celular"
})

# ==========================================
# 11. HORAS VISTAS POR GENERO
# ==========================================

print("\nHORAS VISTAS POR GENERO")

horas_genero = df.groupby(
    "Género"
)["Horas_Vistas"].sum()

print(horas_genero)

# ==========================================
# 12. TOP 5 TITULOS CON MAS HORAS VISTAS
# ==========================================

print("\nTOP 5 TITULOS CON MAS HORAS VISTAS")

top5 = df.sort_values(
    by="Horas_Vistas",
    ascending=False
).head(5)

print(
    top5[["Título", "Horas_Vistas"]]
)

# ==========================================
# 13. DISPOSITIVO MAS UTILIZADO
# ==========================================

print("\nDISPOSITIVO MAS UTILIZADO")

dispositivos = df["Dispositivo"].value_counts()

print(dispositivos)

print(
    "Dispositivo más utilizado:",
    dispositivos.idxmax()
)

# ==========================================
# 14. GRAFICA DE HORAS VISTAS POR GENERO
# ==========================================

horas_genero.plot(
    kind="bar"
)

plt.title("Horas vistas por género")

plt.xlabel("Género")

plt.ylabel("Horas vistas")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ==========================================
# 15. GUARDAR DATASET LIMPIO
# ==========================================

df.to_excel(
    "netflix_limpio.xlsx",
    index=False
)

print("\n====================================")
print("ARCHIVO GUARDADO CORRECTAMENTE")
print("====================================")

print("netflix_limpio.xlsx")
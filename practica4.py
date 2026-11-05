import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/RitvikChouhan/Spotify_Analysis/main/spotify_tracks.csv"

df = pd.read_csv(url)

# ==========================================
# 2. MOSTRAR LOS PRIMEROS REGISTROS
# ==========================================

print("\n--- PRIMEROS REGISTROS ---")
print(df.head())


# ==========================================
# 3. REVISAR TAMAÑO Y CONTENIDO
# ==========================================

print("\n--- TAMAÑO DEL DATASET ---")
print(df.shape)

print("\n--- INFORMACIÓN DEL DATASET ---")
df.info()


# ==========================================
# 4. BUSCAR DATOS VACÍOS Y DUPLICADOS
# ==========================================

print("\n--- DATOS VACÍOS ---")
print(df.isnull().sum())

print("\n--- DATOS DUPLICADOS ---")
print(df.duplicated().sum())


# ==========================================
# 5. ELIMINAR DUPLICADOS
# ==========================================

df = df.drop_duplicates()

print("\nDuplicados después de limpiar:")
print(df.duplicated().sum())


# ==========================================
# 6. 10 CANCIONES CON MAYOR POPULARIDAD
# ==========================================

top_canciones = df.sort_values(
    by="popularity",
    ascending=False
).head(10)

print("\n--- 10 CANCIONES MÁS POPULARES ---")
print(top_canciones[["track_name", "artists", "popularity"]])


# ==========================================
# 7. 10 ARTISTAS CON MÁS CANCIONES
# ==========================================

top_artistas = df["artists"].value_counts().head(10)

print("\n--- 10 ARTISTAS CON MÁS CANCIONES ---")
print(top_artistas)


# ==========================================
# 8. POPULARIDAD PROMEDIO POR GÉNERO
# ==========================================

popularidad_genero = (
    df.groupby("track_genre")["popularity"]
    .mean()
)

print("\n--- POPULARIDAD PROMEDIO POR GÉNERO ---")
print(popularidad_genero)


# ==========================================
# 9. 10 GÉNEROS CON MAYOR POPULARIDAD
# ==========================================

top_generos = popularidad_genero.sort_values(
    ascending=False
).head(10)

print("\n--- 10 GÉNEROS MÁS POPULARES ---")
print(top_generos)


# ==========================================
# 10. GRÁFICA
# ==========================================

top_generos.plot(
    kind="bar",
    title="10 géneros con mayor popularidad promedio"
)

plt.xlabel("Género")
plt.ylabel("Popularidad promedio")
plt.tight_layout()
plt.show()


# ==========================================
# 11. ANÁLISIS DE UN GÉNERO
# ==========================================

genero = "rock"

df_genero = df[df["track_genre"] == genero]

print("\n--- ANÁLISIS DEL GÉNERO:", genero.upper(), "---")

# Canción más popular
cancion_popular = df_genero.sort_values(
    by="popularity",
    ascending=False
).head(1)

print("\nCanción más popular:")
print(cancion_popular[["track_name", "artists", "popularity"]])


# Artista más frecuente
artista_frecuente = df_genero["artists"].value_counts().head(1)

print("\nArtista más frecuente:")
print(artista_frecuente)


# Popularidad promedio
promedio_popularidad = df_genero["popularity"].mean()

print("\nPopularidad promedio:")
print(promedio_popularidad)


# Promedio de danceability
promedio_danceability = df_genero["danceability"].mean()

print("\nPromedio de danceability:")
print(promedio_danceability)

# Promedio de energy
promedio_energy = df_genero["energy"].mean()
print("\nPromedio de energy:")
print(promedio_energy)


# ==========================================
# 12. GUARDAR RESULTADOS EN EXCEL
# ==========================================

with pd.ExcelWriter("spotify_resultados.xlsx") as writer:

    df.to_excel(
        writer,
        sheet_name="Datos_Limpios",
        index=False
    )

    top_canciones.to_excel(
        writer,
        sheet_name="Top_Canciones",
        index=False
    )

    top_artistas.to_excel(
        writer,
        sheet_name="Top_Artistas"
    )

    top_generos.to_excel(
        writer,
        sheet_name="Top_Generos"
    )

    df_genero.to_excel(
        writer,
        sheet_name="Genero_Rock",
        index=False
    )

print("\nArchivo spotify_resultados.xlsx guardado correctamente.")

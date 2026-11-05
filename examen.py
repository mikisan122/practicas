import pandas as pd 
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-17/office_ratings.csv"

df = pd.read_csv(url)
# /////////////
print("\n--- PRIMEROS 10 REGISTROS ---")
print(df.head(10))

# ///////////////
print("\n--- COLUMNAS ---")
print(df.columns)
# ////////////////

print("\n--- DATOS VACÍOS ---")
print(df.isnull().sum())
# ////////////////
print("\n--- REGISTROS DUPLICADOS ---")
print(df.duplicated().sum())
# ////////////////
print("\n---  EPISODIOS DE TEMPORADA 5 ---")
print(df[df['season'] == 5])
# ///////////// 

print("\n--- CALIFICACION MAYOR 8.5 ---")
print(df[df['imdb_rating'] > 8.5])

# ///////////////////////

print("\n--- ME FUI XD NO LE ENTENDI A LA 7  ---")


# //////////////////////////////

print("\n--- TOP 5 EPISODIOS CON MAYOR CALIFICACIÓN ---")
print(df.nlargest(5, 'imdb_rating'))

# ///////////////// 

print("\n--- calificacion promedio de episodios ---")
print(df['imdb_rating'].mean()) 
# //////////////////
print("\n--- mayor numero de espectadores registrados   ---")
print(df['total_votes'].max())

#///////////////////////
print("\n--- grafica de calificacion promedio por temporada  ---")
df.groupby('season')['imdb_rating'].mean().plot(kind='bar')
plt.xlabel('Temporada')
plt.ylabel('Calificación Promedio')
plt.title('Calificación Promedio por Temporada')
plt.show()

# ///////////////////////
print("\n--- grafica de 5 episodios  con mayor calificacion  ---")
df.nlargest(5, 'imdb_rating').groupby('season')['imdb_rating'].mean().plot(kind='bar')
plt.xlabel('Temporada')
plt.ylabel('Calificación Promedio')
plt.title('Calificación Promedio por Temporada')
plt.show()

#  temporada que obtuvo la mayor calificacion promedio de episodios R = 4 
# cual fue el eposodio con mayor calificacion R = season 7 episodio, 21 9.7



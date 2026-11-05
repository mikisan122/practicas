import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Cargar el dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
df = pd.read_csv(url)

# 2. Exploración del dataset
print("Primeros 10 registros:")
print(df.head(10))

print("\nFilas y columnas:")
print(df.shape)

print("\nInformación del dataset:")
df.info()

print("\nValores nulos:")
print(df.isnull().sum())

print("\nEstadísticas:")
print(df.describe())

# 3. Limpieza de datos
df = df.dropna(subset=["horsepower", "mpg"])

print("\nRegistros después de la limpieza:")
print(df.shape)

# 4. Definir variables X y Y
x = df[["horsepower"]]
y = df["mpg"]

# 5. Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(x, y)

# 6. Obtener pendiente e intercepto
print("\nPendiente:", round(modelo.coef_[0], 2))
print("Intercepto:", round(modelo.intercept_, 2))

# 7. Realizar las 5 predicciones
nuevos_datos = pd.DataFrame({
    "horsepower": [75, 100, 125, 150, 175]
})

predicciones = modelo.predict(nuevos_datos)

print("\nPredicciones:")

for hp, mpg in zip(nuevos_datos["horsepower"], predicciones):
    print(f"Automóvil de {hp} HP: {mpg:.2f} MPG")

# 8. Graficar resultados
plt.scatter(
    x["horsepower"],
    y,
    label="Datos reales",
    alpha=0.5
)

# Ordenar los datos para dibujar correctamente la línea
x_ordenado = x.sort_values(by="horsepower")

plt.plot(
    x_ordenado["horsepower"],
    modelo.predict(x_ordenado),
    color="blue",
    label="Línea de regresión"
)

# Mostrar las predicciones
plt.scatter(
    nuevos_datos["horsepower"],
    predicciones,
    color="red",
    marker="x",
    s=100,
    label="Predicciones"
)

plt.xlabel("Caballos de fuerza (HP)")
plt.ylabel("Rendimiento de combustible (MPG)")
plt.title("Regresión lineal - HP vs MPG")
plt.legend()
plt.grid(True)
plt.show()
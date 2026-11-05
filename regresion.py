import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos = {
    "HorasEstudio": [1, 2, 3, 4, 5, 6, 7, 8],
    "Calificacion": [55, 60, 65, 70, 75, 80, 85, 90]
}

df = pd.DataFrame(datos)

# Variables
x = df[["HorasEstudio"]]
y = df["Calificacion"]

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(x, y)

# Predicción para 9 horas
nuevo_dato = pd.DataFrame({"HorasEstudio": [9]})
prediccion = modelo.predict(nuevo_dato)

# Resultados
print("Calificación estimada:", prediccion[0])
print("Pendiente:", round(modelo.coef_[0], 2))
print("Intercepto:", round(modelo.intercept_, 2))

# Gráfica
plt.scatter(x["HorasEstudio"], y, label="Datos reales")

plt.plot(
    x["HorasEstudio"],
    modelo.predict(x),
    label="Línea de regresión"
)

plt.scatter(
    9,
    prediccion[0],
    color="red",
    label="Predicción",
    marker="x",
    s=100
)

plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")
plt.title("Regresión lineal - Horas de estudio")
plt.legend()
plt.grid(True)
plt.show()
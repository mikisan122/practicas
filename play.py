import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Datos de los clientes
datos = {
    "Edad": [25, 22, 25, 28, 30, 35, 40, 45, 50, 21, 27, 38],
    "Ingresos": [5000, 70000, 90000, 11000, 12000, 75000,
                 180000, 200000, 250000, 6000, 80000, 170000],
    "Compra": [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Exploración de datos
print(df.head())
print(df.info())
print(df["Compra"].value_counts())

# Definir variables
X = df[["Edad", "Ingresos"]]
y = df["Compra"]

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Crear y entrenar el modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Realizar predicciones
predicciones = modelo.predict(X_test)

# Evaluar exactitud
exactitud = accuracy_score(y_test, predicciones)

print("Exactitud:", exactitud)
print("Exactitud en porcentaje:", round(exactitud * 100, 2), "%")

# Predicción de un nuevo cliente
nuevo_cliente = pd.DataFrame({
    "Edad": [32],
    "Ingresos": [140000]
})

resultado = modelo.predict(nuevo_cliente)

if resultado[0] == 1:
    print("El cliente probablemente comprará")
else:
    print("El cliente probablemente no comprará")

# Predicción de varios clientes
nuevosClientes = pd.DataFrame({
    "Edad": [20, 25, 30, 35, 45],
    "Ingresos": [60000, 90000, 120000, 200000, 250000]
})

# Realizar predicciones
nuevosClientes["Prediccion"] = modelo.predict(
    nuevosClientes
)

print("\nPredicciones de nuevos clientes:")
print(nuevosClientes)

# Asignar colores según la predicción
colores = nuevosClientes["Prediccion"].map({
    0: "red",
    1: "green"
})

# Crear gráfica
plt.figure(figsize=(10, 6))

plt.scatter(
    nuevosClientes["Edad"],
    nuevosClientes["Ingresos"],
    c=colores,
    s=180,
    edgecolors="black"
)

# Agregar etiquetas a los puntos
for i in range(len(nuevosClientes)):

    resultado = nuevosClientes["Prediccion"].iloc[i]

    etiqueta = "Compra" if resultado == 1 else "No Compra"

    plt.annotate(
        etiqueta,
        (
            nuevosClientes["Edad"].iloc[i],
            nuevosClientes["Ingresos"].iloc[i]
        ),
        xytext=(5, 10),
        textcoords="offset points"
    )

# Personalizar gráfica
plt.title("Predicciones de Compra de los Nuevos Clientes")
plt.xlabel("Edad del cliente")
plt.ylabel("Ingresos mensuales ($)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
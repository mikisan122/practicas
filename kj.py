import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Cargar el dataset Titanic
df = sns.load_dataset("titanic")

# 2. Mostrar los primeros 10 registros
print("\nPRIMEROS 10 REGISTROS")
print(df.head(10))

# 3. Seleccionar las columnas
df = df[["age", "pclass", "survived"]]

print("\nCOLUMNAS SELECCIONADAS")
print(df.head(10))

# 4. Eliminar registros con datos vacíos
df = df.dropna()

print("\nDATOS DESPUÉS DE ELIMINAR VALORES VACÍOS")
print(df.info())

# 5. Separar variables independientes y dependiente
X = df[["age", "pclass"]]
y = df["survived"]

# 6. Dividir datos: 70% entrenamiento y 30% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

print("\nDATOS DE ENTRENAMIENTO:", len(X_train))
print("DATOS DE PRUEBA:", len(X_test))

# 7. Crear y entrenar el árbol de decisión
modelo = DecisionTreeClassifier(
    random_state=42
)

modelo.fit(X_train, y_train)

# 8. Realizar predicciones
predicciones = modelo.predict(X_test)

# 9. Crear DataFrame con resultados reales y predicciones
resultados = pd.DataFrame({
    "Real": y_test.values,
    "Prediccion": predicciones
})

print("\nRESULTADOS REALES Y PREDICCIONES")
print(resultados)

# 10. Identificar predicciones correctas e incorrectas
correctas = (resultados["Real"] == resultados["Prediccion"]).sum()
incorrectas = (resultados["Real"] != resultados["Prediccion"]).sum()

print("\nPREDICCIONES CORRECTAS:", correctas)
print("PREDICCIONES INCORRECTAS:", incorrectas)

# 11. Calcular porcentaje de exactitud
exactitud = accuracy_score(y_test, predicciones)

print("\nEXACTITUD DEL MODELO:")
print(f"{exactitud * 100:.2f}%")

# 12. Crear cuatro pasajeros nuevos
nuevos_pasajeros = pd.DataFrame({
    "age": [10, 25, 45, 70],
    "pclass": [1, 2, 3, 1]
})

# 13. Predecir supervivencia
nuevas_predicciones = modelo.predict(nuevos_pasajeros)

nuevos_pasajeros["Prediccion"] = nuevas_predicciones

nuevos_pasajeros["Resultado"] = nuevos_pasajeros[
    "Prediccion"
].map({
    0: "No sobrevivió",
    1: "Sobrevivió"
})

print("\nPREDICCIONES DE NUEVOS PASAJEROS")
print(nuevos_pasajeros)

# 14. Visualizar el árbol de decisión
plt.figure(figsize=(16, 8))

plot_tree(
    modelo,
    feature_names=["age", "pclass"],
    class_names=["No sobrevivió", "Sobrevivió"],
    filled=True,
    rounded=True,
    max_depth=3
)

plt.title("Árbol de decisión - Titanic")
plt.show()
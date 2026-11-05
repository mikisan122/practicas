import pandas as pd 
import matplotlib.pyplot as plt

#crear df 
datos = {
    "producto": ["SODA", "SABRITAS", "PAPAS", "QUESO"],
    "precio": [10, 15, 7, 12],
    "cantidad": [100, 150, 200, 120]
}

df = pd.DataFrame(datos)
print("DATOS DE LA TIENDA")
print(df)

#AGREGAR UNA COLUMNA 
df["total"] = df["precio"] * df["cantidad"]
print("\nVENTAS TOTALES")
print(df)

print("\nRESULTADO ")
print("total de ventas: $", df["total"].sum())
print("promedio de precio: $", df["precio"].mean())
print("producto mas caro: $", df.loc[df["precio"].idxmax(), "producto"])
print("mayor cantidad vendida: ", df["cantidad"].max())


#filtar

print("\nPRODUCTOS CON PRECIO MAYOR A 1000")

productos_caros = df[df["precio"] > 1000]
print(productos_caros)  

#garfica
df.plot(
x="producto",
y="cantidad",\
 kind="bar",
 legend=False,
)

plt.title("Cantidad de productos vendidos")
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()
import pandas as pd

df = pd.read_csv("ventas_comida.csv")

cols = df[['cantidad', 'precio_promedio']]

#Realizar un análisis inicial con medidas estadísticas básicas
#MEDIDAS DE TENDENCIA CENTRAL 

print("CENTRALIZACIÓN")
media= round(cols.mean(),2)
print("Media: \n" , media)
mediana = round(cols.median(),2)
print("Mediana: \n", mediana)
moda= cols.mode()
print("Moda: \n", moda)

#MEDIDAS DE DISPERSION
rango = cols.max() - cols.min()
print("Rango :\n", rango)
desviacion_estandar = cols.std()
print("Desviación estandar :\n", desviacion_estandar)
varianza = cols.var()
print("Varianza :\n", varianza)


#Identificar valores atípicos
q1 = cols.quantile(0.25)
print("Cuartil 25 :\n", q1)
q3 = cols.quantile(0.75)
print("Cuartil 75 : \n", q3)
iqr = q3 - q1 
print("IQR :\n",iqr)
limite_inf = q1 - 1.5 * iqr
limite_sup = q3 + 1.5 * iqr
print("Limite inferior : \n", limite_inf)
print("Limite superior :\n", limite_sup)

outliers = df[
    (df['cantidad'] < limite_inf['cantidad']) | (df['cantidad'] > limite_sup['cantidad']) |
    (df['precio_promedio'] < limite_inf['precio_promedio']) | (df['precio_promedio'] > limite_sup['precio_promedio'])
]
print("Outliers:\n", outliers)
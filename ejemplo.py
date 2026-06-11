#Importamos la libreria 
import pandas as pd

#Creamos el conjunto de datos como un diccionario
data = {
    'Valores': [10,15,14,18,19,21,23,20,22,25,30,17,16]
}

#Convertimos el diccionario en un DataFrame
df= pd.DataFrame(data)

#Mostrar el dataset
print("Dataset ejemplo:\n", df)

#Calcular desviacion estandar
desviacion_estandar = round(df['Valores'].std(),2)
print("Desviacion estandar: ", desviacion_estandar)

#Varianza
varianza = round(df['Valores'].var(),2)
print("Varianza: ", varianza )


#Percentiles

percentil_25= df['Valores'].quantile(0.25)
print( "Percentil 25 : ", percentil_25)

percentil_50= df['Valores'].quantile(0.50)
print("Percentil 50:", percentil_50)

percentil_75 = df['Valores'].quantile(0.75)
print("Percentil 75:", percentil_75)

#Media
media = round(df['Valores'].mean(),2)
print("Media: ", media )

#Mediana
mediana = round(df['Valores'].median(),2)
print("Mediana: ", mediana)

#Rango
rango = df['Valores'].max() - df['Valores'].min()
print("Rango :", rango)
import pandas as pd
data = ({
    'Edad' : [18,22,25,30,35,40,28,32,45,50]
})
df = pd.DataFrame(data)
print("Dataset:\n ", df)
#La media 
media = df['Edad'].mean()
print("La media es: ", media )
#Mediana
mediana= df['Edad'].median()
print("La mediana es: ", mediana)
#Moda
moda = df['Edad'].mode()
print("La moda es: ", moda)
#Rango 
rango = df['Edad'].max() - df['Edad'].min()
print('El rango es :' , rango)
#Desviación estandar
desviacion = round(df['Edad'].std(),2)
print("Desviacion:", desviacion)
#Varianza
varianza = round(df['Edad'].var(),2)
print( "La varianza es: ", varianza)
#Percentiles
per_25= df['Edad'].quantile(0.25)   #25% de los datos están por debajo
print("Percentil 25 : ", per_25)
per_50= df['Edad'].quantile(0.50)
print("Percentil 50: ", per_50)
per_75=df['Edad'].quantile(0.75)
print("Percentil 75 :", per_75)

import pandas as pd

df = pd.DataFrame({
    "nota": [5,6,7,8,9,4,6,8,10,7]
})

print("Desviación estándar:", df["nota"].std())
print("Varianza:", df["nota"].var())
print("Percentil 25:", df["nota"].quantile(0.25))
print("Percentil 50:", df["nota"].quantile(0.50))
print("Percentil 75:", df["nota"].quantile(0.75))
print("Media :" , df["nota"].mean())
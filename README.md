# Análisis Exploratorio de Pedidos de Comida
# PRACTICA 1

## Descripción
Análisis exploratorio de un dataset de pedidos de comida por zonas y  categorías, aplicando estadística básica, detección de outliers y visualización de datos.

## Dataset
Dataset de 23 registros con las siguientes columnas:
- **fecha**: fecha del pedido
- **zona**: zona geográfica (Norte, Sur, Este, Oeste, Centro)
- **cantidad**: unidades pedidas
- **precio_promedio**: precio medio del producto (€)
- **categoria_comida**: tipo de producto (Bebidas, Verduras, Frutas, Carnes, Pescados, Panadería)

## Análisis realizado
1. **Estadísticas básicas**: media, mediana, moda, rango, 
   desviación típica y varianza
2. **Detección de outliers**: mediante método IQR
3. **Visualización**: gráficos de barras, histograma y gráfica de líneas
4. **Tendencia temporal**: evolución mensual de pedidos

## PREGUNTAS DE REFLEXIÓN

### 1. ¿Qué insights se pueden extraer sobre el rendimiento de pedidos por zona y categoría de comida?

Por zona: Podemos observar que la zona en la que más pedidos se hacen 
es en el sur, parte de este liderazgo puede estar influenciado por un 
valor atípico de 950 unidades de bebidas. Podría considerarse factible 
ya que en el sur hace buen tiempo y la gente suele salir y beber 
refrescos, cervezas, agua... También podemos observar que las zonas con 
menos pedidos son norte y oeste, esto puede deberse a la diferencia del 
clima, suele hacer más frío y la gente decide salir menos.

Por categoría: El producto más vendido son las bebidas, lo que hace que 
el sur lidere en ventas. El segundo producto más vendido son las verduras, 
destacan por su precio económico y accesible, son cruciales en la 
alimentación y suelen hacerse pedidos grandes. Por otro lado el producto 
menos pedido son los pescados, uno de los productos más caros, y 
casualmente donde más se piden es en el norte y oeste, las zonas con 
menos pedidos totales.

### 2. ¿Existen patrones de demanda relacionados con el tiempo? ¿Algún mes o día de la semana muestra mayor actividad?

Al ser un dataset pequeño no podemos analizar bien los días de la semana 
ya que algunos días pueden no aparecer reflejados. Disponemos de 3 meses 
de datos y según el gráfico los pedidos suben a partir del mes 2, esto es 
debido en parte al outlier del día 25 del mes 3 con un pedido de bebidas 
de 950 unidades. Con solo 3 meses no podríamos saber si en meses 
posteriores seguiría subiendo o bajando — se necesitarían más datos para 
confirmar una tendencia real.

### 3. ¿Se detectan anomalías en la cantidad de pedidos en alguna zona o categoría?

Se detectaron dos anomalías mediante el método IQR (límite superior de 
452.5 para cantidad y 19.92 para precio_promedio):
- Cantidad = 950 (Sur, Bebidas): se mantiene en el dataset ya que es 
  factible teniendo en cuenta el clima del sur.
- Precio_promedio = 42.50 (Norte, Pescados): se mantiene ya que las zonas 
  del norte suelen tener pescados de mayor calidad y precio elevado.
# NOTAS LOCATION INTELLIGENCE ([DOTGIS](<https://www.dotgiscorp.com/es/>))

## _Clase 17/12/2022_

Definición Location Intelligence:
> Modernos sistemas GIS.
> GIS = Sistema de Información Geográfica con estas características:

1. Sistema de Información: una base de datos como sistema de almacenamiento de información estructurado. Esto nos permite analizar la información mediante procesos mate´maticos

2. Geográfica: la información tiene una referencia en cuanto a la ubicación.


Los modelos GIS se aplican al Business Inteligence gracias al inmenso desarrollo de Internet y la web en los últimos 20 años, lo que ha permitido automatizar y procesar toda esta información democratizando el dato.


A día de hoy se busca hacer la visualización de los datos más intuitiva, ya que mucha gente utiliza herramientas basadas en sistemas de geolocalización a diario.

Tipos de datos:

- Vectoriales: elementos de tipo discreto del "mundo real" representables mediante vectores. Los datos vectoriales representan información puntual en el espacio de forma precisa. Hay tres tipos: puntos, líneas y polígonos.

- Raster: elementos agregados del "mundo real" representables mediante una matriz formada por celdas. Estos datos representan información representativa de esa celda.



El tipo de archivo más utilizado es el GeoJSON, que es un JSON pero con coordenadas geométricas. Una web interesate para generar GeoJSON es [geojson.io](https://geojson.io).


## Mapas

Un sistema de coordenadas define la localización espacial de los datos así como la relación de los elementos en la superficie.

Un sistema de coordenadas geográficas es un sistema de coordenadas esféricas mediante el cual se localizan objetos en la Tierra. El sistema más habitual de trabajo es el 4326, aunque google trabaja con el 3857 para la Web.

Un sistema de coordendas cartesianas es un sistema de coordinadas proyectadas que sed basa en una proyección de mapas como Transverssal de Mercato, Albers equal area o Robinson. 
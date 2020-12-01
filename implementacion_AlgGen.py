################################################
################################################
# Implementación de nuestro algoritmo genético para el problema del viajero
################################################
################################################



import algoritmo_genetico as algG
import pandas as pd
import folium



################################################
# Preparamos todo y graficamos lo inicial


ListaCiudades = pd.read_csv("Qatar.csv")

# Las convertimos a unidades adecuadas para poder graficar en el mapa
ListaCiudades['Latitud'] = ListaCiudades['Latitud']/1000
ListaCiudades['Longitud'] = ListaCiudades['Longitud']/1000

# Para graficar usamos folium y lo guardamos en un documento html
# si no lo hacemos así, no lo vamos a poder abrir después
        
latitude = 25.3
longitude = 51.51

Quatar_map = folium.Map(location=[latitude, longitude], zoom_start=10)
# Quatar_map.save("Quatar.html")

# Le ponemos los puntitos de las ciudades consideradas

# instantiate a feature group for the incidents in the dataframe
ciudades = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(ListaCiudades.Latitud, ListaCiudades.Longitud):
    ciudades.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
Quatar_map.add_child(ciudades)
Quatar_map.save("Quatar.html")




################################################
# Ahora sí usamos el algoritmo genético

n_Ciudades = ListaCiudades.shape[0] # Calculamos cuántas ciudades tenemos

ListaCoordenadas = []

for i in range(0,n_Ciudades):
    ListaCoordenadas.append(algG.City(x=ListaCiudades.Latitud[i], y=ListaCiudades.Longitud[i] ))



Mejor_Ruta = algG.geneticAlgorithm(population=ListaCoordenadas, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)

# Agregamos la mejor ruta al mapa con líneas
Coordenadas_Mejor_Ruta = []
for i in range(0, n_Ciudades):
    Coordenadas_Mejor_Ruta.append( (Mejor_Ruta[i].x,  Mejor_Ruta[i].y) )


folium.PolyLine(Coordenadas_Mejor_Ruta, color="blue", weight=0.5).add_to(Quatar_map)


Quatar_map.save("Quatar_Ruta_Optima.html")




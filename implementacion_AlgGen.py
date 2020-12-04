################################################
################################################
# Implementación de nuestro algoritmo genético para el problema del viajero
################################################
################################################



import algoritmo_genetico as algG
import pandas as pd
#import folium
#from folium import plugins
#import folium.plugins
import time


################################################
# Preparamos todo y graficamos lo inicial


ListaCiudades = pd.read_csv("Qatar.csv")
ListaCiudades.drop_duplicates(subset=None, keep='first', inplace=False)

# Las convertimos a unidades adecuadas para poder graficar en el mapa
ListaCiudades['Latitud'] = ListaCiudades['Latitud']/1000
ListaCiudades['Longitud'] = ListaCiudades['Longitud']/1000

# Para graficar usamos folium y lo guardamos en un documento html
# si no lo hacemos así, no lo vamos a poder abrir después
        
#latitude = 25.3
#longitude = 51.51

#Quatar_mapOpt = folium.Map(location=[latitude, longitude], zoom_start=10)
#Quatar_mapInit = Quatar_mapOpt
# Quatar_map.save("Quatar.html")

# Le ponemos los puntitos de las ciudades consideradas

# instantiate a feature group for the incidents in the dataframe
#ciudades = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
#for lat, lng, in zip(ListaCiudades.Latitud, ListaCiudades.Longitud):
#    ciudades.add_child(
#        folium.features.CircleMarker(
#            [lat, lng],
#            radius=5, # define how big you want the circle markers to be
#            color='yellow',
#            fill=True,
#            fill_color='blue',
#            fill_opacity=0.6
#        )
#    )

# add incidents to map
#Quatar_mapOpt.add_child(ciudades)
#Quatar_mapInit.add_child(ciudades)
#Quatar_mapOpt.save("Quatar.html")




################################################
# Ahora sí usamos el algoritmo genético

n_Ciudades = ListaCiudades.shape[0] # Calculamos cuántas ciudades tenemos

ListaCoordenadas = []

for k in range(0,n_Ciudades):
    ListaCoordenadas.append(algG.City(x=ListaCiudades.Latitud[k], y=ListaCiudades.Longitud[k], i = ListaCiudades.Ciudad[k] ))


tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=500)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()

print(toc-tic)

# Agregamos la mejor ruta al mapa con líneas
place_lat_opt = []
place_lng_opt = []
place_lat_init = []
place_lng_init = []
for i in range(0, 193):
    place_lat_opt.append( Mejor_Ruta[i].x )
    place_lng_opt.append( Mejor_Ruta[i].y )
    place_lat_init.append( ListaCiudades.Latitud[i] )
    place_lng_init.append( ListaCiudades.Longitud[i] )


points_opt = []
points_init = []
for i in range(len(place_lat_opt)):
    points_opt.append([place_lat_opt[i], place_lng_opt[i]])
    points_init.append([place_lat_init[i], place_lng_init[i]])


uno_o = points_opt[1]


    
folium.PolyLine(exp_o, color='red').add_to(Quatar_mapOpt)

folium.PolyLine(exp_i, color='red').add_to(Quatar_mapInit)
    

Quatar_mapOpt.save("Quatar_Ruta_Optima.html")
Quatar_mapInit.save("Quatar_Init.html")



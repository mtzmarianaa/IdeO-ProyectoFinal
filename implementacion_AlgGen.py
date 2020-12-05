################################################
################################################
# Implementación de nuestro algoritmo genético para el problema del viajero
################################################
################################################



import algoritmo_genetico as algG
import pandas as pd
import time
import seaborn as sns
import random


################################################
# Preparamos todo y graficamos lo inicial


ListaCiudades = pd.read_csv("Qatar.csv")

ListaCiudades.drop_duplicates(subset=None, keep='first', inplace=False)

# Las convertimos a unidades adecuadas para poder graficar en el mapa
ListaCiudades['Latitud'] = ListaCiudades['Latitud']/1000
ListaCiudades['Longitud'] = ListaCiudades['Longitud']/1000




################################################
################################################
################################################
# Ahora sí usamos el algoritmo genético

n_Ciudades = ListaCiudades.shape[0] # Calculamos cuántas ciudades tenemos

ListaCoordenadas = []

for k in range(0,n_Ciudades):
    ListaCoordenadas.append(algG.City(x=ListaCiudades.Latitud[k], y=ListaCiudades.Longitud[k], i = ListaCiudades.Ciudad[k] ))


################################################
    # 100 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=100)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0, 100)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)

sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#573572' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 20, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 100 iteraciones, 14.18 seg')






################################################
    # 150 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=150)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,150)) , 'Distancia': Mejor_Ruta['Distances']}

sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#713572' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 20, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 150 iteraciones, 20.50 seg')




################################################
    # 200 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=200)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,200)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)


sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#72355a' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 20, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 200 iteraciones, 27.18 seg')





################################################
    # 250 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=250)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,250)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)

sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#47b4bb' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 10, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 250 iteraciones, 27.18 seg')








################################################
    # 300 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=300)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,300)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)


sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#214a97' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 10, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 300 iteraciones, 41.46 seg')




################################################
    # 350 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=350)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,350)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)

sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#152e76' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 10, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 350 iteraciones, 47.15 seg')





################################################
    # 400 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=400)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,400)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)

sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#154d76' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 10, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 400 iteraciones, 55.39 seg')





################################################
    # 450 iteraciones

random.seed(23) # Ponemos la semilla para poder comparar los resultados

tic = time.clock()
Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=450)
Mejor_Ruta = Algoritmo_usado.perform()
toc = time.clock()
print(toc-tic)

# Ahora para visualizar los resultados
# Primero obtenemos el orden en el que van las ciudades

optimal_Order = []

for i in range(len(Mejor_Ruta['best_Route'])):
    optimal_Order.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i]) )



dat = {'Iteracion': list(range(0,450)) , 'Distancia': Mejor_Ruta['Distances']}

dat = pd.DataFrame(dat)

sns.set_style("whitegrid")
a = sns.set_palette(sns.color_palette(['#156976' ]))
grafica_algGen_Distancias = sns.scatterplot(
    data=dat,
    x="Iteracion", y="Distancia", palette=a, s = 10, linewidth=0)

grafica_algGen_Distancias.set_title('Algoritmo Genético 450 iteraciones, 60.56 seg')




################################################
################################################
################################################
# Con esta semilla, el minimo es en la iteracion 257, entonces sacamos esa ruta

random.seed(23) # Ponemos la semilla para poder comparar los resultados

Algoritmo_usado = algG.geneticAlogrithm(population=ListaCoordenadas, 
                                        popSize=100, eliteSize=20, 
                                        mutationRate=0.01, generations=257)
Mejor_Ruta = Algoritmo_usado.perform()

indices_ruta_opt = []

for i in range(len(Mejor_Ruta['best_Route'])):
    indices_ruta_opt.append( ListaCoordenadas.index(Mejor_Ruta['best_Route'][i] ) )


indices_ruta_opt




################################################
################################################
################################################



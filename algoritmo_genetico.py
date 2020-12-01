# Proyecto final Investigación de operaciones
# Otoño 2020
#
# Cómo se divide este proyecto
#
# Esta es la implementación del algoritmo genetico


# Impementación propia de:
# https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

# Definiciones previas:
#    Gene: una ciudad, representada con las coordenadas (x,y)
#    Individual/chromosome: una sola ruta que satisface las condiciones
#    Population: colección de todas las posibles rutas (aka la colección de 
#                los individuals)
#    Parents: dos rutas que al ser combinadas crean una nueva ruta
#    Mating pool: la colección de parents que son usados para nuestra 
#                 siguiente población
#    Fitness: una función que nos dice que tan buena es nuestra ruta (la 
#             distancia), queremos minimizar esto
#    Mutation: una manera de introducir variación en nuestra población, 
#              intercambiamos de manera aleatoria dos ciudades en una ruta
#    Elitism: una manera de tomar los mejores individuals para la siguiente
#             generación

import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


################################################
################################################
# Primero creamos dos clases: City y Fitness. 
# Lo primero que hacemos es crear estas clases, la clase City nos va a ayudar a
# manejar todas las ciudades que tenemos. Solo son las coordenadas (x,y) que 
# vamos a leer del csv. En esta clase le agregamos distance, la cual calcula
# la distancia Euclidiana entre las dos ciudades. 

################################################
# Creamos la clase City, esto lo podemos usar para otros metodos que 
# resuelvan el problema del viajero

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Calculamos la distancia entre esta ciudad y otra ciudad 'city'
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2)) # Distancia euclidiana
        return distance
     # Una manera de imprimir mejor las coordenadas de esta ciudad
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
################################################
# Creamos la clase Fitness, va a ser el recíproco de la distancia de la ruta
# actual. Como queremos minimizar la distancia de la ruta, entonces queremos
# un score de Fitness grande. Uno extra: queremos empezar y terminar en el
# mismo lugar. El Fitness obviamente depende de la ruta que tenemos y ya.


class Fitness:
    # Inicializamos
    def __init__(self, route):
        self.route = route # la ruta que estamos considerando
        self.distance = 0
        self.fitness= 0.0
    
    # Calculamos la distancia de la ruta
    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i] # La ciudad de donde partimos, en la ruta
                toCity = None # La ciudad a donde llegamos
                if i + 1 < len(self.route): # Si no hemos llegado al final de la ruta
                    toCity = self.route[i + 1] # la ciudad a donde llegamos es la siguiente en la lista
                else:
                    toCity = self.route[0]  # Si llegamos al final, la siguiente ciudad es de donde partimos
                pathDistance += fromCity.distance(toCity) # Sumamos las distancias entre ambas ciudades
            self.distance = pathDistance # Le decimos que esa es la distancia de esa ruta
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance()) # El Fitness es el reciproco de la distancia de la ruta
        return self.fitness



################################################
################################################
# Segundo: creamos la population. Debemos de crear la primera generación, o 
# la población inicial (colección de todas las posibles rutas). Para poder
# crear las rutas debemos de asegurarnos que éstas satisfagan las condiciones
# iniciales del problema. Creamos rutas al azar para nuestra primera 
# generación


def createRoute(cityList):
    # Genera una sola ruta al azar dentro del listado de ciudades
    route = random.sample(cityList, len(cityList))
    return route


def initialPopulation(popSize, cityList):
    # Crea popSize rutas al azar
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population



################################################
################################################
# Tercero: determinamos con cuáles rutas quedarnos. Usamos Fitness para
# rankear las rutas y ver cuáles son mejores de acuerdo a este criterio
# Esto saca una lista ordenada de las rutas (de mejor a peor) y su score
# de Fitness asociado.

def rankRoutes(population):
    fitnessResults = {} # Repito, necesitamos una lista
    for i in range(0,len(population)): # Hacemos esto para cada ruta que tenemos
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True) # las ordenamos


################################################
################################################
# Cuarto: Seleccionamos el mating pool, es decir la colección de parents que 
# son usados para nuestra siguiente población. En esta implementación usamos 
# el criterio de elitism, es decir seleccionar los mejores individuals (rutas)
# de la población para que éstas sigan en la siguiente generación. 
# Para seleccionar cuáles son los mejores consideramos el Fitness de cada ruta
# o individual relativo a la población (o todas las rutas). Se asigna una
# probabilidad de selección ponderada por esto, entre mejor Fitness tenga,
# mayor probabilidad tiene de ser seleccionada.

def selection(popRanked, eliteSize):
    selectionResults = []  # vector de los seleccionados
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"]) # el
    # data frame de la población que estamos considerando (lo ponemos bonito)
    df['cum_sum'] = df.Fitness.cumsum() # columna de la suma acumulada de Fitness
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum() # probabilidad (pesos)
    
    for i in range(0, eliteSize): # seleccionamos los mejores
        selectionResults.append(popRanked[i][0]) # las rutas
    for i in range(0, len(popRanked) - eliteSize): # cuántos nos quedamos
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0]) # los seleccionamos
                break
    return selectionResults

# Ya tenemos las rutas que van a ir en el mating pool 

def matingPool(population, selectionResults):
    matingpool = [] # vector de las rutas que van a ir aquí
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index]) # las agregamos
    return matingpool

################################################
################################################
# Quinto: Con los seleccionados del mating pool vamos a crear la siguiente 
# generación de rutas. Para esto hacemos un cossover (es como generar hijos 
# de las rutas que ya tenemos). Lo que hacemos es que tomamos un subconjunto
# aleatorio de índices (ciudades) de la primera ruta papá (o mamá) y llenamos
# lo que falta de la ruta con los índices de la segunda ruta papá (o mamá) sin
# que incluya a los primeros índices seleccionados.


def breed(parent1, parent2):
    # Hacemos lo que se explica arriba
    child = [] # inicializamos al hijo
    childP1 = [] # inicializamos la primera parte (selección aleatoria inicial)
    childP2 = [] # inicializamos la segunda parte
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB) # de dónde
    endGene = max(geneA, geneB) # a dónde vamos a hacer la selección inicial

    for i in range(startGene, endGene):
        childP1.append(parent1[i]) # Tomamos el subconjunto del padre 1
        
    childP2 = [item for item in parent2 if item not in childP1] # lo que le
    # vamos a pegar del padre 2
    child = childP1 + childP2 # el hijo final
    return child

# Pero esto solo lo hace para dos padres y produce un solo hijo, necesitamos
# hacer esto más veces

def breedPopulation(matingpool, eliteSize):
    children = [] # vector de los hijos
    length = len(matingpool) - eliteSize # pero no vamos a cambiar las mejores
    # rutas que ya habíamos identificado, esas nos gustaron
    pool = random.sample(matingpool, len(matingpool)) # elegimos al azar
    # cuáles van a ser los papás (como en la edad media)
    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1]) # hacemos bebés, ooops
        children.append(child)
    return children


################################################
################################################
# Sexto: mutamos. Tal vez las mejores rutas seleccionadas antes sí son buenas,
# pero no las mejores, hay que considerar otras rutas que estamos eliminando
# en los primeros pasos porque a primera vista no fueron dignas de seguir. 
# Para esto, intercambiamos o mutamos ciudades de orden. Es decir, le asignamos
# una probabilidad "baja" de que dos ciudades intercambien lugares en nuestra ruta
    

def mutate(individual, mutationRate):
    # mutationRate es esta probabilidad "baja"
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2 # las cambiamos de lugar
            individual[swapWith] = city1
    return individual

# Pero otra vez, tenemos que hacer esto para toda la población no para solo
# una ruta. Spice it up
    

def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate) # Muteamos todos (o no)
        mutatedPop.append(mutatedInd) 
    return mutatedPop


################################################
################################################
# Séptimo: obviamente hay que repetir esto "varias" veces, no nos serviría     
# de mucho hacerlo solo una vez.
# Creamos la siguiente generación de rutas a partir de una generación actual,
# la tasa de "buenas" rutas con las que nos queremos quedar y la probabilidad
# en la que intercambiamos las ciudades (punto sexto de arriba).
def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

################################################
################################################
# Octavo: definimos nuestro algoritmo genético con lo que hicimos en las 262 
# líneas de código arriba

# Necesita la población inicial, su tamaño, la tasa de "buenas" rutas con 
# las que nos queremos quedar y la probabilidad en la que intercambiamos las
# ciudades y la cantidad de generaciones que queremos crear.
def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute







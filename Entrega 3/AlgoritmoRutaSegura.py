import heapq
import pandas as pd
import gmplot
from collections import deque

def crearGrafo(datos):
    origin_unique = datos["origin"].unique()
    GrafoMapa = dict()
    for i in origin_unique:
        Grafito = dict()
        GrafoMapa[i] = Grafito
    for j in range(len(datos)):
        if datos.iloc[j]["oneway"] is True:
            GrafoMapa[datos.iloc[j]["origin"]][datos.iloc[j]["destination"]] = (datos.iloc[j]["harassmentRisk"],datos.iloc[j]["length"])
            GrafoMapa[datos.iloc[j]["destination"]][datos.iloc[j]["origin"]] = (datos.iloc[j]["harassmentRisk"],datos.iloc[j]["length"])
        else:
            GrafoMapa[datos.iloc[j]["origin"]][datos.iloc[j]["destination"]] = (datos.iloc[j]["harassmentRisk"],datos.iloc[j]["length"])

    return GrafoMapa

def Shortest_path_Dijkstra1(Grafo, Origin_vertex, Destination_vertex):
    weights = {vertex: [float('inf'), ""] for vertex in Grafo}
    weights[Origin_vertex][0] = 0
    weights[Origin_vertex][1] = None

    Posibles_ways = [(0, Origin_vertex, 0, 0)]
    
    while len(Posibles_ways) > 0:

      Combined_actual, Vertex_actual, Distance_actual, Risk_actual = heapq.heappop(Posibles_ways)
      
      if Vertex_actual == Destination_vertex:
        pila = deque()
        father = Destination_vertex
        pila.append(father)
        while father is not Origin_vertex:
          father = weights[father][1]
          pila.append(father)
        print("Riesgo promedio: " + str(Risk_actual/(len(pila)-1)) +"\nDistancia acumulada de: "+ str(Distance_actual))
        return pila

      if Combined_actual > weights[Vertex_actual][0]:
        continue

      for Adyacente, Risk in Grafo[Vertex_actual].items():
        Comb = Combined_actual + (Risk[0]*Risk[1])
        Distancia = Distance_actual + Risk[1]
        Riesgo = Risk_actual + Risk[0]
        try:
          if Comb < weights[Adyacente][0]:
            weights[Adyacente][0] = Comb
            weights[Adyacente][1] = Vertex_actual
            heapq.heappush(Posibles_ways, (Comb, Adyacente, Distancia, Riesgo))
        except KeyError:
          continue


def Shortest_path_Dijkstra2(Grafo, Origin_vertex, Destination_vertex):
    weights = {vertex: [float('inf'), ""] for vertex in Grafo}
    weights[Origin_vertex][0] = 0
    weights[Origin_vertex][1] = None

    Posibles_ways = [(0, Origin_vertex, 0, 0)]
    
    while len(Posibles_ways) > 0:

      Combined_actual, Vertex_actual, Distance_actual, Risk_actual = heapq.heappop(Posibles_ways)
      
      if Vertex_actual == Destination_vertex:
        pila = deque()
        father = Destination_vertex
        pila.append(father)
        while father is not Origin_vertex:
          father = weights[father][1]
          pila.append(father)
        print("Riesgo promedio: " + str(Risk_actual/(len(pila)-1)) +"\nDistancia acumulada de: "+ str(Distance_actual))

        return pila

      if Combined_actual > weights[Vertex_actual][0]:
        continue

      for Adyacente, Risk in Grafo[Vertex_actual].items():
        Comb = Combined_actual + (Risk[0]+Risk[1])
        Distancia = Distance_actual + Risk[1]
        Riesgo = Risk_actual + Risk[0]
        try:
          if Comb < weights[Adyacente][0]:
            weights[Adyacente][0] = Comb
            weights[Adyacente][1] = Vertex_actual
            heapq.heappush(Posibles_ways, (Comb, Adyacente, Distancia, Riesgo))
        except KeyError:
          continue


def Shortest_path_Dijkstra3(Grafo, Origin_vertex, Destination_vertex):
    weights = {vertex: [float('inf'), ""] for vertex in Grafo}
    weights[Origin_vertex][0] = 0
    weights[Origin_vertex][1] = None

    Posibles_ways = [(0, Origin_vertex, 0, 0)]
    
    while len(Posibles_ways) > 0:

      Combined_actual, Vertex_actual, Distance_actual, Risk_actual = heapq.heappop(Posibles_ways)
      
      if Vertex_actual == Destination_vertex:
        pila = deque()
        father = Destination_vertex
        pila.append(father)
        while father is not Origin_vertex:
          father = weights[father][1]
          pila.append(father)
        print("Riesgo promedio: " + str(Risk_actual/(len(pila)-1)) +"\nDistancia acumulada de: "+ str(Distance_actual))
        return pila

      if Combined_actual > weights[Vertex_actual][0]:
        continue

      for Adyacente, Risk in Grafo[Vertex_actual].items():
        Comb = Combined_actual + (Risk[1]**Risk[0])
        Distancia = Distance_actual + Risk[1]
        Riesgo = Risk_actual + Risk[0]
        try:
          if Comb < weights[Adyacente][0]:
            weights[Adyacente][0] = Comb
            weights[Adyacente][1] = Vertex_actual
            heapq.heappush(Posibles_ways, (Comb, Adyacente, Distancia, Riesgo))
        except KeyError:
          continue

      
def crearMapa(recorrido1, recorrido2, recorrido3):
    
  new_path1 = []
  for i in range(len(recorrido1)):
    element = str(recorrido1.pop())
    coma = element.find(",")
    elementy = float(element[1:coma])
    elementx = float(element[coma+1:-1])
    tupla = (elementx, elementy)
    new_path1.append(tupla)
  
  new_path2 = []
  for i in range(len(recorrido2)):
    element = str(recorrido2.pop())
    coma = element.find(",")
    elementy = float(element[1:coma])
    elementx = float(element[coma+1:-1])
    tupla = (elementx, elementy)
    new_path2.append(tupla)
  
  new_path3 = []
  for i in range(len(recorrido3)):
    element = str(recorrido3.pop())
    coma = element.find(",")
    elementy = float(element[1:coma])
    elementx = float(element[coma+1:-1])
    tupla = (elementx, elementy)
    new_path3.append(tupla)
  
  CharminarTopAttractionLats, CharminarTopAttractionLons = zip(*new_path1)
  CharminarTopAttractionLats2, CharminarTopAttractionLons2 = zip(*new_path2)
  CharminarTopAttractionLats3, CharminarTopAttractionLons3 = zip(*new_path3)
  
  myGmap = gmplot.GoogleMapPlotter(6.217, -75.567, 15)  
  
  myGmap.plot(CharminarTopAttractionLats, CharminarTopAttractionLons, 'cornflowerblue', edge_width = 10.0) 
  myGmap.plot(CharminarTopAttractionLats2, CharminarTopAttractionLons2, 'crimson', edge_width = 10.0)
  myGmap.plot(CharminarTopAttractionLats3, CharminarTopAttractionLons3, 'springgreen', edge_width = 10.0)
  
  myGmap.marker(CharminarTopAttractionLats[-1],CharminarTopAttractionLons[-1] , "red", title="Destino")
  myGmap.marker(CharminarTopAttractionLats[0],CharminarTopAttractionLons[0] , "red", title="Origen")
  
  myGmap.draw('C:\\Users\\EQUIPO\\Documents\\Proyecto_Estructura_de_Datos\\mapa_google.html')
  
def main():
    print("Asegurese de que las coordenadas ingresadas estén en el csv de las calles de Medellin.")
    print("Ingrese las coordenadas de origen: ")
    origen = str(input())
    print("Ingrese las coordenadas de destino: ")
    destino = str(input())
    data_frame_ciudad = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=";")
    data_frame_ciudad = data_frame_ciudad.fillna({"harassmentRisk": data_frame_ciudad["harassmentRisk"].mean()})
    Grafobonito = crearGrafo(data_frame_ciudad)
    crearMapa(Shortest_path_Dijkstra1(Grafobonito,origen,destino), Shortest_path_Dijkstra2(Grafobonito,origen,destino), Shortest_path_Dijkstra3(Grafobonito,origen,destino))
main()
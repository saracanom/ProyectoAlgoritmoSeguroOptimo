import heapq
import pandas as pd
import gmplot

print("Asegurese de que las coordenadas ingresadas estén en el csv de las calles de Medellin.")
print("Ingrese las coordenadas de origen: ")
origen = str(input())
print("Ingrese las coordenadas de destino: ")
destino = str(input())
data_frame_ciudad = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=";")
data_frame_ciudad = data_frame_ciudad.fillna({"harassmentRisk": data_frame_ciudad["harassmentRisk"].mean()})

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

Grafobonito = crearGrafo(data_frame_ciudad)

def Shortest_path_Dijkstra(Grafo, Origin_vertex, Destination_vertex):
    weightsandf = {vertex: [float('inf'), ""] for vertex in Grafo}
    weightsandf[Origin_vertex][0] = 0
    weightsandf[Origin_vertex][1] = None

    Posibles_ways = [(0, Origin_vertex)]
    
    while len(Posibles_ways) > 0:

      Risk_actual, Vertex_actual = heapq.heappop(Posibles_ways)
      
      if Vertex_actual == Destination_vertex:
        lista = []
        father = Destination_vertex
        lista.append(father)
        while father is not Origin_vertex:
          father = weightsandf[father][1]
          lista.append(father)
        lista = list(reversed(lista))
        lista.append(Risk_actual)
        return lista

      if Risk_actual > weightsandf[Vertex_actual][0]:
        continue

      for Adyacente, Risk in Grafo[Vertex_actual].items():
        Dist = Risk_actual + (Risk[0]*Risk[1])
        try:
          if Dist < weightsandf[Adyacente][0]:
            weightsandf[Adyacente][0] = Dist
            weightsandf[Adyacente][1] = Vertex_actual
            heapq.heappush(Posibles_ways, (Dist, Adyacente))
        except KeyError:
          continue


def crearMapa(recorrido):
  new_path = []
  for i in range(len(recorrido)-1):
    coma = recorrido[i].find(",")
    elementy = float(recorrido[i][1:coma])
    elementx = float(recorrido[i][coma+1:-1])
    tupla = (elementx, elementy)
    new_path.append(tupla)
  CharminarTopAttractionLats, CharminarTopAttractionLons = zip(*new_path)
  myGmap = gmplot.GoogleMapPlotter(6.217, -75.567, 15)  
  myGmap.scatter(CharminarTopAttractionLats, CharminarTopAttractionLons, '#FF0000', size = 0, marker = False )  
  myGmap.plot(CharminarTopAttractionLats, CharminarTopAttractionLons, 'cornflowerblue', edge_width = 10.0)  
  myGmap.marker(CharminarTopAttractionLats[-1],CharminarTopAttractionLons[-1] , "red", title="Destino")
  myGmap.marker(CharminarTopAttractionLats[0],CharminarTopAttractionLons[0] , "red", title="Origen")
  myGmap.draw('C:\\Users\\EQUIPO\\Documents\\Proyecto_Estructura_de_Datos\\mapa_google.html')

crearMapa(Shortest_path_Dijkstra(Grafobonito,origen,destino))
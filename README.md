# Práctica_1 GraphSearch
Práctica 1 de Fundamentos de los Sistemas Inteligentes curso 2018/19.
Implementa los métodos de búsqueda "Ramificación y Acotación" y "Ramificación y Acotación con Subestimación". Se tiene como problema un grafo de las ciudades de Rumanía.

Se ha usado un código base proporcionado por la asignatura FSI(ULPGC).<http://cayetanoguerra.github.io/cayetanoguerra.github.io/ia/search/code.zip> 

  Este código base nos proporciona un metodo denominado graph_search en el que podemos comprobar si el nodo es objetivo o no, actuando de diferente forma en casa caso. Si se trata del nodo objetivo, tenemos un contador que imprimiremos e indicará la cantidad de nodos visitados, en caso contrario, este nodo sera expandido, añadiendo sus hijos a una lista y continuando la exploración. 
La práctica se divide en dos partes. Aunque ambas son prácticamente iguales a excepcion de un pequeño detalle que provocará que los nodos visitados sean diferentes. Ambos metodos gestionan una lista de nodos que se ordenan dependiendo a cual de los 2 métodos nos refiramos(se detallará a continuación). 

### Ramificación y acotación -> Búsqueda no informada
  En este tipo de búsqueda los nodos de la lista abierta se ordenan segun el coste acumulado de cada trayectoria parcial. Siendo la de menor coste las que iran expandiendose primero.

### Ramificación y acotación con subestimación -> Búsqueda informada
  Esta, además de ordenar por el coste acumulado de cada trayectoria parcial, también lo hace con la heurística. Esta heurística se ha determinado como la distancia en linea recta desde el nodo inicial al objetivo. 

Como resultado de la ejecución podemos observar que ambas encontrarán el camino más optimo pero ramificacion y acotacion sin subestimación visitará muchos más nodos que la búsqueda con subestimación.

Link al repositorio git:
https://github.com/carlosmg12/desafio1
Link al video:
https://drive.google.com/file/d/1LkljRetnMdOYsXvCYG1-NtK6QsESJdXk/view?usp=sharing

Explicación del problema

El hexagrama mágico consiste en colocar los 12 primeros números naturales en posiciones estipuladas que conforman un hexágono estrellado de 6 puntas, en este se insertan aleatoriamente los números,ubicándolos de manera aleatoria, sin repetición, con el fin de que todas las diagonales del hexágono sumen 26.
El hexagrama se puede apreciar como una composición de dos triángulos, en dichos triángulos están presentes las posiciones claves, los vértices de estos, que nos pueden guiar de una manera más rápida a una solución, todo esto dependiendo de los números que sean posicionados en dichas posiciones, ya que si dichas posiciones suman una cantidad en especifico el problema se puede llegar a solucionar en cierta forma.
El problema se puede resolver aplicando algoritmos de búsqueda en profundidad, best first implementando heurística, siendo este último el más eficiente.

Modelado del problema en una matriz de 5x7, donde las posiciones que contienen un 1 son los lugares en los que puede ser ingresado un número para la resolución del hexagrama mágico.
[0,0,0,1,0,0,0]
[1,0,1,0,1,0,1]
[0,1,0,0,0,1,0]
[1,0,1,0,1,0,1]
[0,0,0,1,0,0,0]

Solución del problema

Para encontrar una solución de este problema, se parte por la acción de ir colocando los números en orden ascendente en una posición aleatoria dentro del hexagrama mágico vacío (estado Inicial). Para verificar la acción que realiza el algoritmo es válida, se corrobora que la posición en la que se insertó el número, esté dentro de las coordenadas que representan el hexagrama en la matriz inicial, luego, de la misma manera se inserta el siguiente número en cualquiera de las posiciones disponibles, bajo las mismas condiciones.
El estado final cuenta como solución si todas las posiciones de las diagonales están completas con números y estas suman 26.

Se implementa el algoritmo de búsqueda “Best-First” usando como heurística la suma de los números ubicados en los vértices de cada triángulo que componen el hexagrama, como “posiciones clave”, estos vértices se evalúan sumándose, resultando una cifra los más próxima posible a 13, ya que el hecho de posicionar dichos números que sumados dieran esa cifra abría las puertas a encontrar una posible solución de manera más rápida, debido a que son posiciones claves que influyen de mayor forma en las restricciones para completar el desafío.

Cuando implementamos el algoritmo de búsqueda Best-First e integramos el uso de la heurística para su funcionamiento, nos encontramos con el hecho de que esta presentaba errores debido a que nuestro problema no parte de un estado inicial aleatorio, sino que, siempre inicia posicionando primeramente el número 1 en alguna posición válida dentro del hexagrama. Al encontrarse siempre con esta situación, la heurística no era capaz de llevar la evaluación a cabo de manera correcta, ya que no sabíamos cómo evaluar de manera distinta 2 estados que en el principio del desarrollo del problema resultan ser demasiado similares, esto porque no existe prácticamente una diferencia entre posicionar el número 1 en una esquina o hacerlo en otra. Luego de solucionar este problema, gracias a la incorporación de un random que sumará un valor muy mínimo para la diferenciación del valor que asignaba la heurística a cada estado, pudimos encontrarnos con los resultados que conllevaban la aplicación de esta, una gran disminución en la cantidad de iteraciones.


Análisis

Primeramente al utilizar una búsqueda en profundidad, el problema demoraba un tiempo cercano al minuto para lograr encontrar una respuesta, luego el método de búsqueda Best-First y el uso de la heurística provocó que la cantidad de iteraciones disminuyera en aproximadamente un 90%, pasando de alrededor de 500000 iteraciones a 50000 aproximadamente.
Los motivos de esta importante disminución de iteraciones y ahorro de recursos, era debido a que la suma de los números puestos en las posiciones claves del hexagrama, que son los vértices de los triángulos, se convertían en un número lo más cercano posible a 13, permitiendo así, una mayor libertad al resto de posiciones para que al insertar un número en estas se cumpliera el objetivo final que resultaba en la resolución del problema.

Conclusiones

-Buen modelamiento.
-Diferentes tipos de búsquedas conllevan a distintos resultados.
-Implementación de una buena heurística.
-Ahorro de recursos.
Durante este trabajo se aplicaron conocimientos de grafos, algoritmo de búsqueda en grafos, heurísticas y trabajo en equipo.
Podemos concluir que un buen modelamiento del problema junto con el hecho de implementar una buena heurística, que evalúe de una manera correcta cada estado, permite que la cantidad de iteraciones en la búsqueda disminuya de gran manera, por ejemplo al compararla con una simple búsqueda de profundidad, proporcionando así un uso de recursos mucho más óptimo.
Criterios de Evaluación:

–Asistencia:
Nicolás Espinoza: -2
Carlos Méndez: +1
Luis González: +2

–Integración:
Nicolás Espinoza: +1
Carlos Méndez:-2
Luis González:-1

–Responsabilidad:
Nicolás Espinoza: -1
Carlos Méndez: +1
Luis González: +1

–Contribución:
Nicolás Espinoza:+1
Carlos Méndez:+1
Luis González:-1

–Resolución de Conflictos:
Nicolás Espinoza:+1
Carlos Méndez:-1
Luis González:-1

–Aspectos Positivos:
	Nicolás Espinoza: Buena disposición a trabajar en equipo
Carlos Méndez:Buena iniciativa para abordar problemas
Luis González: Buena disposición para trabajar en equipo

–Aspectos a mejorar:
Nicolás Espinoza: Manejo del lenguaje de programación.
Carlos Méndez: Trabajo en equipo.
Luis González: Manejo del tiempo.
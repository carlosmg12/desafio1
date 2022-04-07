from numpy.matrixlib.defmatrix import matrix
import numpy as np
import copy
import random

#formato de los estados
class State:
  def __init__(self, matrix, last_number):
    self.matrix = matrix
    self.last_number = last_number

#matriz "vacía"
initial_state = State([[0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0],\
                       [0,0,0,0,0,0,0]], 0)

class Action:
  def __init__(self,i,j):
    self.i=i; self.j=j

#método para pasar de un estado a otro usando una acción. 
# Observe que este método simplemente coloca en la posición (i,j) de la matriz,
#  el siguiente número y actualiza la variable last_number.
def transition(state, action):
  state.matrix[action.i][action.j] = state.last_number+1
  state.last_number += 1

def is_final_state(state):
  if state.last_number == 12: return True
  return False

#saber si un estado es final, debemos revisar que el último número ingresado sea el 12
def is_final_state(state):
  if state.last_number == 12: return True
  return False

#estado intermedio tenga posibilidades de convertirse en una solución al problema, 
# podemos revisar que tanto sus filas, columnas como diagonales sumen 15 o menos.
def is_valid(state):
  filas=[1,3]
  columnas=[0,2,4,6]
  for i in filas:
    row_sum=0
    for j in columnas:
      row_sum += state.matrix[i][j]
    if row_sum >26: return False
  
  i=1
  j=0
  diag1_sum=0
  while j<=3:
    diag1_sum+=state.matrix[i][j]
    j=j+1
    i=i+1
  if diag1_sum >26: return False

  i=3
  j=0
  diag2_sum=0
  while j<=3:
    diag2_sum+=state.matrix[i][j]
    j=j+1
    i=i-1
  if diag2_sum >26: return False

  i=1
  j=6
  diag3_sum=0
  while j>=3:
    diag3_sum+=state.matrix[i][j]
    j=j-1
    i=i+1
  if diag3_sum >26: return False

  i=3
  j=6
  diag4_sum=0
  while j>=3:
    diag4_sum+=state.matrix[i][j]
    j=j-1
    i=i-1
  if diag4_sum >26: return False

  return True
  
#un método que nos permita obtener todas las acciones válidas a partir de un estado.
#Para ello debemos revisar en la matriz cada casilla faltante y crear la acción correspondiente.}

def get_valid_actions(state):
  valid_actions = []
  coords=[(1,2),(1,4),(2,1),(2,5),(3,2),(3,4),(0,3),(3,0),(3,6),(1,0),(1,6),(4,3)]
  
  for coordenada in coords:
    i,j=coordenada
    if state.matrix[i][j] == 0:
      valid_actions.append(Action(i,j))
  return valid_actions

#implementaremos un algoritmo de búsqueda en profundidad (dfs).
from copy import deepcopy

def dfs(initial_state):
  stack = [deepcopy(initial_state)]
  iters = 0
  while len(stack)>0:
    iters += 1
    state = stack.pop() #retorna y elimina ultimo elemento
    if is_valid(state) == False: continue #se descarta el estado

    if is_final_state(state): return state,iters #se encontró una solución!

    actions = get_valid_actions(state)

    for action in actions:
      new_state = deepcopy(state) #ojo que debemos copiar el estado antes de modificarlo!
      transition(new_state, action)
      stack.append(new_state) #agrega al final
      
#HEURISITICA
def heuristic_eval(state):
  tri_superior=[(0,3),(3,0),(3,6)]
  tri_inferior=[(1,0),(1,6),(4,3)]
  suma_tri_s=0
  suma_tri_i=0
  for n in tri_superior:
    x,y=n
    suma_tri_s+=state.matrix[x][y]
  for n in tri_inferior:
    x,y=n
    suma_tri_i+=state.matrix[x][y]
  suma=(0.00000012364*random.randrange(1,9999999))
  valor=abs(13.0-    (     ((suma_tri_s+suma_tri_i)/2.0)     +suma        )      )
  
  

  #POSICIONES CLAVE
  return valor



from queue import PriorityQueue

#BEST FIRST
def best_first(initial_state, heuristic_eval):
  q = PriorityQueue()

  q.put( (-1, copy.deepcopy(initial_state)) )

  iters = 0
  while not q.empty():
    iters += 1
    elem=q.get()
    state = elem[1] #retorna y elimina el primer elemento

    if is_valid(state) == False: continue #se descarta el estado
    if is_final_state(state): return state,iters #se encontró una solución!

    actions = get_valid_actions(state)
    for action in actions:
      new_state = copy.deepcopy(state) #ojo que debemos copiar el estado antes de modificarlo!
      
      transition(new_state,action)
      q.put((heuristic_eval(new_state), new_state)) #agrega al final
      


#MUESTRA LA SOLUCION    
state,iters=dfs(initial_state)
#state,iters=best_first(initial_state, heuristic_eval)
print("iteraciones:", iters)
n=0
while n<5:
  print(state.matrix[n])
  n+=1
#print("solucion",state.matrix)
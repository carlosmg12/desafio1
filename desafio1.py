from numpy.matrixlib.defmatrix import matrix
import numpy as np

#formato de los estados
class State:
  def __init__(self, matrix, last_number):
    self.matrix = matrix
    self.last_number = last_number

#matriz "vacía"
initial_state = State([[-1,-1,1,1,1,-1,-1],\
                       [-1,-1,1,1,1,-1,-1],\
                       [1,1,1,1,1,1,1],\
                       [1,1,1,0,1,1,1],\
                       [1,1,1,1,1,1,1],\
                       [-1,-1,1,1,1,-1,-1],\
                       [-1,-1,1,1,1,-1,-1]], 0)

class Action:
  def __init__(self,i,j):
    self.i=i; self.j=j

  def transition(self, action):
    old_pos = copy.copy(self.empty)
    if action=='up': self.empty[0] -=1
    if action=='down': self.empty[0] +=1
    if action=='left': self.empty[1] -=1
    if action=='right': self.empty[1] +=1

    self.puzzle[old_pos[0]][old_pos[1]] = self.puzzle[self.empty[0]][self.empty[1]]
    self.puzzle[self.empty[0]][self.empty[1]] = 0
    self.moves.append(action)


  def get_valid_actions(self):
    valid_actions = []
    if self.empty[0] > 0:
      valid_actions.append('up')
    if self.empty[0] < self.N-1:
      valid_actions.append('down');
    if self.empty[1] > 0:
      valid_actions.append('left');
    if self.empty[1] < self.N-1:
      valid_actions.append('right');

    return valid_actions
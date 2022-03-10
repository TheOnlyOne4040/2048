values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

import random
import colours as cl
from getkey import getkey, keys

def printboard():
  print("_____________________")
  for i in values:
    print("|",end = "")
    for j in i:
      j = str(j)
      if j == "0":
        j = "    "
      else:
        while len(j) < 4:
          j = " " + j
      print(colourise(j)+j+cl.reset,end = "|")
    print("\n|____|____|____|____|")
  print()

def colourise(x):
  if "2048" in x: return(cl.pink_back)
  elif "1024" in x: return(cl.grey_back)
  elif "512" in x: return(cl.green)
  elif "256" in x: return(cl.yellow)
  elif "128" in x: return(cl.Orange)
  elif "64" in x: return(cl.Red)
  elif "32" in x: return(cl.purple)
  elif "16" in x: return(cl.magenta)
  elif "8" in x: return(cl.cyan)
  elif "4" in x: return(cl.Blue)
  elif "2" in x: return(cl.White)
  else: return("")
  
def placerandom():
  unsatisfied = True
  while unsatisfied:
    rx = random.randint(0,3)
    ry = random.randint(0,3)
    ri = random.randint(1,5)
    
    if values[rx][ry] == 0:
      if ri == 3:
        values[rx][ry] = 4
      else:
        values[rx][ry] = 2
      unsatisfied = False

def mergeUp():
  for i in range(1,4):
    for j in range(0,4):
      if values[i][j] != 0:
        unsatisfied = True
        inc = 1
        while i - inc >= 0 and unsatisfied:
          if values[i-inc][j] == values[i][j]:
            values[i][j] = 0
            values[i-inc][j] *= 2
            unsatisfied = False
          elif values[i-inc][j] != 0 and inc != 1:
            values[(i-inc)+1][j] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          elif values[i-inc][j] != 0 and inc == 1:
            unsatisfied = False
          elif i - inc == 0 and values[i-inc][j] == 0:
            values[0][j] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          inc += 1
  placerandom()

def mergeDown():
  for i in range(2,-1,-1):
    for j in range(0,4):
      if values[i][j] != 0:
        unsatisfied = True
        inc = 1
        while i + inc <= 3 and unsatisfied:
          if values[i+inc][j] == values[i][j]:
            values[i][j] = 0
            values[i+inc][j] *= 2
            unsatisfied = False
          elif values[i+inc][j] != 0 and inc != 1:
            values[(i+inc)-1][j] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          elif values[i+inc][j] != 0 and inc == 1:
            unsatisfied = False
          elif i + inc == 3:
            values[3][j] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          inc += 1
  placerandom()

def mergeLeft():
  for j in range(1,4):
    for i in range(0,4):
      if values[i][j] != 0:
        unsatisfied = True
        inc = 1
        while j - inc >= 0 and unsatisfied:
          if values[i][j-inc] == values[i][j]:
            values[i][j] = 0
            values[i][j-inc] *= 2
            unsatisfied = False
          elif values[i][j-inc] != 0 and inc != 1:
            values[i][(j-inc)+1] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          elif values[i][j-inc] != 0 and inc == 1:
            unsatisfied = False
          elif j - inc == 0 and values[i][j-inc] == 0:
            values[i][0] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          inc += 1
  placerandom()

def mergeRight():
  for j in range(2,-1,-1):
    for i in range(0,4):
      if values[i][j] != 0:
        unsatisfied = True
        inc = 1
        while j + inc <= 3 and unsatisfied:
          if values[i][j+inc] == values[i][j]:
            values[i][j] = 0
            values[i][j+inc] *= 2
            unsatisfied = False
          elif values[i][j+inc] != 0 and inc != 1:
            values[i][(j+inc)-1] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          elif values[i][j+inc] != 0 and inc == 1:
            unsatisfied = False
          elif j + inc == 3 and values[i][j+inc] == 0:
            values[i][3] = values[i][j]
            values[i][j] = 0
            unsatisfied = False
          inc += 1
  placerandom()
          
def mainGameController():
  status = "playing"
  while status == "playing":
    printboard()
    movement = getkey()
    if movement == "q": status = "quit"; break
    elif movement == "w" or movement == keys.UP : mergeUp()
    elif movement == "a" or movement == keys.LEFT: mergeLeft()
    elif movement == "s" or movement == keys.DOWN : mergeDown()
    elif movement == "d" or movement == keys.RIGHT : mergeRight()

    status = getStatus()

  printboard()
  if status == "won":
    print("winner")
  elif status == "lost":
    print("loser")

def getStatus():
  for i in values:
    for j in i:
      if j == 2048: return("won")
      elif j == 0: return("playing")
        
  for i in range(0,3):
     for j in range(0,4):
       if values[i][j] == values[i+1][j]: return("playing")
  for i in range(0,4):
    for j in range(0,3):
       if values[i][j] == values[i][j+1]: return("playing")
    
  
          
if __name__ == "__main__":
  with open ("splashes/welcome.txt", "r") as welcome:
    print(cl.yellow+welcome.read()+cl.reset)
  with open ("splashes/guide.txt", "r") as guide:
    print(cl.bold+guide.read()+cl.reset)
  placerandom()
  placerandom()
  mainGameController()
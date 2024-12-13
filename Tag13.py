import numpy as np

class Button:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Game:
    
    Goal = (0,0)
    A = Button(0,0)
    B = Button(0,0)
    def __init__(self):
        pass
    def __str__(self):
        return f"Goal: {self.Goal} A: {self.A.x},{self.A.y} B: {self.B.x},{self.B.y}"


arr = [Game()]
m = 0
for line in open("Tag13.txt"):
    
    line = line.strip()
    if m == 0:
        x,y =line.split(":")[1].split(",")
        x = int(x.strip().split("+")[1].strip())
        y = int(y.strip().split("+")[1].strip())
        arr[-1].A = Button(x,y)
    elif m == 1:
        x,y =line.split(":")[1].split(",")
        x = int(x.strip().split("+")[1].strip())
        y = int(y.strip().split("+")[1].strip())
        arr[-1].B = Button(x,y)
    elif m == 2:
        x,y =line.split(":")[1].split(",")
        x = int(x.strip().split("=")[1].strip())
        y = int(y.strip().split("=")[1].strip())
        arr[-1].Goal = (x+10000000000000,y+10000000000000)
    else:
        arr.append(Game())
        m = -1
    m += 1


sum = 0
for game in arr:
    
    A = [[game.A.x,game.B.x],[game.A.y,game.B.y]]
    B = [game.Goal[0],game.Goal[1]]
    X = np.linalg.solve(A,B)
    
    is_integer = (X[0]%1<0.0001 or X[0]%1>0.999 ) and (X[1]%1 <0.001 or X[1]%1>0.999)
    # print(X[0]%1,X[1]%1)
    # print(X,is_integer)
    
    if is_integer:
        sum += round(X[0])*3 + round(X[1])

print(sum)
    


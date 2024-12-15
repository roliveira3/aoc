arr = []
startp = (0, 0)
for i,line in enumerate(open("Tag15.txt")):
    line = line.strip()
    arr.append([])
    for j,c in enumerate(line):
        if c == "@":
            startp = (i, j*2)
            arr[-1].append("@")
            arr[-1].append(".")
        elif c == "O":
            arr[-1].append("[")
            arr[-1].append("]")
        else:
            arr[-1].append(c)
            arr[-1].append(c)
    

moves = []

for line in open("Tag15_2.txt"):
    for c in line.strip():
        moves.append(c)

# can be reused for part 2 
def steplr(p, dir):
    elem = arr[p[0]][p[1]]
    newelem = arr[p[0] + dir[0]][p[1] + dir[1]]
    if newelem == "#":
        return False
    elif newelem == '.':
        arr[p[0] + dir[0]][p[1] + dir[1]] = elem
        arr[p[0]][p[1]] = "."
        return True
    else: #newelem == "0":
        moved = steplr((p[0] + dir[0], p[1] + dir[1]), dir)
        if moved:
            arr[p[0] + dir[0]][p[1] + dir[1]] = elem
            arr[p[0]][p[1]] = "."
            return True
        else:
            return False
        

def checkUD(p, dir):
    
    newelem = arr[p[0] + dir[0]][p[1] + dir[1]]
    if newelem == "#":
        return False
    elif newelem == ".":
        return True
    elif newelem == "]":
        return checkUD((p[0] + dir[0], p[1] + dir[1]), dir) and checkUD((p[0] + dir[0], p[1] + dir[1]-1), dir)
    elif newelem == "[":
        return checkUD((p[0] + dir[0], p[1] + dir[1]), dir) and checkUD((p[0] + dir[0], p[1] + dir[1]+1), dir)
    
def moveUD(c, p, dir):
    # differentiate for part 2
    elem = arr[p[0]][p[1]]
    if elem == ".":
        arr[p[0]][p[1]] = c
        return
    elif elem == "#":
        raise Exception("Encountered a wall while moving up/down")
    elif elem == "[":
        arr[p[0]][p[1]] = c
        moveUD("[", (p[0] + dir[0], p[1] + dir[1]), dir)
        moveUD("]", (p[0] + dir[0], p[1] + dir[1]+1), dir)
        arr[p[0]][p[1]+1] = "."
    elif elem == "]":
        arr[p[0]][p[1]] = c
        moveUD("]", (p[0] + dir[0], p[1] + dir[1]), dir)
        moveUD("[", (p[0] + dir[0], p[1] + dir[1]-1), dir)
        arr[p[0]][p[1]-1] = "."



def stepUD(p, dir):
    if(checkUD(p,dir)):
        arr[p[0]][p[1]] = "."
        moveUD("@",(p[0]+dir[0], p[1]+dir[1]),dir)
        return True
    else:
        return False
        
def c_todir(c):
    if c == "^":
        return (-1, 0)
    elif c == "v":
        return (1, 0)
    elif c == "<":
        return (0, -1)
    elif c == ">":
        return (0, 1)

for m in moves:
    dir = c_todir(m)
    # print(startp, dir)
    if dir == (0,-1) or dir == (0,1):
        if(steplr(startp, dir)):
            startp = (startp[0] + dir[0], startp[1] + dir[1])
    else: # dir == (1,0) or dir == (-1,0):
        if(stepUD(startp, dir)):
            startp = (startp[0] + dir[0], startp[1] + dir[1])

    # for line in arr:
    #     print("".join(line))
    
sum = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "[":
            sum += i*100 + j
print(sum)

arr = []
xr = 0
yr = 0
for i, line in enumerate(open("Tag6.txt")):
    arr.append([])
    for j in range(len(line)):
        c = line[j]
        if c == "^":
            xr = i
            yr = j
        if c!="\n":
            arr[i].append(c)

def turnr (x,y):
    if x == 0:
        if y == 1:
            return 1,0
        if y == -1:
            return -1,0
    if y == 0:
        if x == 1:
            return 0,-1
        if x == -1:
            return 0,1
sum = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "^" or arr[i][j]== '#':
            continue
        arr_copy = [row[:] for row in arr]
        arr_copy[i][j] = "#"
      
        visited = [[False]*len(arr) for _ in range(len(arr[0]))]
        
        stepx = -1
        stepy = 0
        stepamount= 0
        prod = len(arr)*len(arr[0])*10
        x=xr
        y=yr
        print(prod)
        print(stepamount)
        while True:
            if(stepamount >= prod):
                sum+=1
                break
            if x<0 or x>=len(arr) or y<0 or y>=len(arr[0]):
                break
            if arr_copy[x][y] != '#':
                visited[x][y] = True
                x = x+stepx
                y = y+stepy
                stepamount+=1
            else:
                x-=stepx
                y-=stepy
                stepx, stepy = turnr(stepx,stepy)
        


print(sum)

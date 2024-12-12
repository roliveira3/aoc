import copy

class Node:
    def __init__(self, id, num):
        self.num = num
        self.id = id
        self.visited = False

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
        
arr = []
for line in open("Tag10.txt"):
    line = line.strip()
    arr.append([])
    for string in line: 
        if string == ".":
            arr[len(arr)-1].append(-1)
            continue
        num = int(string)
        arr[len(arr)-1].append( num)
graph = {}  
for i in range(0, len(arr)):
    c = len(arr[i])
    for j in range(0, len(arr[i])):
        graph[Node(i*c+j, arr[i][j])] = []
        newnum = arr[i][j]+1
        for pos in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newi = i+pos[0]
            newj = j+pos[1]
            if newi>=0 and newi<len(arr) and newj>=0 and newj<len(arr[i]):
                if arr[newi][newj] == newnum:
                    graph[Node(i*c+j, arr[i][j])].append(Node(newi*c+newj, newnum))


def dfs(node, graph, visited):
    if node in visited:
        return 0
    visited.add(node)
    if node.num == 9:
        return 1
    total = 0
    for neighbor in graph.get(node, []):
        total += dfs(neighbor, graph, visited)
    return total

sum = 0            
for key in graph:
    if key.num == 0: 
        visited = set()
        sum += dfs(key, graph, visited)



for row in arr:
    print(*row, sep="\t")

DP = [[-1 for i in range(len(arr[0]))] for j in range( len(arr))]


def trails (i, j, num, DP, arr):
    if num == 9:
        DP[i][j] = 1
        return 1
    
    sum = 0
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    newnum = num+1
    
    for posn in pos:
        newi = i+posn[0]
        newj = j+posn[1]
        if newi>=0 and newi<len(arr) and newj>=0 and newj<len(arr[i]):
         
            if arr[newi][newj] == newnum:
           
                sum += trails(newi,newj,newnum, DP, arr)
    
    return sum
                

sum = 0
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if arr[i][j] == 0:
            sum += trails(i, j, 0, DP, arr)
for row in DP:
    print(*row, sep="\t")
print(sum)

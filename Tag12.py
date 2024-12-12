from collections import defaultdict
arr = []
visited = []
for line in open("Tag12.txt"):
    line = line.strip()
    arr.append ([])
    visited.append([])
    for c in line: 
        arr[-1].append(c)
        visited[-1].append(False)

reg = defaultdict(int)
per = defaultdict(int)
clusters = []

def dfs(i,j, clus):
    clus.append((i,j))
    for pos in [(0,1),(1,0),(-1,0),(0,-1)]:
        newi = i + pos[0]
        newj = j + pos[1]
        if newi<len(arr)  and newi>=0 and newj <len(arr[i]) and newj >= 0 and not visited[newi][newj] and  arr[i][j]== arr[newi][newj]:
            visited[newi][newj] = True
            dfs(newi,newj, clus)
            




for i in range(len(arr)):
    for j in range (len(arr[0])):
        if not visited[i][j]:
            clus = []
            visited[i][j] = True
            dfs(i,j,clus)
            clusters.append(clus)
total_sum = 0
for clus in clusters:
    reg = len(clus)
    peri = 0
    numSide = 0
    for (ip, jp) in [(0,1),(1,0),(-1,0),(0,-1)]:
        sides = set()
        for point in clus:
            if (point[0]+ip, point[1]+jp) not in clus:
                sides.add((point[0]+ip, point[1]+jp))
        for p in sides:
            if not (p[0]+abs(ip)-1,p[1]+abs(jp)-1) in sides:
                numSide +=1
        
        
    
    
    print("b  ", numSide)
    total_sum += numSide*reg
    print("end")
print(total_sum)


        



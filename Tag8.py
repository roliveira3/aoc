
chars = {}
arr = []
for i,line in enumerate(open("Tag8.txt")):
    arr.append([])
    line = line.strip()
    for j,char in enumerate(line):
        arr[i].append(False)

        if char != ".":
            if char not in chars:
                chars[char] = [(i,j)]  
            else:
                chars[char].append((i,j))
print(chars)
print(arr)  

def check(pos1, pos2, arr):
    i, j = pos1
    k, l = pos2

    diffi = i-k
    diffj = j-l

    print("start")
    
    pos = pos1
    while pos[0] >= 0 and pos[0] < len(arr) and pos[1] >= 0 and pos[1] < len(arr[0]):
        arr[pos[0]][pos[1]] = True
        pos = (pos[0]+diffi, pos[1]+diffj)
    pos = pos2
    while pos[0] >= 0 and pos[0] < len(arr) and pos[1] >= 0 and pos[1] < len(arr[0]):
        arr[pos[0]][pos[1]] = True
        pos = (pos[0]-diffi, pos[1]-diffj)
    print("end")
    

for value in chars.values():
    if len(value) > 1:
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                check(value[i], value[j], arr)
sum = 0
for line in arr:
    for b in line:
        if b:
            sum += 1
print(sum)

        

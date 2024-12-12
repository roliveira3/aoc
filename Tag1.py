arr1= []
arr2=[]
for line in open("Tag1.txt"):
    line = line.strip()
    
    a,b = line.split("   ")
    arr1.append(int(a))
    arr2.append(int(b))
arr1.sort()
arr2.sort()
sum = 0
for j in arr1:
    prod = 0
    for k in arr2:
        if j == k:
            prod +=1
    sum += prod*j
print(sum)
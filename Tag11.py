from collections import defaultdict
import math
arr1 = []
for i,line in enumerate(open("Tag11.txt")):
    line = line.strip()
    split = line.split(" ")
    for w in split:
        arr1.append(int(w))

dic = defaultdict(int)
for stone in arr1:
    dic[stone] +=1
print(dic)
sum = 0

   
for i in range(75):
    print(i)
    dicnew = defaultdict(int)
    for num,count in dic.items():
        if num == 0:
            dicnew[1] += count
            continue
        l = int(math.log10(num)) +1
        if l%2 == 0:
            half = 10**(l//2)
            dicnew [num//half] +=count
            dicnew[num%half] += count
        else:
            dicnew[num*2024] += count
    dic = dicnew
print(dic)
sum = 0
for num in dic.values():
    sum+= num
print(sum)
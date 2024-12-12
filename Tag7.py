equations = {}
for line in open("Tag7.txt"):
    line.strip()
    left, right = line.split(":")
    equations[int(left.strip())] = [int(string) for string in right.strip().split(" ")]

sum = 0
def new_op(i,j):
    return i*(10**len(str(j)))+j
for key, value in equations.items():
    
    possible = [value[0]]
    
    for i in range(1, len(value)):
        newval = value[i]
        possible = [x + newval for x in possible]+ [x* newval for x in possible] + [new_op(x,newval) for x in possible]
        possible= [x for x in possible if x <=key]
    if key in possible:
        sum += key
print(sum)


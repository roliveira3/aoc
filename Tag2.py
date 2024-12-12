sum = 0
for line in open("Tag2.txt"):
    line = line.strip()
    print(line)

    arr =  [int(string)for string in line.split(" ")]
    value = arr[0]
    slipup = False
    valid = True
    if abs(value -arr[1])<1 or abs(value -arr[1])>3:
        if slipup:
            valid = False
        slipup = True
    if value <arr[1]:
        value = arr[1]
        for i in range(2,len(arr)):
            if abs(value -arr[i])<1 or abs(value -arr[i])>3:
                if slipup:
                    valid = False
                slipup = True
            elif value <arr[i]:
                value = arr[i]
            else : 
                if slipup:
                    valid = False
                slipup = True

                
    else:
        value = arr[1]
        for i in range(2,len(arr)):
            if abs(value -arr[i])<1 or abs(value -arr[i])>3:
                if slipup:
                    valid = False
                slipup = True
            elif value >arr[i]:
                value = arr[i]
            else : 
                if slipup:
                    valid = False
                
    if valid:
        sum += 1
print(sum)


    
    
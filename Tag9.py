
class block:
    

    def __init__(self, id, length):
        
        self.id = id
        self.length = length
        self.next = None
        self.prev = None

for line in open("Tag9.txt"):
    line = line.strip()

    arr = []
    i = 0
    even = True
    l = None
    prev = None
    first = None
    for j in line:
        
        if even:
            b = block(i, int(j))
            even = False
            i+=1
            if prev is not None:
                prev.next = b
                b.prev = prev
            else:
                first = b
            l = b
            prev = b
        else:
            b = block(-1, int(j))
            even = True
        
            prev.next = b
            b.prev = prev
            l = b
            prev = b
        
    print(first)
    sum = 0

    curr = l

    while curr.prev is not None:
       
        if curr.id == -1:
            curr = curr.prev
            continue
        candidate = first 
        while candidate is not curr: 
            if candidate.id == -1 and candidate.length>= curr.length:
                
                b = block(curr.id, curr.length) 
                
                candidate.length = candidate.length - curr.length
                candidate.prev.next = b
                b.prev = candidate.prev
                b.next = candidate
                candidate.prev = b
                curr.id = -1

                


                break
            
            candidate = candidate.next
        curr = curr.prev

    curr = first 
    idx = 0
    while curr.next != None:
        print( curr.id, "   ", curr.length)
        for _ in range (curr.length):
            if curr.id != -1:
                sum += curr.id*idx
            idx += 1
        curr = curr.next
    # l = 0
    # r = len(arr)-1

    # while l <=r: 
    #     if arr[r] == -1:
    #         r -= 1
    #         continue
    #     if arr[l] != -1:
    #         sum += arr[l]*l
    #         l+=1
    #         continue
    #     tmp = arr[l]
    #     arr[l] = arr[r]
    #     arr[r] = tmp
    print(sum)
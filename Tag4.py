txt = open("Tag4.txt", "r")
lines = txt.readlines()

sum = 0
for i in range (len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'A':
            if i-1>=0 and j-1>=0 and i+1 < len(lines) and j+1<len(lines):
                sum+= lines[i-1][j-1] =='M' and lines[i+1][j+1] =='S' and lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S'
                sum+= lines[i-1][j-1] =='M' and lines[i+1][j+1] =='S' and lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M'
                sum+= lines[i-1][j-1] =='S' and lines[i+1][j+1] =='M' and lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S'
                sum+= lines[i-1][j-1] =='S' and lines[i+1][j+1] =='M' and lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M'
           
for k in [-1,0,1]:
    for l in [-1,0,1]:
         print(k,l)
print(sum)

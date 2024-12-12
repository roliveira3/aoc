import re
mults = []

enabled = True
for line in open("Tag3.txt"):
    line = line.strip()
    print(line)
    m = re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", line)
    
    for t in m:
        print(t)
        if t == "do()":
            enabled = True
        elif t == "don't()":
            enabled = False
        elif re.match(r"mul\(\d{1,3},\d{1,3}\)", t):
            print("match")
            if enabled:
                mults.append(t[4:-1])  # Extract the numbers inside mul()

print(mults)
sum = 0
for mult in mults:
    a, b = mult.split(",")
    sum += int(a) * int(b)
print(sum)
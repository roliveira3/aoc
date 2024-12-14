import numpy as np
xtiles = 101
ytiles = 103

class Robot:
    def __init__(self, x, y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
    def __str__(self):
        return f"Robot: {self.x},{self.y} {self.vx},{self.vy}"
    def move(self):
        if self.vx > 0:
            self.x = (self.x +self.vx)%xtiles
        else :
            if self.x + self.vx < 0:
                self.x = xtiles + (self.vx + self.x)
            else:
                self.x = self.x + self.vx
        
        if self.vy > 0:
            self.y = (self.y +self.vy)%ytiles
        else :
            if self.y + self.vy < 0:
                self.y = ytiles + (self.vy + self.y)
            else:
                self.y = self.y + self.vy
    
    def __hash__(self):
        return hash((self.x, self.y))

robots = []
arr = []
for line in open("Tag14.txt"):
    line = line.strip()
    p,v = line.split(" ")
    x,y = p.split("=")[1].split(",")
    vx,vy = v.split("=")[1].split(",")
    robots.append(Robot(int(x),int(y),int(vx),int(vy)))


i = 0




while True:
    
    if len(set(robots)) == len(robots):
        arr = [["."] * xtiles for _ in range(ytiles)]
        for robot in robots:
            arr[robot.y][robot.x] = 'R'
        s = 0
        for k in range(45,55):
            for l in range(45,55):
                if arr[k][l] == 'R':
                    s += 1
        if s >= 50:
            print("CHRISTMAS FOR ROBOTS  i:",i)
            for row in arr:
                print("".join(row))
        # ensure no overlap


    for robot in robots:
        # if robot.vx == 2 and robot.vy == -3:
        #     print(robot) 
        robot.move()
    i += 1

    

q1 = 0
q2 = 0
q3 = 0
q4 = 0

print("FINALL########################")
for robot in robots:
    print(robot)
for robot in robots:
    if robot.x>=0 and robot.x<xtiles//2 and robot.y>=0 and robot.y<ytiles//2:
        q1 += 1
    elif robot.x>xtiles//2 and robot.x<xtiles and robot.y>=0 and robot.y<ytiles//2:
        q2 += 1
    elif robot.x>=0 and robot.x<xtiles//2 and robot.y>ytiles//2 and robot.y<ytiles:
        q3 += 1
    elif robot.x>xtiles//2 and robot.x<xtiles and robot.y>ytiles//2 and robot.y<ytiles:
        q4 += 1
print(q1,q2,q3,q4)
print(q1*q2*q3*q4)

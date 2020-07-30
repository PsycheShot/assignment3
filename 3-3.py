week = {"mon":0,"tue":1,"wed":2,"thu":3,"fri":4,"sat":5,"sun":6}

sch = [
        [3,3,3,3,3,3,0],
        [2,2,2,2,2,1,0],
        [2,2,2,1,1,0,0]
      ]

inp = input("Enter day: ")
ans = []
for i in range(0,3):
    ans.append(sch[i][week[inp]])
print(ans)
n = int(input("Enter no of elements in array: "))
lst1 = []
lst2 = []
for i in range(0,n):
    lst1.append(int(input()))
for i in range(n):
    lst2.append(int(input()))
res = list(map(lambda a,b: a+b,lst1,lst2))
print(res)
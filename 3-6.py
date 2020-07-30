from functools import reduce
n = int(input("Enter the no of elements: "))
lst=[int(input()) for i in range(n)]

res = reduce(lambda acc,m: acc+m,lst)
print(res)
from functools import reduce
n = int(input("Enter number: "))
lst = [int(input()) for i in range(n)]

res = reduce(lambda acc,num: acc+num ,map(lambda a: a**2,filter(lambda x: x % 2 == 0, lst)))
print(res) 
  
 
 

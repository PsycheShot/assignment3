def bC(n,k):
    result = 1
    if k>n-k:
        k = n-k
    for i in range(k):
        result = result*(n-i)
        result//=(i+1)
    return result
    
n = int(input("enter n: "))

for i in range(n):
    for j in range(i+1):
        print(bC(i,j)," ", end="")
    print()
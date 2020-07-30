st = input("Enter a word: ")
vLst = list(filter(lambda a: a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u',st))
print(vLst)
print(len(vLst))
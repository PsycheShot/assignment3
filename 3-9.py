data = """Comprehensions are a feature of Python which I would really miss if I ever have to leave it
Comprehensions are constructs that allow sequences to be built from other sequences.
Several types of comprehensions are supported in both Python 2 and Python 3"""
words = data.split(" ")
dct = {}
for i in range(len(words)):
    if words[i] not in dct:
        dct[words[i]]=1
    else:
        dct[words[i]]+=1
    
keymax = max(dct,key=dct.get)
for key,value in dct.items():
    if value==dct[keymax]:
        print(f"{key}: {value}")

keymin = min(dct,key = dct.get)
for key,value in dct.items():
    if value==dct[keymin]:
        print(f"{key}:{value}")



data = "how much wood would a woodchuck chuck if the woodchuck could chuck wood"
word = data.split(" ")
l = len(word)
dct = {}
for i in range(0,l):
    if word[i] not in dct:
        dct[word[i]]=1
    else:
        dct[word[i]]+=1
print(len(dct))
print(dct)
Cricket = {"PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"}
Football = { "PKM", "ALN","RMZ","CS", "MCS"}
Badminton ={ "PKM", "ALN", "NV", "KM","RMV"}

st1 = Cricket.intersection(Football).intersection(Badminton)
print(st1)

st2 = Cricket.union(Football).union(Badminton) - Cricket.intersection(Football) - Cricket.intersection(Badminton) - Football.intersection(Badminton)
print(st2)
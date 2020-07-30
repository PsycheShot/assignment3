import csv

with open('coursedata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lst = [row for row in csv_reader]
    uQuali = input("Enter a qualification: ")
    count = 0
    for i in range(0,len(lst)):
        if lst[i]["Qualification"]==uQuali:
            print(lst[i]["Name"])
            count+=1
    if count==0:
        print("NO student available with choosen qualification")
    quali = []
    qualiCount=[]
    for i in range(0,len(lst)):
        if lst[i]["Qualification"] not in quali:
            quali.append(lst[i]["Qualification"])
            qualiCount.append(1)
        else:
            qualiCount[quali.index(lst[i]["Qualification"])]+=1
    for i in range(0,len(qualiCount)):
        print(f"{quali[i]}: {qualiCount[i]}")

    placedCount = 0
    cbutnotP = 0
    notPlaced = 0
    for i in range(0,len(lst)):
        if lst[i]["Placed"]=="Y":
            placedCount+=1
        else:
            notPlaced+=1
        if lst[i]["Placed"]=="N" and lst[i]["Completed"]=="Y":
            cbutnotP+=1

    print(f"No of students placed: {placedCount}\nNo of students with completed degree but not placed: {cbutnotP}\nNo of students not placed: {notPlaced}")

    flag = True
    name = input("Enter a name in capital letters: ")
    for i in range(0,len(lst)):
        if lst[i]["Name"]==name:
            print(lst[i])
            flag = False
    if flag == True:
        print("No such entry exists")

    batch = []

    for i in range(0,len(lst)):
        if lst[i]["Batch"] not in batch:
            batch.append(lst[i]["Batch"])
    bPlaced = [0]*len(batch)
    btotal = [0]*len(batch)
    for i in range(0,len(lst)):
        if lst[i]["Placed"]=="Y":
            bPlaced[batch.index(lst[i]["Batch"])]+=1
        btotal[batch.index(lst[i]["Batch"])]+=1
    bSucess = [(bPlaced[i]/btotal[i])*100 for i in range(0,len(batch))]
    print(bSucess)

    maxP = 0
    idex = 0
    for i in range(0,len(lst)):
        if float(lst[i]["Score"])>maxP:
            maxP=float(lst[i]["Score"])
            idex = i
    print(lst[idex])

    for i in range(0,len(lst)):
        print(lst[i]["Name"])

    for i in range(0,len(lst)):
        print(lst[i]["Name"],end=",")
        print(lst[i]["Qualification"],end=",")
        print(lst[i]["Score"])
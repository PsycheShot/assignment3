data = """
1
What is super class for every class in java?
String
Object
Math
System
Ans:2

#2
Which of the following is not a java.lang.String class method?
trim
length
reverse
split
Ans:3

#3
What is the output of 10 >>  1?
10
5
20
1
Ans:2

#4
Which of following is not true about Java?
Platform Indepent
Uses Byte code
When compile generates.exe file
Java has interfaces
Ans:3

#5
Which of the following is not a valid data types in Java?
int
byte
short
array
Ans:4
"""

qandaLst = data.split("#")

qLst = [qandaLst[i].split("Ans:")[0] for i in range(0,5)]
aLst = [qandaLst[i].split("Ans:")[1] for i in range(0,5)]
uaLst = []
print("Quiz begins now\nType your choice of option from 1 - 4")
for i in range(0,5):
    print(qLst[i])
    option = int(input())
    print()
    uaLst.append(option)

noCorrect = 0
for i in range(0,5):
    if int(aLst[i])==uaLst[i]:
        noCorrect+=1


Result = "Pass"
if noCorrect<=2:
    Result="Fail"

print(f"No of questions correct: {noCorrect}\nNo of questions wrong: {5-noCorrect}\nSecured percentage: {(noCorrect/5)*100}\nResult: {Result}")

    

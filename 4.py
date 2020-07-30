data_dict = {"100":["Krish","xyz@gmail.com","9823"], "101":["Shivam","shiv@gmail.com","9843"],"102":["Anshul","ansh@gmail.com","9856"],"103":["Akshat","ak@gmail.com","9851"]}
chr = None
count = 0
while chr!=6:
    print("---------MAIN MENU--------")
    print("1. ADD\n2. Modify\n3. SHOW ALL\n4. SEARCH\n5. DELETE\n6. EXIT")

    chr = input("Enter choice: ")
    while chr !="6":
        if chr == "1":
            idNo = 100+len(data_dict)
            name = input("Enter the name: ")
            mail = input("Enter mail id: ")
            mobileN = input("Enter mobile No: ")
            data_dict[str(idNo)] = [name,mail,mobileN]
            print("Entry has been added")
            print("7. ADD ANOTHER\n8. BACK TO MAIN MENU\nEnter your choice: ")
            while chr!="7" and chr!="8":
                chr = input()
                if chr!="7" and chr!="8":
                    print("Wrong choice, Try again")
                else:
                    break
            if chr=="7":
                chr = "1"
                continue
            else:
                break
        
        if chr == "3":
            j=0
            for i in range(len(data_dict)):
                if str(100+i) in data_dict:
                    print(data_dict[str(100+i)])
                    j=i
            if count!=0:
                for k in range(1,count+1):
                    if str(100+j+k) in data_dict:
                        print(data_dict[str(100+j+k)])

                
            print("2. WANT TO MODIFY\n8. BACK TO MAIN MENU")
            while chr!="2" and chr!="8":
                chr = input("Enter your choice: ")
                if chr!="2" and chr!="3":
                    print("Wrong choice, Try agian")
                else:
                    break
            
            if chr =="2":
                continue
            else:
                break
        
        if chr == "2":
            ky = input("Enter idNo that you want modify: ")
            if ky not in data_dict:
                print("NO such idNo exists")
                print("3. Do you want look at all contacts?\n 8. OR GO BACK TO MAIN MENU")
                while chr!="3" and chr!="8":
                    chr = input("Enter your choice: ")
                    if chr!="3" and chr!="8":
                        print("Wrong choice, Please try again")
                    else:
                        break
                if chr == "3":
                    continue
                else:
                    break
        
            else:
                name = input("Enter new name: ")
                mail = input("Enter new mail: ")
                mobileN = input("Enter new mobileN: ")
                data_dict[ky] = [name,mail,mobileN]

                print("Your entry has been modified")
                print("2. Do you want to modify another contact\n3. Display all contacts\n8. BACK TO MAIN MENU")
                chr = None
                while chr!="2" and chr!="3" and chr != "8":
                    chr = input("Enter yout choice")
                    if chr!="2"and chr!="3" and chr!="8":
                        print("Wrong choice, Try Again")
                    else:
                        break
                if chr =="2" or chr =="3":
                    continue
                else:
                    break
            

        if chr =="4":
            ky = input("Enter idNo that you want search: ")
            if ky not in data_dict:
                print("NO such idNo exists")
                print("3. Do you want look at all contacts?\n 8. OR GO BACK TO MAIN MENU")
                while chr!="3" and chr!="8":
                    chr = input("Enter your choice: ")
                    if chr!="3" and chr!="8":
                        print("Wrong choice, Please try again")
                    else:
                        break
                if chr == "3":
                    continue
                else:
                    break
            else:
                print(data_dict[ky])
                print("4. Do you want to search another\n8. BACK TO MAIN MENU")
                chr=None
                while chr!="4" and chr!="8":
                    chr = input("Enter your choice: ")
                    if chr!="4" and chr!="8":
                        print("Wrong choice, Please try again")
                    else:
                        break
                if chr == "4":
                    continue
                else:
                    break

        if chr == "5":
            ky = input("Enter idNo that you want delete: ")
            if ky not in data_dict:
                print("NO such idNo exists")
                print("3. Do you want look at all contacts?\n 8. OR GO BACK TO MAIN MENU")
                while chr!="3" and chr!="8":
                    chr = input("Enter your choice: ")
                    if chr!="3" and chr!="8":
                        print("Wrong choice, Please try again")
                    else:
                        break
                if chr == "3":
                    continue
                else:
                    break
            
            else:
                del data_dict[ky]
                count+=1
                print("Your entry has been deleted")
                print("4. DELETE ANOTHER\n8. BACK TO MAIN MENU")
                chr = None
                while chr!="4" and chr!="8":
                    chr = input("Enter your choice: ")
                    if chr!="4" and chr!="8":
                        print("Wrong choice, Try again")
                    else:
                        break
                if chr=="4":
                    continue
                else:
                    break
    
    if chr =="6":
        print("EXITING")
        break




        



        

    


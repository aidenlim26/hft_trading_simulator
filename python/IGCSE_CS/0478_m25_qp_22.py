MemberID = [0]*1000
Name = [[0]*1000,[0]*1000]
programcontinue = True

while programcontinue == True:
    for i in range(1000):
        selection = int(input("Enter 1 to input a new member, 2 to output a list of membership codes and first and last names, and 3 to stop the program: "))
        if selection < 1 or selection > 3:
            print("Your input is invalid, it must be either 1,2,3.")
        elif selection == 1:
            used = False
            NewID = str(input("Please input a new membership code: "))
            if len(NewID) != 6:
                print("The code must be 6 characters long")
            else:
                indexcheck = 1
                while indexcheck != "" and indexcheck != used:
                    if NewID == MemberID[indexcheck]:
                        used = True
                        print("This code has already been used, please try again.")
                    else:
                        MemberID[indexcheck] == NewID
                        Name[indexcheck][0] = str(input("What is your first name?: "))
                        Name[indexcheck][1] = str(input("What is your last name?: "))
                        indexcheck = indexcheck + 1
        elif selection == 2:
            indexout = 1
            while MemberID[indexout] != "":
                print("Membership code: ", MemberID[indexout])
                print("Member first name: ", Name[indexout][0])
                print("Member last name ", Name[indexout][1])
        else:
            programcontinue = False
            exit()
                

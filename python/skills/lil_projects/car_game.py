condition = True
while condition == True:
    command = input("> ")
    if command == "help":
        print("Start - to start car")
        print("Stop - to stop car")
        print("Quit - to quit")

    elif command == "Start":
        print("Start car")
    elif command == "Stop":
        print("Stop car")
    elif command == "Quit":
        break
    else:
        print("I dont understand")
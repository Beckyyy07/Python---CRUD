import employee

while True:
    choice = input(f"Wich actitivity do you want to do? \n 1)Insert \n 2)Update \n 3)Delete? \n 4)EXIT ")
    if (choice == "1"):
        employee.insertFunc()
    elif (choice == "2"):
        employee.updateFunc()
    elif (choice == "3"):
        employee.deleteFunc()
    elif (choice == "4"):
        print("Exiting...")
        break
    else:
        print("Choose a valid option ")
employee = []

def insertFunc():
    name = input ("Inform the employee name ")
    employee.append(name)
    print(employee)

def deleteFunc():
    name = input("Wich employee do you want to delete?")
    employee.remove(name)
    print(employee)
    
def updateFunc():
    choice = int(input("Wich position the employee you want to update is? "))
    employee[choice] = input("New name: ")
    print("Name updated ", employee)
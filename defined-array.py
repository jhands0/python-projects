print("Welcome to the Project Manager: ")
choice = input(str("\nFile Manager = FM \nExit = E \n\nWhat would you like to do: "))
while choice != "E":
    select = input(str("\nCreate Project = CP \nCreate Feature = CF \nDelete Project = DP \nMove Project = MP \nBack = B \n\nWhat would you like to do: "))
    while select != "B":
        if select == "CP":
            print("Creating Project")
        if select == "CF":
            print("Creating Feature")
        if select == "DP":
            print("Deleting Project")
        if select == "MP":
            print("Moving Project")
        select = input(str("\nCreate Project = CP \nCreate Feature = CF \nDelete Project = DP \nMove Project = MP \nQuit = Q \n\nWhat would you like to do: "))
    choice = input(str("\nFile Manager = FM \nExit = E \n\nWhat would you like to do: "))
import requests


No_of_Participants = 0
No_of_Students = 0
No_of_Employees = 0
No_of_Un_Employees = 0
category_check = True
name_check = True
place_check = True

my_dict = {}
total_value = []
name_list = []
place_list = []
category_list = []


d = requests.

while No_of_Participants < 3:

    print("                Welcome to DSIT Seminar")
    print("                -----------------------")

    name_check = True
    while name_check:
        name = str(
            input("Name of Participant                        :"))
        if name.isalpha():     # To check empty or non Alphabet
            name_check = False
            name_list.append(name)
        else:
            print("Name can't be empty or non Alphabet")
            continue

    place_check = True
    while place_check:
        place = str(
            input("Place                                      :"))
        if place.isalpha():       # To check empty or non Alphabet
            place_check = False
            place_list.append(place)
        else:
            print("Place can't be leave empty or non Alphabet..!! ")
            continue

    category_check = True
    while category_check:
        category = str(
            input("Category (S)tudent/(E)mployee/(U)nEmployee :").lower())
        if category == "s":
            No_of_Students += 1
            category_check = False
            category = "Student"
            category_list.append(category)
        elif category == "e":
            No_of_Employees += 1
            category_check = False
            category = "Employee"
            category_list.append(category)
        elif category == "u":
            No_of_Un_Employees += 1
            category_check = False
            category = "Unemployee"
            category_list.append(category)
        else:
            print("Error..!! Please provide valid input..!!")
            continue  # Loop will re-execute if spelling error occurred category

    No_of_Participants += 1
    total_value.append(No_of_Participants)

    my_dict[No_of_Participants] = {"name": name,
                                   "place": place, "category": category}

    print(total_value)
    print(name_list)
    print(place_list)
    print(category_list)

    print("-------------------------------------------------------------")
    print("""
                Data Science In Tamil
                  Anna Salai, Chennai
                Seminar on Data Science
                  E N T R Y  P A S S    
          """)
    print(f"Pass No      : {No_of_Participants}")
    print(f"Name         : {name.upper()}")
    print(f"Place        : {place.title()}")
    print(f"Category     : {category.title()}")
    print("-------------------------------------------------------------")

print("HOUSEFUL")

report = input("Do you want Report <Y/N> :".lower())  # To check overall report

if report == "y":

    print("-------------------------------------------------------------")
    print("""
                    Data Science In Tamil
                    Anna Salai, Chennai
                    Seminar on Data Science
                        R E P O R T   
        """)
    print(f"No of Participan      : {No_of_Participants}")
    print(f"No of Students        : {No_of_Students}")
    print(f"No of Employees       : {No_of_Employees}")
    print(f"No of Un-Employees    : {No_of_Un_Employees}")
    print("-------------------------------------------------------------")
print(my_dict)

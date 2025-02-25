# User-defined function
def Credits(Pass, Defer, Fail, dict1, user_id):
    if Pass + Defer + Fail == 120:
        
        if Pass == 120 and Defer == 0 and Fail == 0:
            pro = 'Progress'
            print(pro)
            Progress.append("*")

        elif Pass == 100 and (Defer in (20, 0)) and (Fail in (0, 20)):
            pro = 'Progress (Module Trailer)'
            print(pro)
            Trailer.append("*")

        elif (Pass in (0, 20, 40, 60, 80)) and (Fail in (0, 20, 40, 60)):
            pro = 'Do not progress - Module Retriever'
            print(pro)
            Retriever.append("*")

        elif (Pass in (40, 20, 0)) and (Defer in (0, 20, 40)) and (Fail in (80, 100, 120)):
            pro = 'Exclude'
            print(pro)
            Exclude.append("*")

    else:
        print("Total Incorrect")
        pro = 'Invalid total credits'

    dict1[user_id] = [pro, Pass, Defer, Fail]

# Creating descriptive names for variables
Progress = []
Trailer = []
Retriever = []
Exclude = []
dict1 = {}

# Looping the program to allow a staff member to predict progression outcomes for multiple students
print()
print("__________Staff Portal___________")

while True:
    try:
        # Get student ID
        while True:
            user_id = input("Enter your student ID: ")
            if user_id[0] == 'w' and len(user_id) == 8:
                break
            else:
                print("Invalid UserID. Please ensure it starts with 'w' and is 8 characters long.")
        
        # Get credits for Pass, Defer, and Fail
        while True:
            try:
                Pass = int(input("Please enter your credits at Pass: "))
                if Pass in (0, 20, 40, 60, 80, 100, 120):
                    break
                else:
                    print("Out of range. Valid values are 0, 20, 40, 60, 80, 100, 120.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        while True:
            try:
                Defer = int(input("Please enter your credits at Defer: "))
                if Defer in (0, 20, 40, 60, 80, 100, 120):
                    break
                else:
                    print("Out of range. Valid values are 0, 20, 40, 60, 80, 100, 120.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        while True:
            try:
                Fail = int(input("Please enter your credits at Fail: "))
                if Fail in (0, 20, 40, 60, 80, 100, 120):
                    break
                else:
                    print("Out of range. Valid values are 0, 20, 40, 60, 80, 100, 120.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        # Call the Credits function
        Credits(Pass, Defer, Fail, dict1, user_id)
        
        # Ask to continue or quit
        print()
        change = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ").lower()
        if change == 'y':
            continue
        elif change == 'q':
            break
        else:
            print("Invalid input, exiting program.")
            break
    except ValueError:
        print("Error, please enter valid data.")
        break

# Display results
print("--" * 30)        
print("Progression Results")
print("--" * 30)
for key, value in dict1.items():
    print(f"{key}: {value[0]} - Pass: {value[1]}, Defer: {value[2]}, Fail: {value[3]}")
print("--" * 30)

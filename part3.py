# user-defined function
def Credits(Pass, Defer, Fail):
    if Pass + Defer + Fail == 120:
        PASS.append(Pass)
        DEFER.append(Defer)
        FAIL.append(Fail)
        
        if Pass == 120 and Defer == 0 and Fail == 0:
            print("Progress")
            Progress.append("*")

        elif Pass == 100 and (Defer in(20, 0)) and (Fail in(0, 20)):
            print("Progress(Module Trailer)")
            Trailer.append("*")

        elif (Pass in (0, 20, 40, 60, 80)) and (Fail in(0, 20, 40, 60)):
            print("Do not progress-module retriever")
            Retriever.append("*")

        elif (Pass in(40, 20, 0)) and (Defer in (0, 20, 40)) and (Fail in(80, 100, 120)):
            print("Exclude")
            Exclude.append("*")

    else:
        print("Total Incorrect")

# Creating descriptive names for variables
Progress = []
Trailer = []
Retriever = []
Exclude = []
PASS = []
DEFER = []
FAIL = []

print()
print("__________Staff Portal___________")
while True:
    while True:
        try:
            # Getting inputs from students
            Pass = int(input("Please enter your credits at Pass: "))  
            if Pass in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
    
    while True:
        try:
            Defer = int(input("Please enter your credits at Defer: "))
            if Defer in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
    
    while True:
        try:
            Fail = int(input("Please enter your credits at Fail: "))
            if Fail in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
    
    # Call the function
    Credits(Pass, Defer, Fail) 

    # Asking to quit or continue and creating histogram
    print()
    print("Would you like to enter another set of data?")
    change = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
    
    if change == "y":
        continue 

    elif change == "q":
        print()            
        print('')
        
        # Writing to text file
        print('-'*10, "TEXT FILE", '-'*10)
        with open("mytextfile", "w") as file:
            for i in range(len(PASS)):
                if PASS[i] == 120:
                    file.write(f"Progress - {PASS[i]},  {DEFER[i]},  {FAIL[i]}\n")
                elif PASS[i] == 100 and (DEFER[i] in (20, 0)) and (FAIL[i] in (0, 20)):
                    file.write(f"Progress (module trailer) - {PASS[i]}, {DEFER[i]}, {FAIL[i]}\n")
                elif (PASS[i] in (80, 60, 40, 0, 20)) and (DEFER[i] in (40, 20, 0, 60, 80, 100, 120)) and (
                        FAIL[i] in (0, 20, 40, 60)):
                    file.write(f"Module retriever - {PASS[i]}, {DEFER[i]},{FAIL[i]}\n")
                elif (PASS[i] in (40, 20, 0)) and (DEFER[i] in (0, 20, 40)) and (FAIL[i] in (80, 100, 120)):
                    file.write(f"Exclude - {PASS[i]}, {DEFER[i]},{FAIL[i]}\n")

        # Reading from the text file
        with open("mytextfile", "r") as file:
            print(file.read())
    
    else:  # Error message for invalid condition
        print("Something went wrong, please check your condition.")
        break
    break

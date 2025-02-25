# User-defined function for determining the progression status
def Credits(Pass, Defer, Fail):
    if Pass + Defer + Fail == 120:
        # Appending credit details to the lists
        PASS.append(Pass)
        DEFER.append(Defer)
        FAIL.append(Fail)

        # Determine progression status and append to corresponding lists
        if Pass == 120 and Defer == 0 and Fail == 0:
            print("Progress")
            Progress.append("*")

        elif Pass == 100 and (Defer in (20, 0)) and (Fail in (0, 20)):
            print("Progress (Module Trailer)")
            Trailer.append("*")

        elif (Pass in (0, 20, 40, 60, 80)) and (Fail in (0, 20, 40, 60)):
            print("Do not progress - Module Retriever")
            Retriever.append("*")

        elif (Pass in (40, 20, 0)) and (Defer in (0, 20, 40)) and (Fail in (80, 100, 120)):
            print("Exclude")
            Exclude.append("*")
    else:
        print("Total Incorrect")

# Initialize lists to store the progression results
Progress, Trailer, Retriever, Exclude = [], [], [], []
PASS, DEFER, FAIL = [], [], []

print("\n__________ Staff Portal __________\n")

# Main loop for the staff portal
while True:
    try:
        # Get user input for credits with validation
        while True:
            try:
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

        # Call the Credits function to process the input values
        Credits(Pass, Defer, Fail)

        # Ask whether to continue or view results
        print("\nWould you like to enter another set of data?")
        change = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()

        if change == "y":
            continue  # Continue for additional data entry
        elif change == "q":
            print("\n--" * 30)
            print("_________ Progression Results _________\n")
            
            # Print the results in a structured format
            for i in range(len(PASS)):
                if PASS[i] == 120:
                    print(f"Progress - {PASS[i]}, {DEFER[i]}, {FAIL[i]}")
                elif PASS[i] == 100 and (DEFER[i] in (20, 0)) and (FAIL[i] in (0, 20)):
                    print(f"Progress (Module Trailer) - {PASS[i]}, {DEFER[i]}, {FAIL[i]}")
                elif (PASS[i] in (80, 60, 40, 0, 20)) and (DEFER[i] in (40, 20, 0, 60, 80, 100, 120)) and (FAIL[i] in (0, 20, 40, 60)):
                    print(f"Module Retriever - {PASS[i]}, {DEFER[i]}, {FAIL[i]}")
                elif (PASS[i] in (40, 20, 0)) and (DEFER[i] in (0, 20, 40)) and (FAIL[i] in (80, 100, 120)):
                    print(f"Exclude - {PASS[i]}, {DEFER[i]}, {FAIL[i]}")

        else:
            # Handle invalid input for continuing the loop
            print("Invalid input, please check your condition.")
            break
        break

    except ValueError:
        # Handle invalid integer input
        print("Integer required")

# Function to get validated input from the user
def get_valid_input(credit_type):
    while True:
        try:
            credit = int(input(f"Please enter your credits at {credit_type}: "))
            if credit in (0, 20, 40, 60, 80, 100, 120):
                return credit
            else:
                print("Out of range. Please enter a valid credit value.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

# Function to determine progression based on credit values
def determine_progression(Pass, Defer, Fail):
    if Pass + Defer + Fail == 120:
        if Pass == 120 and Defer == 0 and Fail == 0:
            print("Progress")
            Progress.append("*")
        elif Pass == 100 and Defer in (0, 20) and Fail in (0, 20):
            print("Progress (Module Trailer)")
            Trailer.append("*")
        elif Pass in (0, 20, 40, 60, 80) and Fail in (0, 20, 40, 60):
            print("Do not progress (Module Retriever)")
            Retriever.append("*")
        elif Pass in (40, 20, 0) and Defer in (0, 20, 40) and Fail in (80, 100, 120):
            print("Exclude")
            Exclude.append("*")
    else:
        print("Total credits incorrect. Should sum to 120.")

# Function to display the histogram of outcomes
def display_histogram():
    print("\n--" * 40)
    print("Histogram\n")
    if Progress:
        print("Progress", len(Progress), "\t:", len(Progress) * "*")
    if Trailer:
        print("Trailer", len(Trailer), "\t:", len(Trailer) * "*")
    if Retriever:
        print("Retriever", len(Retriever), "\t:", len(Retriever) * "*")
    if Exclude:
        print("Exclude", len(Exclude), "\t:", len(Exclude) * "*")
    total_outcomes = len(Progress) + len(Trailer) + len(Retriever) + len(Exclude)
    print(f"\n{total_outcomes} outcomes in total\n")

# Main menu logic
def main():
    global Progress, Trailer, Retriever, Exclude

    # Initialize outcome lists
    Progress = []
    Trailer = []
    Retriever = []
    Exclude = []

    # User menu to choose between student or staff
    menu_choice = int(input("For student type '1' and for staff type '2': "))

    if menu_choice == 1:
        # Student input section
        while True:
            Pass = get_valid_input("Pass")
            Defer = get_valid_input("Defer")
            Fail = get_valid_input("Fail")
            determine_progression(Pass, Defer, Fail)
            break

    elif menu_choice == 2:
        # Staff portal to process multiple students
        print("\n__________Staff Portal___________")
        while True:
            Pass = get_valid_input("Pass")
            Defer = get_valid_input("Defer")
            Fail = get_valid_input("Fail")
            determine_progression(Pass, Defer, Fail)
            print("\nWould you like to enter another set of data? ('y' for yes, 'q' to quit): ")
            change = input().lower()
            if change == 'q':
                display_histogram()
                break
            elif change != 'y':
                print("Invalid input. Please enter 'y' or 'q'.")

    else:
        print("Invalid menu choice. Please enter '1' for student or '2' for staff.")

# Execute the main function
if __name__ == "__main__":
    main()

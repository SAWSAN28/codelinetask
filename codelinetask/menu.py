def print_pattern():
    n = int(input("Enter the number of rows for the  Pattern: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(n):
             for j in range(n-1 *i):
                 print("*" , end=" ")
             print()


def rotate_array():
    n = int(input("Enter the number of elements (n): "))
    k = int(input("Enter the number of steps (k): "))
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

    k = k % n  
    rotated_arr = arr[-k:] + arr[:-k]
    print("Output:", rotated_arr)
    


def help_message():
    print("--- Help ---")
    print("Option 1: Print a pattern with 'n' rows of decreasing asterisks.")
    print("Option 2: Rotate an array of 'n' elements to the right by 'k' steps.")
    print("Option 3: Display this help message.")
    print("Option 4: Exit the program.\n")
    print("Welcome to the Menu-Based Program!")

while True:
    print("Please select an option:")
    print("1. Print Pattern")
    print("2. Rotate Array")
    print("3. Help")
    print("4. Exit")

    option = input("Option: ")

    if option == "1":
        print_pattern()
    elif option == "2":
        rotate_array()
    elif option == "3":
        help_message()
    elif option == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option (1-4).")
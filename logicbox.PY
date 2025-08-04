def show_choices():
    print("I. Right Triangle Pattern")
    print("II. Pyramid Pattern")
    print("III. Left Triangle Pattern")
    print("IV. Numbers (Total, Average, Even Numbers)")

show_choices()

user_choice = input("Enter your choice (I, II, III, or IV): ").upper()

if user_choice == "I":
    print("You selected I. Right Triangle Pattern:")
    rows = 8
    for i in range(1, rows + 1):
        print('*' * i)

elif user_choice == "II":
    print("You selected II. Pyramid Pattern:")
    rows = 5
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

elif user_choice == "III":
    print("You selected III. Left Triangle Pattern:")
    rows = 6
    for i in range(1, rows + 1):
        print('*' * i)

elif user_choice == "IV":
    print("You selected IV. Numbers Calculation:")
    numbers = range(1, 11)
    total = sum(numbers)
    average = total / len(numbers)
    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Total:", total)
    print("Average:", average)
    print("Even Numbers:", even_numbers)

else:
    print("Invalid choice!")
# This program asks users to enter 15 numbers into a list.
# Then, the program displays whether each entered number is odd or even.

print("Hello, the following prompts will ask you to enter 15 numbers.")
numbers_array = []		# This is an empty array that stores the numbers input by the user.		
for i in range(15):		# This loop collects 15 numbers from the user and stores them in the array.
    user_input = int(input("Please enter number " + str(i + 1) + " of 15: "))
    numbers_array.append(user_input)

for number in numbers_array:    # This loop evaluates if each input number is odd or even then displays the results.
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")

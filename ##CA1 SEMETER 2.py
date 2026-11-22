##CA1 SEMETER 2

# Exercises: 
# 1.1: 
# ● Write a program that takes in numbers from the user. Input should terminate when the 
# user enters -1. 
# ● Once -1 has been entered, the program should print out the sum and average of the 
# entered numbers. 

#here we are initializing the numbers that be used of adding and count being set to zero
total = 0.0
count = 0

while True:
    user_entry1 = input("Please enter a number, enter -1 to exit: ")
    try:
        number = float(user_entry1)
    except ValueError:
        print("Invalid entry! Please enter a numeric value.")
        continue

    if number == -1:
        break

    total += number
    count += 1

if count== 0:
    print("No numbers were entered.")
else:
    average = total/ count
    print(f"sum:  {total}")
    print(f"Average: {average}")

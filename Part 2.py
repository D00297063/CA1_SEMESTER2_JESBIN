##CA1 SEMETER 2
# /*** 1.2: 
# ● Takes in two numbers from the user.  
# ● Adds up all the numbers between those the user entered.   
# ● Outputs the result. 
# ●  
# ---Example: If a user enters 3 and 7, then the program should print out 25 (i.e. 3+4+5+6+7).  
# --Your program should still work correctly, even if the user enters the bigger number first (i.e. 7 
# --and then 3).  
# --Commit and push your code: 
# --● When the program takes in the two numbers and adds up all values (but only works with 
# --the small number first).  
# --● When the program takes in the two numbers and adds up all values no matter which 
# --order they are in. 
# *//


num1 = int(input("enter the first number: "))
num2 = int(input("enter the seccond number: "))


start = min(num1, num2)
end = max(num1, num2)

numbers = list(range(start, end + 1))
total  =sum(numbers)
expression = "+".join(str(n) for n in numbers)

print(f"{total}")



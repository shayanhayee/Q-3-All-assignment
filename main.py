# Task 1; Create 1st python code `Hello world` and upload on GitHub

print("Hello world")
print()


# Task 2: Create 2nd Python code on different data types and upload on GitHub

# Integer Data Type Example: Age Verification System
print("Welcome to the age verification system!")
age = int(input("Enter your age:"))  

if age >= 18:
    print("You are eligible for voting") 
    print() 
else:
    print("You are not eligible for voting")  
    print()

# Float Data Type Example: Temperature Checker

print("Welcome to the temperature checker!")

temperature = float(input("Enter the temperature: "))  

if temperature == 36.1 :
    print("You have a healthy temperature")
    print()
elif temperature < 35.5:
    print("You have a Hypothermia (dangerous) temperature")  
    print()
elif temperature > 38.5:
    print("You have a Fever (dangerous) temperature")
    print()
elif temperature > 41.:
    print("You have a Life-threatening temperature")
    print()

# String Data Type Example: Name Length Checker

print("Welcome to the name length checker!")

name = str(input("Enter your name: "))

if len(name) > 12:
    print("You have a long name")
elif len(name) == 12:
    print("you have a perfect name")
else:
    print("You have a short name")
    print()

# Boolean Data Type Example: Simple Login System

print("Welcome to the login system!")

password = input("Enter the password: ")  

if password == "123":
    print("Access granted!")
elif password == "abc":
    print("Access granted!")
else:
    print("Access denied!")
    print()


# Task 3: Create 3rd Python code on following pyhon operators and upload on GitHub
 
        # Arithmetic Operators Example: Simple Calculator 
    print("Welcome to the simple calculator!")

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    operator = input("Enter the operator (+, -, *, /): ")  
    results = 0
def calculator(num1, num2, operator):
    if operator == "+": 
        results = num1 + num2
    elif operator == "-":
        results = num1 - num2
    elif operator == "*":
        results = num1 * num2
    elif operator == "/":
        results = num1 / num2
    else:

        print("Invalid operator")
        print(f"The result is: { results}")   
        print()

        # Comparison Operators Example: Simple Comparison System
        print("Welcome to the simple comparison system!")

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  

    if num1 == num2:
        print("The numbers are equal")
    elif num1 > num2:
        print("The first number is greater")
    elif num1 < num2:
        print("The second number is greater")
    else:
        print("Invalid input")
        print()

        # Logical Operators Example: Simple Logical System
        print("Welcome to the simple logical system!")

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    operator = input("Enter the operator (and, or, not): ")  

    if operator == "and":
        result = num1 and num2
    elif operator == "or":
        result = num1 or num2
    elif operator == "not":
        result = not num1
    else:
        print("Invalid operator")
        print(f"The result is: {result}")
        print()

        # Assignment Operators Example: Simple Assignment System    
        print("Welcome to the simple assignment system!")

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    operator = input("Enter the operator (=, +=, -=, *=, /=): ")  

    if operator == "=":
        result = num1
    elif operator == "+=":
        result = num1 + num2
    elif operator == "-=":  
        result = num1 - num2
    elif operator == "*=":
        result = num1 * num2    
    elif operator == "/=":
        result = num1 / num2
    else:
        print("Invalid operator")
        print(f"The result is: {result}")
        print() 

        # Identity Operators Example: Simple Identity System
        print("Welcome to the simple identity system!")

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    operator = input("Enter the operator (is, is not): ")  

    if operator == "is":
        result = num1 is num2    
    elif operator == "is not":  
        result = num1 is not num2
    else:
        print("Invalid operator")   
        print(f"The result is: {result}")   
        print()     

        # Membership Operators Example: Simple Membership System
        print("Welcome to the simple membership system!")

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    operator = input("Enter the operator (in, not in): ")  

    if operator == "in":
        result = num1 in num2
    elif operator == "not in":
        result = num1 not in num2
    else:
        print("Invalid operator")
        print(f"The result is: {result}")
        print() 

        # Bitwise Operators Example: Simple Bitwise System
        print("Welcome to the simple bitwise system!")  

    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))    
    operator = input("Enter the operator (&, |, ^, ~, <<, >>): ")  

    if operator == "&":
        result = num1 & num2    
    elif operator == "|":
        result = num1 | num2
    elif operator == "^":    
        result = num1 ^ num2
    elif operator == "~":
        result = ~num1    
    elif operator == "<<":
        result = num1 << num2
    elif operator == ">>":
        result = num1 >> num2        
    else:
        print("Invalid operator")
        print(f"The result is: {result}")
        print()             

        
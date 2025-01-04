## Importing Modules
import math
import operator
import threading

## Defining a Dictionary for Operator Mapping
operator_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

## Defining a Function for Calculator Operations
def calculator():
    print("WELCOME TO THE ADVANCED CALCULATOR!")
    
    while True:
        # Displaying Menu Options
        print("\nSELECT AN OPTION:")
        print("1. Basic Arithmetic Operations")
        print("2. Trigonometric Operations")
        print("3. Exponential Operations")
        print("4. Logarithmic Operations")
        print("5. Exit")
        
        # Getting User Input
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            # Basic Arithmetic Operations
            print("\nSELECT AN ARITHMETIC OPERATION:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            
            # Getting User Input
            op_choice = input("Enter your choice (1/2/3/4): ")
            
            # Performing Arithmetic Operations
            if op_choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if op_choice == '1':
                    result = operator_map['+'](num1, num2)
                    print(f"{num1} + {num2} = {result}")
                    
                elif op_choice == '2':
                    result = operator_map['-'](num1, num2)
                    print(f"{num1} - {num2} = {result}")
                    
                elif op_choice == '3':
                    result = operator_map['*'](num1, num2)
                    print(f"{num1} * {num2} = {result}")
                    
                elif op_choice == '4':
                    if num2 != 0:
                        result = operator_map['/'](num1, num2)
                        print(f"{num1} / {num2} = {result}")
                    else:
                        print("Error: Division by zero is not allowed!")
                        
            else:
                print("Invalid choice. Please choose a valid option.")
                
        elif choice == '2':
            # Trigonometric Operations
            print("\nSELECT A TRIGONOMETRIC OPERATION:")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            
            # Getting User Input
            trig_choice = input("Enter your choice (1/2/3): ")
            
            # Performing Trigonometric Operations
            if trig_choice in ['1', '2', '3']:
                angle = float(input("Enter the angle in degrees: "))
                
                if trig_choice == '1':
                    result = math.sin(math.radians(angle))
                    print(f"sin({angle}) = {result}")
                    
                elif trig_choice == '2':
                    result = math.cos(math.radians(angle))
                    print(f"cos({angle}) = {result}")
                    
                elif trig_choice == '3':
                    result = math.tan(math.radians(angle))
                    print(f"tan({angle}) = {result}")
                    
            else:
                print("Invalid choice. Please choose a valid option.")
                
        elif choice == '3':
            # Exponential Operations
            print("\nSELECT AN EXPONENTIAL OPERATION:")
            print("1. Exponentiation")
            print("2. Square Root")
            
            # Getting User Input
            exp_choice = input("Enter your choice (1/2): ")
            
            # Performing Exponential Operations
            if exp_choice in ['1', '2']:
                if exp_choice == '1':
                    base = float(input("Enter the base: "))
                    exponent = float(input("Enter the exponent: "))
                    result = math.pow(base, exponent)
                    print(f"{base} ^ {exponent} = {result}")
                    
                elif exp_choice == '2':
                    num = float(input("Enter a number: "))
                    result = math.sqrt(num)
                    print(f"sqrt({num}) = {result}")
                    
            else:
                print("Invalid choice. Please choose a valid option.")
                
        elif choice == '4':
            # Logarithmic Operations
            print("\nSELECT A LOGARITHMIC OPERATION:")
            print("1. Natural Logarithm")
            print("2. Base-10 Logarithm")
            
            # Getting User Input
            log_choice = input("Enter your choice (1/2): ")
            
            # Performing Logarithmic

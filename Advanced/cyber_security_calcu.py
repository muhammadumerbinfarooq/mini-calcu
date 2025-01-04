import os
import sys
import math
import hashlib
import base64
from cryptography.fernet import Fernet
from datetime import datetime
from collections import deque

class CybersecurityCalculator:
    
    #A secure and feature-rich calculator application with advanced functionalities.
    
    def __init__(self):
        self.key = self.generate_encryption_key()
        self.cipher_suite = Fernet(self.key)

    def generate_encryption_key(self):
        
       #Generates a strong encryption key using the Fernet algorithm.
      
        return Fernet.generate_key()

    def encrypt_input(self, input_data):
        
        #Encrypts the user input using the Fernet cipher.
        
        return self.cipher_suite.encrypt(input_data.encode())

    def decrypt_output(self, output_data):
        
        #Decrypts the calculation output using the Fernet cipher.
        
        return self.cipher_suite.decrypt(output_data).decode()

    def perform_addition(self):
        
        #Performs secure addition operation with error handling.
        
        try:
            a = self.encrypt_input(input("Enter the first number: "))
            b = self.encrypt_input(input("Enter the second number: "))
            c = int(self.decrypt_output(a)) + int(self.decrypt_output(b))
            print(f"The sum of {self.decrypt_output(a)} and {self.decrypt_output(b)} is: {c}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def perform_subtraction(self):
       
        #Performs secure subtraction operation with error handling.
        
        try:
            a = self.encrypt_input(input("Enter the first number: "))
            b = self.encrypt_input(input("Enter the second number: "))
            c = int(self.decrypt_output(a)) - int(self.decrypt_output(b))
            print(f"The difference between {self.decrypt_output(a)} and {self.decrypt_output(b)} is: {c}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def perform_multiplication(self):
        
        #Performs secure multiplication operation with error handling.
       
        try:
            a = self.encrypt_input(input("Enter the first number: "))
            b = self.encrypt_input(input("Enter the second number: "))
            c = int(self.decrypt_output(a)) * int(self.decrypt_output(b))
            print(f"The product of {self.decrypt_output(a)} and {self.decrypt_output(b)} is: {c}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def perform_division(self):
        
      #  Performs secure division operation with error handling.
        
        try:
            a = self.encrypt_input(input("Enter the dividend: "))
            b = self.encrypt_input(input("Enter the divisor: "))
            c = int(self.decrypt_output(a)) / int(self.decrypt_output(b))
            print(f"The quotient of {self.decrypt_output(a)} divided by {self.decrypt_output(b)} is: {c}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def run(self):
        
       # Main entry point of the CybersecurityCalculator application.
        
        print("Welcome to the Cybersecurity Calculator!")
        print("Please select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 1:
                    self.perform_addition()
                elif choice == 2:
                    self.perform_subtraction()
                elif choice == 3:
                    self.perform_multiplication()
                elif choice == 4:
                    self.perform_division()
                elif choice == 5:
                    print("Exiting the Cybersecurity Calculator.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

if __name__ == "__main__":
    calculator = CybersecurityCalculator()
    calculator.run()

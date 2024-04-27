# Program to check if a string contains any special character
# ========================================================\n
# Approach#4:using string.punctuation
# ================================\n
import string

def check_string(s):
    for c in s:
        if c in string.punctuation:
            print("String is not accepted")
            return
    print("String is accepted")


check_string("Geeks$For$Geeks") 
check_string("Geeks For Geeks")  

import random
import string
def password(length,u_case=True,l_case=True,digit=True,s_char=True):
    
    char_pool=""
    if u_case :
        char_pool+=string.ascii_uppercase
    if l_case:
        char_pool+=string.ascii_lowercase
    
    if digit:
        char_pool+=string.digits
    
    if s_char:
        char_pool+=string.punctuation            


    # Generate a random password
    pas = ''.join(random.choice(char_pool) for _ in range(length))
    
    return pas       


print(" Welcome to the password generator ")
length=int(input("Enter length of password "))
x=password(length,u_case=True,l_case=True,digit=True,s_char=True)
print(f"Generated password: {x}")

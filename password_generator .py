import random
import string
import math

def generate_password(length=12, lower_letters=1, upper_letters=1, numbers=1, symbols=1):
    
    # Define characters to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_emoji = [":-)", ":,-)", "8-)", "B-)", "o:-)", ":-D", "}:-)", ";-)", ":-*", ":-p", ":-!", ":-[", ":-]", ":-(", "(TT)", "(=_=)", ">.<", "(+_+)", "'.'", '"."', "(*_*)", "O_o", ":-O", "(@_@)", "(*~*)", "(-.-||)", "(-_-;)", "(~_~;)"]
    
    Included = []
    if lower_letters:
        Included.append(lowercase_letters)
    if upper_letters:
        Included.append(uppercase_letters)
    if numbers:
        Included.append(digits)
    if symbols:
        Included.append(special_emoji)
    
    
    
    if symbols:    
        symbol = random.choice(special_emoji)
        Included.remove(special_emoji)
        pl = length-len(symbol)
    else:
        p1 = length
        symbol = ''
        
    if lower_letters:
        Range = int(pl/(len(Included))) if len(Included)>1 else math.ceil(pl/(len(Included)))
        lower = "".join(random.choice(lowercase_letters) for i in range(Range))
        Included.remove(lowercase_letters)
        pl = length-(len(symbol)+len(lower))
    else:
        p1 = length - len(symbol)
        lower = ""
        
    if upper_letters:
        Range = int(pl/(len(Included))) if len(Included)>1 else math.ceil(pl/(len(Included)))
        upper = "".join(random.choice(uppercase_letters) for i in range(Range))
        Included.remove(uppercase_letters)
        pl = length-(len(symbol)+len(lower)+len(upper))
    else:
        p1 = length-(len(symbol)+len(lower))
        upper = ""
        
    if numbers:
        num = "".join(random.choice(digits) for i in range(length-pl))
    else:
        num = ""
        
    # Generate password using random.choice
    password = upper+lower+symbol+num

    return password

# Test the function
if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    letters_upper = input("Include letters? (If yes enter 1 otherwise 0): ")
    letters_lower = input("Include letters? (If yes enter 1 otherwise 0): ") 
    numbers = input("Include numbers? (If yes enter 1 otherwise 0): ") 
    symbols = input("Include symbols? (If yes enter 1 otherwise 0): ") 
    password = generate_password(length, letters_upper, letters_lower, numbers, symbols)
    print("Generated Password:", password)

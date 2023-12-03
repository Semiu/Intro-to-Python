def is_between_8_and_12_characters(password):
    """
    Checks if the number of characters in the given password is more than or equal to 8, or less than or equal to 12
    params
    ------
    password - string: the provided password value
    returns
    ------
    True if it meets the set criteria
    """
    password_len = len(password) # Gets the number of the characters using Python len method
    if password_len >= 8 and password_len <= 12: # Checks whether or not the number of characters is more than or equal to 8, and less than or equal to 12
        return True

def contains_number_capital_lower_letters(password):
    """
    Checks if a password contains number, capital and lowercase letters.
    params
    ------
    password - string: the provided password value
    returns
    ------
    True if it meets the set criteria
    """
    if any(chr.isdigit() for chr in password): # Checks if any of the character is digit
        if any(chr.isupper() for chr in password): # Checks if any of the character is uppercase
            if any(chr.islower() for chr in password): # Checks if any of the character is lowercase
                return True

def contains_2_capital_or_lower_letters(password):
    """
    Checks if a password contains at least 2 capital or lowercase letters
    params
    ------
    password - string: the provided password value
    returns
    ------
    True if it meets the set criteria
    """
    count = 0
    for chr in password:
        if chr.isupper() or chr.islower():
            count += 1
    
    if count >= 2:
        return True
    
def contains_no_space(password):
    """
    Checks if a password does not contain whitespace
    params
    ------
    password - string: the provided password value
    returns
    ------
    True if it meets the set criteria
    """
    if ' ' not in password:
        return True

def validate_password(password):
    """
    Validates if the provided password meets the following requirements:
    - includes capital and lowercase letters, a number and 8 to 12 characters
    - contains at least 2 capital or lowercase letters
    - contains no space
    params
    ------
    password - string: the provided password value
    returns
    ------
    True if it meets the set criteria
    """
    if is_between_8_and_12_characters(password):
        if contains_number_capital_lower_letters(password):
            if contains_2_capital_or_lower_letters(password):
                if contains_no_space(password):
                    return True


if __name__ == "__main__":
    password_string = input("Please, enter your password: ")
    
    if validate_password(password_string):
        print(f"{password_string} is a valid password.")
    else:
        print(f"{password_string} is not a valid password.")
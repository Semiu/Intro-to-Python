def hash_username(username):
    """
    Gets the hash value of the provided username
    params
    ------
    username - string: the username for login
    returns
    ------
    hashed username
    """
    import hashlib

    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Hash the username
    hash_object.update(username.encode())
    # Get the hex digest of the hash
    hash_username = hash_object.hexdigest()

    return hash_username

def validate_username(hashed_register, hashed_login):
    """
    Checks if the hashed username used for registration is the same hashed username used for the login
    params
    -----
    hashed_register - hash number of the registered username
    hashed_login - has number of the login username
    """
    if hashed_register == hashed_login:
        return True


from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a random encryption key.
    """
    return Fernet.generate_key()

def encrypt_password(password, key):
    """
    Encrypt a password using Fernet symmetric key encryption.
    """
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    """
    Decrypt an encrypted password using Fernet symmetric key decryption.
    """
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def validate_password(encrypted_password, login_password, key):
    """
    """
    decrypted_password = decrypt_password(encrypted_password, key)
    if decrypted_password == login_password:
        return True

if __name__ == "__main__":

    working = True

    while working:

        key = generate_key() # Generate key for  the encryption and decryption

        print(" === Register your username and password === ")
        registered_username = input("Please, enter your username for registration: ")
        hashed_registered_username = hash_username(registered_username)

        registered_password = input("Please, enter your password for registration: ")
        encrypted_password = encrypt_password(registered_password, key)

        print(" === Log in with your username and password === ")
        login_username = input("Please, enter your username for log in: ")
        hashed_login_username = hash_username(login_username)
        login_password = input("Please, enter your password for log in: ")

        if validate_username(hashed_registered_username, hashed_login_username):
            if validate_password(encrypted_password, login_password, key):
                print(" Succesfully logged in.")
            else:
                print(" Either your password or username is not correct.")
        else:
            print(" Either your password or username is not correct.")

        prompt_to_work = int(input("Enter 1 to continue, any other number to exit: "))
        if prompt_to_work == 1:
            working = True
        else:
            working = False
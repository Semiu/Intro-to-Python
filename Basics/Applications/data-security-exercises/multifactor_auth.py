
def get_otp():
    """
    Gets One Time Password
    returns
    -------
    A current OTP
    """
    import pyotp

    # Generate a new secret key for the user
    secret = pyotp.random_base32()

    # Create a TOTP object with the secret key
    totp = pyotp.TOTP(secret)

    # Get the current OTP
    current_otp = totp.now()

    return int(current_otp) # Type cast to integer

def validate_otp(sent_otp, provided_otp):
    """
    Validates if the sent otp is the same as the provided otp
    params
    ------
    sent_otp: OTP sent
    provided_otp: user-provided OTP
    returns
    ------
    True if it meets the set criteria
    """
    if provided_otp == sent_otp:
        return True
    
def is_event_less_than_25_seconds_ago(current_time_get_otp, current_time_verify_otp):
    """
    Checks if the time difference is less than 25 seconds ago.
    Parameters:
    - current_time_get_otp: datetime object representing when the OTP is generated.
    - current_time_verify_otp: datetime object representing when the OTP is verified.
    returns:
    True if it meets the set criteria
    """
    time_difference = current_time_verify_otp - current_time_get_otp
    seconds_difference = time_difference.total_seconds()

    return seconds_difference < 26

if __name__ == "__main__":
    from datetime import datetime

    # Generate the OTP
    sent_otp = get_otp()
    current_time_get_otp = datetime.now()
    print(f"The sent OTP is {sent_otp}") 

    # Get user provided OTP
    provided_otp = int(input("Please, provide the OTP sent to you: "))
    current_time_verify_otp = datetime.now()

    if is_event_less_than_25_seconds_ago(current_time_get_otp, current_time_verify_otp):
        if validate_otp(sent_otp, provided_otp):
            print("Valid OTP. User is verified.")
        else:
            print("Invalid OTP. Authentication failed.")
    else:
        print("The OTP has expired.")

    


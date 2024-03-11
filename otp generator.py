import random

def generate_otp():
    # Generate a random 6-digit OTP
    otp = ''.join(random.choices('0123456789', k=6))
    return otp

# Example usage
otp = generate_otp()
print("Your OTP:", otp)

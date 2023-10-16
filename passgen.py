import secrets

def generate_password():
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if input("Are CAPITAL letters allowed? (Y/N): ").lower() == 'y' else ''
    lower_chars = 'abcdefghijklmnopqrstuvwxyz' if input("Are lowercase letters allowed? (Y/N): ").lower() == 'y' else ''
    digit_chars = '0123456789' if input("Are digits allowed? (Y/N): ").lower() == 'y' else ''
    special_chars = '!@#$%^&*()-_,' if input("Are special characters allowed? (Y/N): ").lower() == 'y' else ''

    allowed_chars = upper_chars + lower_chars + digit_chars + special_chars

    if not allowed_chars:
        print("Error, you must allow at least one set of characters.")
        return

    pass_length = int(input("Enter the desired length of the password: "))
    password = ''.join(secrets.choice(allowed_chars) for _ in range(pass_length))
    
    print(f"Generated Password is: {password}")

if __name__ == '__main__':
    generate_password()

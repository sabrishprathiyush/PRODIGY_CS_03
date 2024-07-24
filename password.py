import string

def check_password_strength(password):
    
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = set(string.punctuation)

    
    if len(password) < min_length:
        return "Password is too short. Minimum length should be {}".format(min_length)

    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    
    strength = 0
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    if strength == 4:
        return "Very strong password"
    elif strength == 3:
        return "Strong password"
    elif strength == 2:
        return "Moderate password"
    elif strength == 1:
        return "Weak password (consider adding more complexity)"
    else:
        return "Very weak password"

# 
password1 = "sab123"
password2 = "sabrishsam23!"
password3 = "p@ssw0rd"

print("Password 1:", check_password_strength(password1))
print("Password 2:", check_password_strength(password2))
print("Password 3:", check_password_strength(password3))

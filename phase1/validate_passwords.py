


def validate_passwords(passwords):
    valid = []
    invalid = []

    
    for password in passwords:
        if password is None:
            invalid.append(password)
            continue
        conditions = [
            len(password) >= 8,
            any(c in "!@#$%^&*()" for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            
        ]
        
        if all(conditions):
            valid.append(password)
        else:
            invalid.append(password)
    return {
    "valid": valid,
    "invalid": invalid
        }
    
        

passwords = ["abc", "Secret1!", "hello123", "Secure@99", "12345678", "No$ym!"]

print(validate_passwords(passwords))

#if all(all([password.isupper(), password.isdigit(), len(password) >= 8, any(password in "!@#$%^&*()" for password in  passwords)]) for password in passwords):  que es eso
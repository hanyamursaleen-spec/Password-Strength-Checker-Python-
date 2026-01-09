print("Enter your password to check its strength:")
password = input(str)

def strength_checker(password:str):
    uppercount = 0
    lowercount = 0
    digitcount = 0
    specialcount = 0

    if len(password) < 8:
        return "Weak"
    else:  
        for i in range(len(password)):
            thischar = password[i]
            if thischar.isupper():
                uppercount += 1
            elif thischar.islower():
                lowercount += 1
            elif thischar.isdigit():
                digitcount += 1 
            else:
                specialcount += 1
        if uppercount >= 3 and lowercount >= 3 and digitcount >= 2 and specialcount >= 1:
            return "Strong"
        elif uppercount >= 1 and lowercount >= 1 and digitcount >= 1:
            return "Moderate"
        elif uppercount >= 0 or lowercount >= 0 or digitcount >= 0:
            return "Weak"
        else:
            return "Weak"
        
print (strength_checker(password))  # Example usage
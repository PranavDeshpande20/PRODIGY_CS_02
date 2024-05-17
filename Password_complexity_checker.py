input_pass = input("Enter password: ")

special = ""'[ @_=+-.;^!#$%^&*()<>?/\|}{~:]'""

def complex_check(user_pass):
    if len(user_pass) < 8:
        print("Password should be atleast 8 characters long.")
    elif not any(char.isupper() for char in user_pass):
        print("Weak Password. Include atleast one uppercase letter, one lowercase letter, one digit and one special character in the password.")
    elif not any(char.islower() for char in user_pass):
        print("Weak Password. Include atleast one uppercase letter, one lowercase letter, one digit and one special character in the password.") 
    elif not any(char.isdigit() for char in user_pass):
        print("Weak Password. Include atleast one uppercase letter, one lowercase letter, one digit and one special character in the password.")
    elif not any(char in special for char in user_pass):
        print("Weak Password. Include atleast one uppercase letter, one lowercase letter, one digit and one special character in the password.")
    else:
        print("Valid Password, Password strength: Strong")
        

complex_check(input_pass)











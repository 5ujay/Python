password = input("Enter a password : " )

if len(password) < 6 :
    print("Password is weak")
elif len(password) <= 10 :
    print("Password in less strong")
elif len(password) > 10 :
    print("Password is strong")
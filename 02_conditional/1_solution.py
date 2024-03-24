age = input("What is your age : ")

age_int = int(age)

if age_int < 13:
    print("You are child")
elif age_int < 20:
    print("You are teenager")
elif age_int < 60:
    print("You are adult")
elif age_int >= 60:
    print("You are senior")
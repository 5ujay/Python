grade =  int(input("Enter Your Marks : "))


if grade > 100 :
    print("Please verify your marks in percentage")
    exit()

if grade >= 90:
    print("Your Grade is A")
elif grade >= 80:
    print("Your Grade is B")
elif grade >= 70:
    print("Your Grade is C")
elif grade >= 60:
    print("Your Grade is D")
elif grade <= 50:
    print("Your Grade is f")

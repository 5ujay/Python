pet = str(input("who is your pet dog/cat : ").lower())
age = int(input("what is your pet age : "))

if (pet == "dog" and age < 2):
    print("Puppy food")
elif pet == "dog":
    print("dog food")

elif (pet == "cat" and age > 5):
    print("senoir cat food")
elif pet == "cat":
    print("cat food")
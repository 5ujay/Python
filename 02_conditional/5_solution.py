print("Tell me your weather (sunny,rainy,snowy) i'll suggest you a work")

weather = str(input("What is your weather :").lower())

if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
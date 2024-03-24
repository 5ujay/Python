fruit = str(input("Enter fruit Name : "))
color = str(input("Enter fruit color : ").lower())

if color == "green":
    print(fruit , "is unripe")
elif color == "yellow" :
    print(fruit , "is ripe")
elif color == "brown":
    print(fruit , "is overripe")

distance = int(input("Enter distance in the KM : "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Use a bike"
elif distance > 15:
    transport = "Use a car"

print(transport)
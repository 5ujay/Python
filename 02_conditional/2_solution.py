age = int(input("Enter your age : "))
day_name = (input("Enter today day: "))

day = str(day_name)

price = 12 if age >= 18 else 8

if day == "wednesday":
   # price = 10 if age >=18 else 6
   # price = price-2
   price -= 2

print("Ticket Price is : $",price)
order_type = str(input("Enter the order type small, medium, large : " ).lower())
extra_shot = str(input("Do you want extra shot yes/no : " ))

if order_type == "small":
    if extra_shot == "Yes":
        print("Order is small coffee with extra shot")
    else:
        print("Order is small coffee")
elif order_type == "medium":
    if extra_shot == "Yes":
        print("Order is medium coffee with extra shot")
    else:
        print("Order is medium coffee")
if order_type == "large":
    if extra_shot == "Yes":
        print("Order is large coffee with extra shot")
    else:
        print("Order is large coffee")
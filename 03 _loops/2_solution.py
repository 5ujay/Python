n = int(input("Enter a no upto which u want the even no. addition : "))

sum_even = 0

for i in range(1,n+1):
    if i % 2 == 0 :
        sum_even += 1

print(sum_even)
n=int(input("enter number:"))
total_sum=0
for i in range(1,n+1):
    total_sum += i**5
print(f"The sum of the series up to{n}^5 is: {total_sum}")
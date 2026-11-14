n = "hello"
for i in n:
    print(i)
for i in range (5,11):
    print (i)
n = int(input("Enter the number whose sum you want to find"))
sum=0

for i in range (1, n+1):
    sum = sum+i 
print("\nsum =", sum)
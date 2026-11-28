# Reverse Order: reverse the digits of a number using a while loop

# Write your code below
num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse of", num, "is", reverse)

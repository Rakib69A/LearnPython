n = input("Enter a text of numbers :")

list = n.split()
sum = 0

for num in list:
    sum += int (num)

print(sum)
numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of numbers :")

for x in text:
    x = x.lower()
    if x>='a' and x<='z':
        numOfLetters +=1
    elif x>='0' and x<='9':
        numOfDigits += 1
    elif x == ' ':
        numOfWords += 1

print("Number of Letters :",numOfLetters)
print("Number of Digit :",numOfDigits)
print("Number of word :",numOfWords+1)

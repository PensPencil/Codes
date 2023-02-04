alphabets,numbers = 0,0
string = input("Enter a string :")
for s in string:
    if s.isnumeric():
        numbers += 1
    elif s.isalpha():
        alphabets +=1
print("Total Letters :",alphabets)
print("Total digits :",numbers)
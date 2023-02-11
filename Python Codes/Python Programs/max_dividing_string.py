def emptylist(str1,str2):
    for i in str1.split(str2):
        if i != '':
            return 0
    return 1

str1 = input("Enter the first string :")
str2 = input("Enter the second string :")
ans = ""
finalans = ""
if (len(str1) <= len(str2)):
    minstr = str1
    maxstr = str2
else:
    minstr = str2
    maxstr = str1
for i in minstr:
    ans = ans + i
    if emptylist(maxstr,ans) == 1 and emptylist(minstr,ans) == 1:
        finalans = ans
if finalans == '':
    print("No string which divides both the string.")
print(finalans)
str1 = input("Enter first string :")
str2 = input("Enter second string :")
ans= ""
if (len(str1) <= len(str2)) and (str1 in str2):
    for i in str1:
        if i not in ans:
            ans = ans + i
else:
    if str2 in str1:
        for i in str2:
            if i not in ans:
                ans = ans + i
print(ans)
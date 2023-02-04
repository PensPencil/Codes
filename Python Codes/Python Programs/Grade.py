n = int(input("Enter Student Number :"))
list=[]
for i in range(5):
    print("Enter Marks for Subject -",i+1," :")
    m = int(input())
    list.append(m)
sum1 = sum(list)/5
print("Student Number :",n)
print("Grade : ",end='')
if sum1 >= 80:
    print("Distinction")
elif sum1 in range(65,80):
    print("Merit")
elif sum1 in range(50,65):
    print("Pass")
else:
    print("Fail")
def grade(list):
    tot = sum(list)/5
    print("Grade :",end='')
    if tot>= 80:
        print("Distinction")
    elif tot in range(65,80):
        print("Merit")
    elif tot in range(50,65):
        print("Pass")
    else:
        print("Fail")
list = []
n = int(input("Enter Number of Students :"))
for i in range(n):
    list.append([])
for i in range(n):
    print("Enter Details for Student -",i+1," :")
    reg = input("Enter Register Number :")
    list[i].append(reg)
    name = input("Enter Name :")
    list[i].append(name)
    dept = input("Enter Department :")
    list[i].append(dept)
    list[i].append([])
    for j in range(5):
        print("Enter Marks for Subject -",j+1," :")
        m = int(input())
        list[i][3].append(m)
print("The Student Details are :")
print()
for i in range(n):
    print("Register Nember - ",list[i][0])
    print("Name - ",list[i][1])
    print("Department - ",list[i][2])
    print("Marks :")
    print()
    for j in range(5):
        print("Subject -",j+1,end=" :")
        print(list[i][3][j])
    print("Total Marks = ",sum(list[i][3]))
    print(grade(list[i][3]))
    print()
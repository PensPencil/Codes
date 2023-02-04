month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
mon = input("Enter name of month :")
if mon not in month:
    print("Invalid Input !!!")
else :
    print("The number of days in ",mon,"is ",days[month.index(mon)])
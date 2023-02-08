neighbors = []
col_default = ["blue","cyan","green","black","magenta","red","white","yellow"]
colours = []
c = int(input("Enter the number of colours :"))
n = int(input("\nEnter the number of states :"))
for i in range(n):
    print("\nEnter neighboring state for state - ",i+1)
    neighbors[i] = list(map(int,input().split()))
count = 0
for i in range(n):
    for x in col_default:
        if x != colours[[j for j in neighbors[count]]]:
            colours[i] = x
            break
        else:
            continue    
print(colours)

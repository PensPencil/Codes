#1.Given a string, find its mirroring image.
def mirror(a):
    rev=a[::-1]
    print(a," | ",rev)
q=input("Enter the word :")
mirror(q)
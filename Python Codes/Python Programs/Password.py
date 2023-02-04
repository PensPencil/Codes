password = input("Enter new password :")
validity = 1
alph1 = ALPH1 = spec_char1 = 0
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPH = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spec_char = ['$','#','@']
if len(password)<6 or len(password)>16:
    validity = 0
for s in password:
    if s in alph:
        alph1+=1
    elif s in ALPH:
        ALPH1+=1
    elif s in spec_char:
        spec_char1+=1
if alph1 == 0 or ALPH1 == 0 or spec_char1 == 0:
    validity = 0
if validity == 0:
    print("Invalid Password")
else:
    print("Valid Password")

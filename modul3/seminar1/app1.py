
cnp = input("Introduceti primele 7 cifre din CNP: ")
if (int(cnp[0]) in [1,2]):
    print("Aveti peste 18 ani")
elif(int(cnp[0]) in [5,6]):
    if(int(cnp[1:3]) >7):
        print("Aveti sub 18 ani")
    else:
        print("Aveti peste 18 ani")
else:
    print("CNP invalid")









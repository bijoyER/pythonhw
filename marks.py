a=int(input("mark:"))
if a<0:
    print("invalid number")
elif a<33:
    print("fail")
elif a<40:
    print("D")
elif a<50:
    print("C")
elif a<60:
    print("B")
elif a<70:
    print("A-")
elif a<80:
    print("A")
elif a<=100:
    print("A+")
else :
    print("Invalid number")
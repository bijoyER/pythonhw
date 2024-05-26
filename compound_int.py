p=float(input("Enter principal ammount:"))
n=float(input("Enter year:"))
r=float(input("Enter rate of interest:"))

interst=p*(1+r/100)**n-p
print("compound interest is:",interst)
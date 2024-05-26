math=float(input("Enter math marks:"))
ph=float(input("Enter math marks:"))
che=float(input("Enter math marks:"))

if (math>=65 and ph>=55 and che>=50) or (math+ph+che>=180)or (math+ph+che>=140):
    print("ELigible of admisson")
else:
    print("Not Eligible for admisson")
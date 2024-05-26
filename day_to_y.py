day=int(input("Enter day:"))

year=day//365
days=day%365

week=days//7
d=days%7
print("years:",year,"weak:",week,"day:",d)

import random
count=0
print("Welcome to time waste")
computer=random.randrange(1,100)
while True:
    user=int(input("guess your number:"))  
    count+=1      
    if user>computer:
        print("high")
    elif user<computer:
        print("low")
    else:
        print("now it's equal.")
        break;
print(count)
        
        
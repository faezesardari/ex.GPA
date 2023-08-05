name = input("enter your name : ") 
family = input("enter your family : ")

score1 = int(input("enter your score1 : "))
score2 = int(input("enter your score2 : "))
score3 = int(input("enter your score3 : "))
GPA = (score1 + score2 + score3)/3

if score1 > 20 or score1 < 0 :
    print("wrong please enter score1 between 0 to 20")
if score2 > 20 or score2 < 0 :
    print("wrong please enter score2 berween 0 to 20 ")
if score3 > 20 or score3 < 0 :
    print("wrong please enter score3 berween 0 to 20 ")
    
else :
        print(GPA)
    
if GPA > 18 :
    print("good")
if GPA >= 10 :
    print("try more ")
if GPA < 10 :
    print("reject")
print("good job")
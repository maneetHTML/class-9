attendance=int(input("enter your attendance percentage :"))
if attendance<75:
    mc=input("Do you have a medical cause. Press Y for yes and press N for no :")
    if mc=="Y" or mc=="y":
        print("you are allowed to write exams")
    else:
        print("you are not allowed to write exams")
else:
        print("you are allowed to write exams")
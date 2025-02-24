print("Press 1. Car Press 2. bike")
vehchoice=int(input("enter Your choice :"))
if vehchoice==1:
    print("press one toyoto press 2 ford")
    carchoice=int(input("enter Your choice :"))
    if carchoice==1:
       print("toyoto selected pay $2000")
    elif carchoice==2:
       print("ford selected pay $1000")
    else:
       print("invaid choice")
elif vehchoice==2:
   print("press one trek press 2 royal enfield")
   bikechoice=int(input("enter Your choice :"))
   if bikechoice==1:
    print("trek selected pay $2000")
   elif bikechoice==2:
    print("royal enfield selected pay $1000")
   else:
    print("invaid choice")
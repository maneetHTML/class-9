uc=int(input("enter the units consumed : "))
if uc<50:
    amt=uc*2.60+25
elif uc>=50 and uc<100:
    amt=uc*3.25+35
elif uc>=100 and uc<200:
    amt=uc*5.26+45
else:
    amt=uc*8.45+75
print("Amount to be paid",amt)
m1=int(input("Enter Your Marks 1 :"))
m2=int(input("Enter Your Marks 2 :"))
m3=int(input("Enter Your Marks 3 :"))

tp=((m1+m2+m3)*100)/300

if(tp>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass",tp)

else:
    print("You are fail,Try next year",tp)
       
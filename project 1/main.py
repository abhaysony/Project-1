import random
'''
snake=1
water=-1
gun=0'''




computer=-random.choice([-1,1,0])
you=input("enter your choice:")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=youdict[you]

print(f"you choose{reversedict[you]}\n computer choose{reversedict[computer]}")



if(computer==you):
    print("draw")
    
else:
     if(computer==-1 and you==1):
       print("you win!")
     elif(computer==-1 and you==0):
       print("you loose!")
     elif(computer==1 and you==-1):
       print("you loose!")
     elif(computer==1 and you==0):
       print("you win!")
     elif(computer==0 and you==-1):
       print("you win!")
     elif(computer==0 and you==1):
       print("you loose!")
     else:
       print("something went wrong")

   
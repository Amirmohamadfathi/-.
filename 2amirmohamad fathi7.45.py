# amirmohamad fathi
# sun. 7:45 ~ 10:00
def Monthley__Payment__(pricipal, annual_interst_rate, duration):

 pricipal = float (pricipal)
 annual_interst_rate= float (annual_interst_rate)
 duration=float (duration)

 number_Monthly_payment =duration*12

 if annual_interst_rate == 0:

    Monthly_Payment = pricipal/number_Monthly_payment
 
 print ("Your Monthly Payment: ", Monthly_Payment)
 
 else :

 Monthly_Rate = ((annual_interst_rate/100)/12)

 phasel = 1+Monthly_Rate

 phase2 = phasel**number_Monthly_payment 

 phase3 = Monthly_Rate*phase2

 phase4 = pricipal*phase3

 phase5 =phase2-1 

 Monthly Payment = phase4/phase5
 print ("Your Monthly Payment: ", Monthly_Payment)

 pricipal = input ("Enter pricipal : ")

 annual interst_rate= input ("Enter annual interst_rate : ")

 duration= input ("Enter duration : ")

 Monthley Payment (pricipal, annual interst_rate, duration)

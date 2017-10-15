hrs= input("enter hours worked ")
rate= input("enter the rate")
hs=float(hrs)
rt=float(rate)
pay=0
if hs>40:
    pay=40*rt+(hs-40)*1.5*rt
else:
    pay=hs*rt
print(pay)

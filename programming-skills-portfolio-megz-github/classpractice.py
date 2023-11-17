"""
sales=float(input("enter sales:")) #enter the sales amount
bonus=0
if sales>50000:
    bonus=500
else:
    bonus=0
print("Your Bonus: "+str(bonus))

temp=float(input("enter current weather: "))
cli=0
if temp < 80:
    cli="nice weather"
else:
    cli="not a nice weather"
print("todays climate:"+str(cli))
"""
earning=float(input("enter current earnings: "))
work_exp=0
if earning > 30000:
    if work_exp>=2:
        print("elegibile for a loan")
    else:
        print("sorry,less work experience:")
else:
    print("earning more than 30000")





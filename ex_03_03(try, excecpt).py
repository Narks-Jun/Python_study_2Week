hrs = input('Enter Hours:')
rate = input('Enter pay for hour:')
try :
    h = float(hrs)
    pfh = float(rate)
except :
    print("Error, Please enter numeric iput")
    quit()

if h > 40 :
    w = 40*pfh+(h-40)*pfh*1.5
else :
    w = h*pfh
print('pay:', w)

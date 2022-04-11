# Total investment
totinvest =22500
# value of each share 
value = 50
#discount on each share 
discount = (float(10)/100)*value
#Market price
mprice =value - discount
#total no.of shares purchased 
no_shares = totinvest/mprice
#total dividend
dividend = float(12)/100*value*no_shares
#rate of return 
retrnpercent = float(dividend)/totinvest*100
print("No.of shares purchased = ",no_shares,)
print("Total dividend = ",dividend,)
print("Rate of return(approx to nearest integer) = ",int(retrnpercent),)
if (no_shares==500 , dividend==3000 , int(retrnpercent) == 13):
    print("Verified")
else :
    print("There is an error")	

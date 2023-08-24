def main():
#  1.  Output a message to identify the program, and a blank line
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    print()

#  2.  Input the cost and the amount of change from user
    cost = float(input("Cost of an item? "))
    amt = float(input("Amount of money given to the cashier? "))
    print()	

#  3.  Calculate the change
    change = float((amt - cost))
    remain = change % 1
    dollar = int(change - remain)
    qrt = remain / .25
    qrt_r = remain % .25
    qrt = int(qrt - qrt_r)
    dme = remain / .1
    dme_r = remain % .1
    dme = int(dme - dme_r)
    nkl = remain / .05
    nkl_r = remain % .05
    nkl = int(nkl - nkl_r)
    pny = remain / .01
    pny_r = remain % .01
    pny = float(pny - pny_r)
    Pny = round(pny)
#-ok-test case 1 input 0.99 _ output Pennies= 1
#-fail-test case 2 input 1.57 _ output $=1, qrt= 1, dme=4, nkl=8, pny=43
# dimes, nickels, and pennies outputs are incorrect
#  4.  Output resulting change 
    print("Change is converted to dollars=", dollar,"Quarters=", qrt,"Dimes=", dme,"Nickels=", nkl,"Pennies=", Pny)
main()
# end of program file
 
#function input employee information
def employee_info():
    employeename = input("Enter the employee's name :   ")
    hours = float(input ("Enter the number of hours worked:  "))
    payrate = float(input("Enter the employee's payrate in dollars per hour:  "))
    taxrate = float(input ("Enter the income tax rate for this employee:  "))
    print (" ")

    return employeename,  hours, payrate, taxrate

#function gross pay
def grosspay(hours, payrate):
    return hours * payrate

#functino net pay
def netpay(taxrate, payrate, hours):
    return (hours * payrate) - ((hours * payrate) * taxrate)

#function tax ammount
def tax_ammount(taxrate, payrate, hours):
    return taxrate * hours * payrate

nextemployee = " "
count = 0
totalhours = 0
totalgrosspay = 0
totalincometax = 0
totalnetpay = 0


while (nextemployee.lower() != "end"):
    
    #main
    if __name__ == "__main__":
        employeename, hours, payrate, taxrate  = employee_info()
        print ("Name:             ", employeename)
        print ("Hours Worked:     ", hours, "Hours")
        print ("Payrate:         $", payrate, "per Hour")
        print ("Income Tax Rate:  ",round(taxrate, 2), "%")
        print ("Gross Pay:       $",round(grosspay(hours, payrate), 2))
        print ("Taxes Withheld:  $",round(tax_ammount(taxrate, payrate, hours), 2))
        print ("Net Pay:         $",round(netpay(taxrate, payrate, hours), 2))
        
        count = count +1         
        totalhours = hours + totalhours
        totalgrosspay = grosspay(hours, payrate) + totalgrosspay
        totalincometax = tax_ammount(taxrate, payrate, hours) + totalincometax
        totalnetpay = netpay(taxrate, payrate, hours) + totalnetpay
    
    print (" ")
    nextemployee = input ("Would you like to enter another employee?  To end type \"end\":   ")
    print (" ")

print (" ")
print ("Total Number of employees: ", count)
print ("Total Hours Worked: ", round(totalhours, 2))
print ("Total Gross Pay: ", round(totalgrosspay, 2)) 
print ("Total Income Tax: ", round(totalincometax, 2))
print ("Total Net Pay: ", round(totalnetpay, 2)) 

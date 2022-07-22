 
#function input employee information
def employee_info():
    employee_name = input("Enter the employee's name :   ")
    hours = float(input ("Enter the number of hours worked:  "))
    payrate = float(input("Enter the employee's payrate in dollars per hour:  "))
    taxrate = float(input ("Enter the income tax rate for this employee:  "))
   
    return employee_name,  hours, payrate, taxrate

#function gross pay
def grosspay(hours, payrate):
    return hours * payrate

#functino net pay
def netpay(taxrate, payrate, hours):
    return (hours * payrate) - ((hours * payrate) * taxrate)

#function tax ammount
def tax_ammount(taxrate, payrate, hours):
    return taxrate * hours * payrate

next_employee = " "
count = 0

while (next_employee.lower() != "end"):
    
    #main
    if __name__ == "__main__":
        employee_name, hours, payrate, taxrate  = employee_info()
        print ("Name:             ", employee_name)
        print ("Hours Worked:     ", hours, "Hours")
        print ("Payrate:         $", payrate, "per Hour")
        print ("Income Tax Rate:  ", taxrate, "%")
        print ("Gross Pay:       $",grosspay(hours, payrate))
        print ("Taxes Withheld:  $",tax_ammount(taxrate, payrate, hours))
        print ("Net Pay:         $",netpay(taxrate, payrate, hours))
        count = count +1 
        
    next_employee = input ("Would you like to enter another employee?  To end type \"end\":   ")

    print ("employee count = ", count)
   
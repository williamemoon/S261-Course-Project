

#function input employee information
def employee_info():
    employee_name = input("Enter the employee's name:   ")
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


    #Create a loop that will get user input by calling various functions until terminated by the user typing “End.”
    #Create a function that will display total number of employees, total hours, total tax, and total net pay.
    #Submit the Python source code file and a Word document that contains a screenshot of input and display for one employee and a screenshot of the display of totals. A minimum of five employees must be entered to receive full credit. Include a 1–2 sentence reflection on the successes and challenges you had with this assignment.






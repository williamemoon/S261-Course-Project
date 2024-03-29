def getemployee_name():
    employee_name = input("Enter the employee's name :   ")
    return employee_name

def date_input():
    start_date = input("Enter the start date (MM/DD/YYYY):  ")
    end_date = input("Enter the end date (MM/DD/YYYY):   ")
    return start_date, end_date

def getemployee_hours():
    employee_hours = float(input ("Enter the number of hours worked:  "))
    return employee_hours

def getemployee_payrate():
    employee_payrate = float(input("Enter the employee's payrate in dollars per hour:  "))
    return employee_payrate

def getemployee_taxrate():
    employee_taxrate = float(input ("Enter the income tax rate for this employee:  "))
    return employee_taxrate

def get_net_gross_tax(employee_hours, employee_taxrate, employee_payrate):
    grosspay = employee_hours * employee_payrate
    tax_ammount = grosspay * employee_taxrate
    netpay = grosspay - tax_ammount
    return grosspay, netpay, tax_ammount

def print_details(pay_detaillist):
    count_emp = 0
    totalhours = 0.00
    totalgrosspay = 0.00
    totalincometax = 0.00
    totalnetpay = 0.00
    for pay_details in pay_detaillist:
        start_date = pay_details[0]
        end_date = pay_details[1]
        employee_name = pay_details[2]
        employee_hours = pay_details[3]
        employee_payrate = pay_details[4]
        employee_taxrate = pay_details[5]
        
        grosspay, tax_ammount, netpay = get_net_gross_tax(employee_hours, employee_taxrate, employee_payrate)
        print (start_date, end_date, employee_name, f"{employee_hours:,.2f}", f"{employee_payrate:,.2f}", f"{grosspay:,.2f}", f"{employee_taxrate:,.1%}", f"{tax_ammount:,.2f}", f"{netpay:,.2f}")
        
        count_emp += 1
        totalhours += employee_hours
        totalgrosspay += grosspay
        totalincometax += tax_ammount
        totalnetpay += netpay
        
        company_totals["employee_count"] = count_emp
        company_totals["totalhours"] = totalhours
        company_totals["totalgrosspay"] = totalgrosspay
        company_totals["totalincometax"] = totalincometax
        company_totals["toatlnetpay"] = totalnetpay

def printcompany_totals(company_totals):
    print (" ")
    print (f'Total Number of Employees: {company_totals["employee_count"]}')
    print (f'Total Hours Worked:        {company_totals["totalhours"]:,.2f}')
    print (f'Total Gross Pay:           {company_totals["totalgrosspay"]:,.2f}')
    print (f'Total Income Tax Withheld: {company_totals["totalincometax"]:,.2f}')
    print (f'Total Net Pay:             {company_totals["toatlnetpay"]:,.2f}')
      
    
if __name__ == "__main__":
    pay_detailslist = []
    company_totals = {}
    while True:
        employee_name = getemployee_name()
        if (employee_name == "end"):
            break
        start_date, end_date = date_input()
        employee_hours = getemployee_hours()
        employee_payrate = getemployee_payrate()
        employee_taxrate = getemployee_taxrate()
        paydetails = [start_date, end_date, employee_name, employee_hours, employee_payrate, employee_taxrate]
        pay_detailslist.append(paydetails)

    print_details(pay_detailslist)
    printcompany_totals(company_totals)




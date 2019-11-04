#  Python 3.6 or higher required (due to use of formatted string literals)
import sys

def main_stage(option):
    if option ==1:
        employee_type = get_input(1,3,"Type of employee salery\n1= weekly, 2= hourly,  3= commission\n")
        employee_info = add_stage(employee_type)
        add_to_file(employee_info)
        show_employee(employee_info)
    elif option == 2:
        try:
            employees = get_from_file()
            for employee in employees:
                show_employee(employee)
        except:
            print("Due to the error indicated above, you will be returning to main menu.")
    else:
        sys.exit()

# 1= weekly salary 2= hourly  3= commission Employee
def add_stage(employee_type):
    first_name = get_input(option_string="Firstname: ", extra_val=2)  # input(": ")
    last_name = get_input(option_string="Lastname: ", extra_val=2)
    ssn = get_input(option_string="SSN: ", extra_val=2)
    employee_info = [first_name,last_name,ssn]
    if employee_type ==1:
        weekly_salary = get_input(option_string = "Weekly salary: ",extra_val = 1)
        employee_info.append(weekly_salary)
        employee_info.insert(0,1)
    elif employee_type ==2:
        hours = get_input(option_string = "Hours worked: ",extra_val = 1)
        hourly_rate =get_input(option_string = "Hourly rate: ",extra_val = 1)
        employee_info.append(hours)
        employee_info.append(hourly_rate)
        employee_info.insert(0,2)
    elif employee_type ==3:
        gross_sales = get_input(option_string = "Gross sales: ",extra_val = 1)
        commission_rate = get_input(option_string = "Commission rate: ",extra_val = 1)
        employee_info.append(gross_sales)
        employee_info.append(commission_rate)
        employee_info.insert(0,3)
    return employee_info

def add_to_file(employee):
    with open('employees.txt', 'a') as filehandle:
        filehandle.write('%s\n' % str(employee))

def get_from_file():
    employees = []
    try:
        with open('employees.txt', 'r') as filehandle:
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentPlace = eval(line[:-1])
                # add item to the list
                employees.append(currentPlace)
        return employees
    except FileNotFoundError:
        print("No existing records were found in the directory.")
    except IOError:
        print("Could not read file")
    except:
        print("Unexpected error has occured")

def show_employee(employee):
    print("\n","*"*7)
    if employee[0] == 1:
        print("Weekly Salary Employee")
    elif employee[0] == 2:
        print("Hourly Employee")
    elif employee[0] == 3:
        print("Commission Employee")
    print(f"First name: {employee[1]}")
    print(f"Last name: {employee[2]}")
    print(f"SSN: {employee[3]}")
    if employee[0] == 1:
        print(f"Weekly Salary: {employee[4]}")
    elif employee[0] == 2:
        print(f"Hours worked: {employee[4]}")
        print(f"Hourly rate: {employee[5]}")
        earning = earning_hourly(employee[4], employee[5])
        print("Earning: ",format(earning, ".2f"))
    elif employee[0] == 3:
        print(f"Gross sales: {employee[4]}")
        print(f"Commission rate: {employee[5]}")
        earning = employee[4] * employee[5]
        print("Earning: ",format(earning, ".2f"))
    print()

def earning_hourly(hours,rate):
    if hours > 40:
        earning = ((hours -40) * (rate * 1.5)) + (40 * rate)
    else:
        earning = hours * rate
    return earning

def get_input(start=0, end=1, option_string = "Enter a value",extra_val = 0):
    while True:
        try:
            choice1 = input(option_string)
            if extra_val ==0:
                choice1 = int(choice1.strip())
            elif extra_val ==1:
                choice1 = float(choice1.strip())
            elif extra_val ==2:
                choice1 = str(choice1.strip())
        except ValueError:
            print('Valid number, please')
            continue
        except:
            print("Something wrong in the input")
            continue
        if extra_val ==0:
            if choice1 == -1:
                sys.exit()
            else:
                if start <= choice1 <= end:
                    break
                else:
                    print(f"Valid range is: {start} to {end}")
        elif extra_val ==1:
            break
        elif extra_val ==2:
            if len(choice1) < 1:
                print("No input detected!")
                continue
            break
    return choice1

def main():
    while True:
        print("Would you like to Add or View")
        option_chosen = get_input(1,2,"Enter the integer: 1 to ADD, 2 to VIEW and -1 to EXIT\n")
        if option_chosen == 1:
            main_stage(1)
        elif option_chosen == 2:
            main_stage(2)

if __name__ =="__main__":
    print("Welcome!")
    main()

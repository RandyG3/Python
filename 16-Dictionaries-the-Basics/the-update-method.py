employee_salaries = {
    "Guido": 100000,
    "James": 500000,
    "Brandon": 900000
}

extra_employee_salaries = {     # This set wins in the 1st update
    "Yukihiro": 1000000,
    "Guido": 333333             # Updated this record
}

# employee_salaries.update(extra_employee_salaries)
extra_employee_salaries.update(employee_salaries)
#
print(employee_salaries)
print(extra_employee_salaries)
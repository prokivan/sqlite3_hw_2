import sqlite3

db = sqlite3.connect('hw.db')
c = db.cursor()

# write a query in SQL to display the first name, last name, department number, and department name for each employee

# c.execute('''SELECT first_name, last_name, employees.department_id, department.department_name FROM employees
# INNER JOIN department ON employees.department_id=department.department_id''')
# d = c.fetchall()
# for i in d:
#     print(i)

# write a query in SQL to display the first and last name, department, city, and state province for each employee

# c.execute('''SELECT first_name,last_name,department.department_name, locations.city, locations.state_province
# FROM ((employees
# INNER JOIN department ON employees.department_id=department.department_id)
# INNER JOIN locations ON department.location_id=locations.location_id)''')
# d = c.fetchall()
# for i in d:
#     print(i)

# write a query in SQL to display the first name, last name, department number, and department name,
# for all employees for departments 80 or 40

# c.execute('''SELECT first_name, last_name, employees.department_id, department.department_name FROM employees
# INNER JOIN department ON employees.department_id=department.department_id
# WHERE department.department_id=40 OR department.department_id=80''')
# d = c.fetchall()
# for i in d:
#     print(i)

# write a query in SQL to display all departments including those where does not have any employee

# c.execute('''SELECT department_name FROM department''')
# d=c.fetchall()
# for i in d:
#     print(d)
# print(d)

# write a query in SQL to display the job title, full name (first and last name ) of the employee,
# and the difference between the maximum salary for the job and the salary of the employee

# c.execute('''SELECT employees.job_id, first_name, last_name,MIN_SALARY.MIN_SALARY-employees.salary
# FROM employees
# INNER JOIN MIN_SALARY ON employees.job_id=MIN_SALARY.job_id''')
# d = c.fetchall()
# for i in d:
#     print(i)

# write a query in SQL to display the job title and the average salary of employees

# c.execute('''SELECT job_id, AVG(salary)
# FROM employees
# NATURAL JOIN MIN_SALARY
# GROUP BY job_id''')
#
# d = c.fetchall()
# for i in d:
#     print(i)


# write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London

# c.execute('''SELECT first_name,last_name, locations.city
# FROM ((employees
# INNER JOIN department ON employees.department_id=department.department_id)
# INNER JOIN locations ON department.location_id=locations.location_id) WHERE locations.city = "London"''')
# d = c.fetchall()
# for i in d:
#     print(i)

# write a query in SQL to display the department name and the number of employees in each department

# c.execute('''SELECT first_name,last_name,department.department_name, locations.city, locations.state_province
# FROM ((employees
# INNER JOIN department ON employees.department_id=department.department_id)
# INNER JOIN locations ON department.location_id=locations.location_id)''')
# d = c.fetchall()
# for i in d:
#     print(i)

# c.execute('''SELECT department.department_name, employees.first_name
# FROM employees
# INNER JOIN department ON department.department_id = employees.department_id''')
# d = c.fetchall()
# for i in d:
#     print(i)

c.execute('''SELECT employees.department_id, department.department_name, COUNT(employees.first_name)
FROM employees
INNER JOIN department ON department.department_id = employees.department_id
GROUP BY department.department_id''')
d = c.fetchall()
for i in d:
    print(i)
print()
c.execute('''SELECT department_id, COUNT(first_name)
FROM employees
GROUP BY department_id''')
d = c.fetchall()
for i in d:
    print(i)
db.commit()
db.close()

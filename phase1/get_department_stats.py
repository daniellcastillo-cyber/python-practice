

def get_department_stats(employees):
    salary_engineering = 0 #sumar salario
    salary_marketing = 0
    salary_hr = 0
    contador_eng = 0   #sumar trabajadores
    contador_mar = 0
    contador_hr = 0
    total_engineering = []
    total_marketing = []
    total_hr = []

    # separar engineering marketing y hr, guardar en listas separadas
    # y agregar un contador para sumar sus salarios
    for employee in employees:
        if employee is None:
            return False
        if employee['department'] == 'engineering':
            contador_eng += 1
            salary_engineering += employee['salary']
            total_engineering.append(employee['name'])
            

        elif employee['department'] == 'marketing':
            contador_mar += 1
            salary_marketing += employee['salary']
            total_marketing.append(employee['name'])
            

        elif employee['department'] == 'hr':
            contador_hr += 1
            salary_hr += employee['salary']
            total_hr.append(employee['salary'])


    return {
    "engineering": {'employees': contador_eng, "average_salary": round(salary_engineering / contador_eng, 2)},
    "marketing": {'employees': contador_mar, "average_salary": round(salary_marketing / contador_mar, 2)},
    "hr": {'employees': contador_hr, "average_salary": round(salary_hr / contador_hr, 2)},
    }
employees = [
    {"name": "ana", "department": "engineering", "salary": 3500},
    {"name": "luis", "department": "marketing", "salary": 2800},
    {"name": "maria", "department": "engineering", "salary": 4200},
    {"name": "Carlos", "department": "marketing", "salary": 3100},
    {"name": "sofia", "department": "engineering", "salary": 3800},
    {"name": "pedro", "department": "hr", "salary": 2600},

]
print(get_department_stats(employees),'\n')
result = get_department_stats(employees)
print(f"engineering: {result['engineering']}\n")
print(f"marketing: {result['marketing']}\n")
print(f"hr: {result['hr']}\n")

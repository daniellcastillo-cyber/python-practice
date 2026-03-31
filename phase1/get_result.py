
def get_results(lista):
    passed = []
    failed = []
    total = 0
    for student in lista:
        if student is None:
            return False
        elif student is not None:
            if student['score'] < 60:
                failed.append(student['name'])
            else:
                passed.append(student['name'])
            
            total = (total + student['score'])
    average = round(total / len(lista), 2)
    print(average)
    return {
            "passed": passed,
            "failed": failed,
            "average": average
            }

students = [
    {"name": "Ana", "score": 45},
    {"name": "Luis", "score": 78},
    {"name": "Maria", "score": 92},
    {"name": "Carlos", "score": 61},
    {"name": "Sofia", "score": 34},
    {"name": "Pedro", "score": 88},
]

result = get_results(students)
        
 
print(result) 
print("Los estudiantes que pasaron son: ", result['passed'])
print('Los estudiantes que perdieron son: ',(result["failed"]))
print('El promedio es de : ', result["average"])   
    

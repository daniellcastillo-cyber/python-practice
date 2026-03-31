
def get_bmi(weight, height):
        imc = round(weight / height ** 2, 2)
        

        if imc < 18.5:
            category = "Underweight"
        
        elif imc >= 18.5 and imc <= 24.9:
            category = "Normal"
        
        elif imc >= 25 and imc <= 29.9:
            category = "Overweight"
        
        else:
            category = "Obese"

        return imc, category


while True:
    try:
        weight = float(input("Enter your weight kg: "))
        height = float(input("Enter your height mt: "))


        if height == 0:
            print('height cannont be zero\n')
            continue
        if weight == 0:
            print("weight cannont be zero\n")
            continue
        bmi, category = get_bmi(weight, height)
        print(f"Your BMI is: {bmi} - {category}")

        break

    except ValueError:
        print("not valid. ")
          
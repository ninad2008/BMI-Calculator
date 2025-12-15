weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi < 24.9:
    print("You have Normal weight")
elif 25 <= bmi < 29.9:
    print("You are Overweight")
else:
    print("You are Obese")
h = int(input("Input your height:"))
w = int(input("Input your weight:"))
he = h * 0.01
BMI = w / (he * he)
if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI <= 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 25:
    print("Normal")
elif 25 <= BMI <=30:
    print("Overweight")
else:
    print("Obese")
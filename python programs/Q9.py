w=int(input("Enter the weight in kg"))
h=float(input("Enter the height in meter"))
bmi=w/(h**h)
print("Nutritional value"'\n')
if (bmi<18.5):
    print("underweight")
elif (bmi>=18.5 and bmi<=24.9):
    print("normal")
elif (bmi>24.9 and bmi<=29.9):
    print("overweight")
elif (bmi>29.9):
    print("Obese")

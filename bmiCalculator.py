"""This is simple BMR Calculator that will take input from the users in terms of their height
and weight and then return their respective BMI Values"""

height = float(input('Enter your height in m: '))  # This takes inputs as height
weight = int(input('Enter your weight in Kg: '))  # This takes input as weight

BMI = (weight / height ** 2)  # This will calculate the BMI

print('As per your Height and Weight your BMR is: ' + str(BMI))

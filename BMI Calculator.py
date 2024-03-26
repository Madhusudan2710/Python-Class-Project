#Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. 
#If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Warning you should convert the result to a whole number.

# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# Output : 26

#Write your code below

height = float(input("enter your height in m: "))
weight = float (input("enter your weight in kg: "))
bmi = round (weight/ (height)**2)
print ("body mass index :",bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi},You have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi},You are obese")
else:
    print(f"Your BMI is {bmi}, You are clinically obese")

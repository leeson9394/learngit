height=input('Enter your height in meter: ')
weight=input('Enter your weight in kilogram: ')
BMI= weight / (height*height)
print'Your BMI is: ', BMI

if BMI <= 18.5:
	print('Under weight')
elif BMI <= 25:
	print('Normal')
elif BMI <= 28:
	print('Over weight')
elif BMI <= 32:
	print('Obese')
else:
	print('Serious obese')	

height=1.8
weight=50
BMI= weight / (height*height)
print(BMI)

if BMI <= 18.5:
	print('light')
elif BMI <= 25:
	print('normal')
elif BMI <= 28:
	print('over weight')
elif BMI <= 32:
	print('obese')
else:
	print('serious obese')	

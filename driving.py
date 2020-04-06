country = input('where are you from?')
age = input('how old are you?')
age = int(age)
if country == 'Taiwan':
	if age >=18:
		print('you can get the driving license!')
	else:
		print('you are not old enough yet!')
elif country == 'United State':
	if age >=16:
		print('you can get the driving license!')
	else: 
		print('you are not old enough yet!')
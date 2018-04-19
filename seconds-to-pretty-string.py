def Time2String(Duration, Names = [[' minute', ' minutes'], [' hour', ' hours'], [' day', ' days'], [' week', ' weeks'], [' year', ' years'], ', ']):
	Duration = int(Duration)
	DurValue = Duration
	if Duration < 3600:
		if math.floor(DurValue/60) == 1:
			Duration = str(math.floor(DurValue/60)) + Names[0][0]
		else:
			Duration = str(math.floor(DurValue/60)) + Names[0][1]
	elif Duration < 86400:
		if math.floor(DurValue/60/60) == 1:
			Duration = str(math.floor(DurValue/60/60)) + Names[1][0] + Names[5]
		else:
			Duration = str(math.floor(DurValue/60/60)) + Names[1][1] + Names[5]
			
		if math.floor(DurValue/60%60) == 1:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][0]
		else:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][1]
	elif Duration < 604800:
		if math.floor(DurValue/60/60/24) == 1:
			Duration = str(math.floor(DurValue/60/60/24)) + Names[2][0] + Names[5]
		else:
			Duration = str(math.floor(DurValue/60/60/24)) + Names[2][1] + Names[5]
			
		if math.floor(DurValue/60/60%24) == 1:
			Duration = Duration + str(math.floor(DurValue/60/60%24)) + Names[1][0] + Names[5]
		else:
			Duration = Duration + str(math.floor(DurValue/60/60%24)) + Names[1][1] + Names[5]
	
		if math.floor(DurValue/60%60) == 1:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][0]
		else:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][1]
	elif Duration < 31449600:
		if math.floor(DurValue/60/60/24/7) == 1:
			Duration = str(math.floor(DurValue/60/60/24/7)) + Names[3][0] + Names[5]
		else:
			Duration = str(math.floor(DurValue/60/60/24/7)) + Names[3][1] + Names[5]
		
		if math.floor(DurValue/60/60/24%7) == 1:
			Duration = Duration + str(math.floor(DurValue/60/60/24%7)) + Names[2][0] + Names[5]
		else:
			Duration = Duration + str(math.floor(DurValue/60/60/24%7)) + Names[2][1] + Names[5]
			
		if math.floor(DurValue/60/60%24) == 1:
			Duration = Duration + str(math.floor(DurValue/60/60%24)) + Names[1][0] + Names[5]
		else:
			Duration = Duration + str(math.floor(DurValue/60/60%24)) + Names[1][1] + Names[5]
	
		if math.floor(DurValue/60%60) == 1:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][0]
		else:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][1]
	else:
		if math.floor(DurValue/60/60/24/7/52) == 1:
			Duration = str(math.floor(DurValue/60/60/24/7/52)) + Names[4][0] + Names[5]
		else:
			Duration = str(math.floor(DurValue/60/60/24/7/52)) + Names[4][1] + Names[5]
		
		if math.floor(DurValue/60/60/24/7%52) == 1:
			Duration = Duration + str(math.floor(DurValue/60/60/24/7%52)) + Names[3][0] + Names[5]
		else:
			Duration = Duration + str(math.floor(DurValue/60/60/24/7%52)) + Names[3][1] + Names[5]
		
		if math.floor(DurValue/60/60/24%7) == 1:
			Duration = Duration + str(math.floor(DurValue/60/60/24%7)) + Names[2][0] + Names[5]
		else:
			Duration = Duration + str(math.floor(DurValue/60/60/24%7)) + Names[2][1] + Names[5]
			
		if math.floor(DurValue/60/60%24) == 1:
			Duration = Duration + str(math.floor(DurValue/60/60%24)) + Names[1][0] + Names[5]
		else:
			Duration = Duration + str(math.floor(DurValue/60/60%24)) + Names[1][1] + Names[5]
	
		if math.floor(DurValue/60%60) == 1:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][0]
		else:
			Duration = Duration + str(math.floor(DurValue/60%60)) + Names[0][1]
			
	return str(Duration)

#you can use this function with custom names and separator by using a list based off this:
#[['single minute', 'multiple minutes'], ['single hour', 'multiple hours'], ['single day', 'multiple days'], ['single week', 'multiple weeks'], ['single year', 'multiple years'], 'separator (", " is the default one)']
#just pass the list after the seconds value e.g: func(120, [['m', 'm'], ['h', 'h'], ['d', 'd'], ['w', 'w'], ['y', 'y'], ', '])

def Ordinal(Num):
	Num = str(Num)
	if Num.endswith('1') and not Num.endswith('11'):
		return Num + 'st'
	elif Num.endswith('2') and not Num.endswith('12'):
		return Num + 'nd'
	elif Num.endswith('3') and not Num.endswith('13'):
		return Num + 'rd'
	else:
		return Num + 'th'

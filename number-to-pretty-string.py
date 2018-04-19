def Num2PrettyString(Num):
	String = str(Num)[::-1]
	Result = ''
	Count = 1
	for i in String:
		if Count == 3:
			Result = Result + i + ','
			Count = 1
		else:
			Result = Result + i
			Count = Count + 1
	
	Result = Result[::-1]
	
	if Result.startswith(','):
		Result = Result[1:]
	
	return Result

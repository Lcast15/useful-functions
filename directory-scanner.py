import os

def Scanner(DIR):
	ReturnList = []
	for i in os.scandir(DIR):
		if i.is_file():
			ReturnList.append(i.name)
		elif i.is_dir():
			for x in Scanner(DIR + '/' + i.name):
				ReturnList.append(i.name + '/' + x)
				
	return ReturnList

def SteamID264ID(SID):
	SIDSplit = SID.split(':')
	SID = int(SIDSplit[2]) * 2
	
	if SIDSplit[1] == '1':
		SID += 1
	 
	SID += 76561197960265728
	
	return SID

def getSchedule(messages):
#messages = [["HACKRU", "COLLEGEAVE", "10:30am", "5:30pm", "10/4/16","30"],["HACKRU", "COLLEGEAVE", "10:30am", "5:30pm", "10/4/16","30"]]
	names = [""]
	for i, item in enumerate(messages):
		event = messages[i][0]
		location = messages[i][2]
		start_time = messages[i][2]
		end_time = messages[i][3]
		date = messages[i][4]
		notify = messages[i][5]
		names.append(str(i) + ': ["HACKRU", "COLLEGEAVE", "10:30am", "5:30pm", "30"]' + 'You have ' + event + ' at ' + location + '. It starts at ' + start_time + ' and will end at ' + end_time + ' on ' + date + '. It is ' + notify + ' minutes before the event.\n')
	
	z = ""

	for x, item in enumerate(names):
		z += names[x]

#print(z)
	return(z)

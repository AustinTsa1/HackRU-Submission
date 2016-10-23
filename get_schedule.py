def get_schedule(messages):
	#messages = [["HACKRU", "COLLEGEAVE", "10:30am", "5:30pm", "10/4/16","30"],["HACKRU", "COLLEGEAVE", "10:30am", "5:30pm", "10/4/16","30"]]
	try:
		names = [""]
		for i, val in enumerate(messages):
			event = val[0]
			location = val[1]
			start_time = val[2]
			end_time = val[3]
			date = val[4]
			notify = val[5]
			names.append(str(i+1) + ': ' + 'You have ' + event + ' at ' + location + '. It starts at ' + start_time + ' \nand will end at ' + end_time + ' on ' + date + '.\nIt is ' + notify + ' minutes before the event.\n\n')
	
		z = ""

		for item in names:
			z += item
	except Exception as e:
		return('No Schedule Found.')
	#print(z)
	return(z)

#event,location,start_time,end_time,date,minutesbeforenotify
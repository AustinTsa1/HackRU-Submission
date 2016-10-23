def getSchedule(messages){
	names = [""]
	for i in len(messages) {
		event = messages[i][0]
		location = messages[i][2]
		start_time = messages[i][2]
		end_time = messages[i][3]
		date = messages[i][4]
		notify = messages[i][5]
		names.append('You have ' + event + ' at ' + location + '. It starts at ' + start_time + ' and will end at ' + end_time + ' on ' + date + '. It is ' + notify + ' minutes before the event.'\n)
	}
	for x in len(names) {
		z.append(x + ':' + names[x])
	}
	return z
}
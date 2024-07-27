def seconds_since_midnight(hours, minutes, seconds):

	hours_in_seconds = 13 * 3600
	minutes_in_seconds = 30 * 60
	seconds = 45

	result = hours_in_seconds + minutes_in_seconds + seconds
	return result

print(seconds_since_midnight(13, 30, 45))
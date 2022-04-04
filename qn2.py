'''
Lab 11 QN.2 
Done By: 1802965
'''
import datetime

class clockTime:
	def __init__(self):				# Initialize the clock Object with 0 timings
		self.hours = 0
		self.minutes = 0
		self.seconds = 0
		self.time = datetime.time()	# Creates a Time Object
	
	def setHours(self, hours):
		self.hours = hours
	
	def setMinutes(self, minutes):
		self.minutes = minutes
	
	def setSeconds(self, seconds):
		self.seconds = seconds
	
	def setTime(self, hours, minutes, seconds):
		self.time = datetime.time(hours, minutes, seconds)

	def showTime(self):				
		print(self.time.strftime("%H:%M:%S"))	# Formats & Prints the output when called 


def main():
	myClock = clockTime()
	while True:		
		input_hours = int(input("Input the hour 0-23: "))
		if input_hours >= 0 and input_hours < 24:			# Checks for valid hours
			break
	while True:		
		input_minutes = int(input("Input the minute 0-59: "))
		if input_minutes >= 0 and input_minutes < 60:		# Checks for valid minutes
			break
	while True:		
		input_seconds = int(input("Input the second 0-59: "))
		if input_seconds >= 0 and input_seconds < 60:		# Checks for valid seconds
			break
	myClock.setTime(input_hours, input_minutes, input_seconds)
	myClock.showTime()


if __name__ == "__main__":
	main()
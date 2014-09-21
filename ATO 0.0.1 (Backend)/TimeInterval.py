#-*-coding:utf-8-*-
#---------Modules---------#
import datetime
import Type

#---------Constants-------#
MINIMUM_TIME = 20         # (Integer) - Minimum duration for a time interval in minutes.

'''
	Class Description:
	# Dedicated time to fullfill a pending activity.
	# Its start date and duration have to be known.
'''
class TimeInterval(object):


	'''
	Constructor of the class

	# Atributes:  "start"        -  (datetime)           Start date of the timeInterval.
	# 			  "duration"     -  (datetime.timedelta) Duration in seconds of the timeInterval. It has to be 
	#											         greater or equal to the MINIMUM_TIME.
	#			  "end"			 -  (datetime) 			 End date of the timeInterval.
	'''
	def __init__(self, start, duration):
		self.start = start
		self.duration = duration
		self.end = start + duration

	'''
		Input: "newStart"  -  (datetime) New start date for the timeInterval. It has to be greater or
									   	 equal to datetime.datetime.now()
		Output: Raise Exception if "newStart" is lesser or equal to datetime.datetime.now()
		Purpose: Change the start date of the restriction.
	'''
	def changeStart(self, newStart):
		if( newStart >= datetime.datetime.now() ):
			self.start = newStart
		else:
			raise Exception("The new start date has to be greater than now.")

	'''
		Input: "newDuration"  -  (datetime.timedelta) New duration of the timeInterval. It has to bew greater or
								 equal to "MINI".
		Output: Raise exception if "newDuration" is lesser or equal to datetime.timedelta(minutes = MINIMUM_TIME)
		Purpose: Change the duration of a restriction.
	'''
	def changeDuration(self, newDuration):
		if( newDuration >= datetime.timedelta(minutes = MINIMUM_TIME) ):
			self.duration = newDuration
		else:
			raise Exception("The new duration has to be greater or equal than %d" % MINIMUM_TIME)

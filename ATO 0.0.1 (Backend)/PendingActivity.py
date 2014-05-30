#-*-coding:utf-8-*-
#---------Modules---------#
import datetime
import TimeInterval

#---------Constants-------#
TIME_TO_START =  120 # (Integer) - Minimum time until deadline

# Class Description:
	# Pending activities. 
	# Their deadline and estimated duration is known.
	# Even if the deadline of a pending activity has been reached, it is still considered as a Pending Activity.
	# If the activity has been succesfully completed, it is considered as a Completed Activity.
class PendingActivity(object):	# Constructor of the class
	# Atributes:  "title"             -  (String)    Text max. of 40 char that describes the pending activity.
	#			  "timeIntervals"     -  (List)      List of timeIntervals. The sum of the duration of the timeIntervals in
	#										         the list must be greater or equal to the estimated time to complete the
	#										         pending activity.
	#			  "freeTimeIntervals" -  (List)		 List of timeIntervals. It represents the time intervals that are
	#												 available to work in the pending activity, since (now() + TIME_TO_START)
	#												 to the deadline.
	#			  "description"       -  (String)    140 char max. that describes details of the pending activity.
	#			  "deadline"          -  (datetime)  Limit date to end the pending activity.
	#			  "estimatedTime"     -  (timeDelta) It is the time that the user believes that he/she will spend 
	#								                 performing a pending activity.
	# 			  "type"			  -  (Type)      Type of the pending activity.
	def __init__(self, title, deadline, eTime, patype, description = ''):
		self.title = title
		self.timeIntervals = []
		self.freeTimeIntervals = []
		self.description = description
		self.deadline = deadline
		self.estimatedTime = eTime
		self.type = patype


	# Input: None
	# Output: (Boolean) - Return True   if the pending activity can be completed based on the duration dedicated for it.
	#					  Retun  False  if the pending activity cannot be completed with the existing number of timeIntervals.
	'''Purpose: Check if a pending activity can be completed or not with the existing time intervals.'''
	def canBeCompleted(self):
		duration = 0 
		for ti in timeIntervals:
			duration += ti.duration
		return (duration >= estimatedTime)

	# Input: "newTimeInterval"  (TimeInterval)  - New time interval to work in the pending activity. It has to be greater 
	# 											  than the last time interval in the time intervals list.
	# Output: Raise Exception if the new time interval is lesser or equal than the end date of the last time interval in the
	#         timeIntervals list.
	''' Purpose: Add a new time interval to the list of time intervals of the pending activity in order to increase the 
			   probability of achieving it.'''
	def addTimeInterval(self, newTimeInterval):
		if( newTimeInterval	> timeIntervals[len(timeIntervals) - 1] ):
			timeIntervals.append(newTimeInterval)
		else:
			raise Exception("The new interval has to be greater than the last time interval in the time intervals list.")

	# Input: "newDeadline"  (datetime)  -  New deadline for the pending activity
	# Ouput: Raise Exception if the new deadline is lesser or equal than datetime.datetime.now() + the minimum time of a time interval.
	'''Purpose: Change the deadline of a pending activity.'''
	def reschedule(self, newDeadline):
		if( newDeadline > (datetime.datetime.now() + TimeInterval.MINIMUM_TIME) ):
			self.deadline = newDeadline
		else:
			raise Exception("The new deadline is too close.")

	






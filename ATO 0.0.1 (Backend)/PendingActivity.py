#-*-coding:utf-8-*-
#---------Modules---------#
import datetime
import TimeInterval
import Activity

#---------Constants-------#
TIME_TO_START =  120 # (Integer) - Minimum time until deadline

'''
	Class Description:
	Pending activities. 
	Their deadline and estimated duration is known.
	Even if the deadline of a pending activity has been reached, it is still considered as a Pending Activity.
	If the activity has been succesfully completed, it is considered as a Completed Activity.

	# Atributes:

	#		(Inherited)  
	#		"title"             -  (String)    Text max. of 40 char that describes the pending activity.
	#		"estimatedTime"     -  (timeDelta) It is the time that the user believes that he/she will spend 
	#  						                   performing a pending activity.
	#		"type"			    -  (Type)      Type of the pending activity.
	#		"deadline"          -  (datetime)  Limit date to end the pending activity.
	#		"description"       -  (String)    140 char max. that describes details of the pending activity.
	#		"startTime"		    -  (datetime)  Date when the activity is createc.

	#			  "timeIntervals"     -  (List)      List of timeIntervals. The sum of the duration of the timeIntervals in
	#										         the list must be greater or equal to the estimated time to complete the
	#										         pending activity.
	#			  "freeTimeIntervals" -  (List)		 List of timeIntervals. It represents the time intervals that are
	#												 available to work in the pending activity, since (now() + TIME_TO_START)
	#												 to the deadline.
	#			  "startTime"		  -  (datetime)  Date when the activity is createc.
'''
class PendingActivity(object, Activity):	# Constructor of the class

	def __init__(self, title, estimatedTime, atype, deadline, description=""):
		super().__init__(self, title, estimatedTime, False, atype, deadline, description)
		self.timeIntervals = []
		self.freeTimeIntervals = []


	'''
		Input: None
		Output: (Boolean) - Return True   if the pending activity can be completed based on the duration dedicated for it.
						    Retun  False  if the pending activity cannot be completed with the existing number of timeIntervals.
		Purpose: Check if a pending activity can be completed or not with the existing time intervals.
	'''
	def canBeCompleted(self):
		duration = 0 
		for ti in timeIntervals:
			duration += ti.duration
		return (duration >= estimatedTime)

	'''
		Input: "newTimeInterval"  (TimeInterval)  - New time interval to work in the pending activity. It has to be greater 
	 											  than the last time interval in the time intervals list.
		Output: Raise Exception if the new time interval is lesser or equal than the end date of the last time interval in the
	            timeIntervals list.
	 	Purpose: Add a new time interval to the list of time intervals of the pending activity in order to increase the 
			     probability of achieving it.
	'''
	def addTimeInterval(self, newTimeInterval):
		if( newTimeInterval	> timeIntervals[len(timeIntervals) - 1] ):
			timeIntervals.append(newTimeInterval)
		else:
			raise Exception("The new interval has to be greater than the last time interval in the time intervals list.")


	'''
		Input: None
		Output: None
	 	Purpose: Modify the time state of a pending activity by asking the user 
	 			 If the activity has been completed the attribute isCompleted becames True, if not it keeps being False
	'''
	def ask_if_completed(self):
		print ('Have you completed this Activity?\n \
				{title}\n \
				Started in: {start}\n \
				Deadline: {deadline}\n \
				Yes (Y), No (N)'.format(title = self.title, start = self.startTime, deadline = self.deadline)
		ans = raw_input().lower()
		if (ans != 'y') or (ans != 'n'):
			ask_if_completed(self)
		elif (ans == 'y'):
			self.isCompleted = True
		else:
			continue




	






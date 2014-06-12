#-*-coding:utf-8-*-
#---------Modules---------#
import datetime
import User
import PendingActivity
import TimeInterval
import CompletedActivity
''' Class Description:
	 ATO - autonomous task organizer with pending activities to organize.'''
class ATO(object):	

	'''
	Constructor of the class

	# Atributes:  "pendingActivities" -  (List)     List of pending Activities, initialized empty.
	# 			  "restrictions"      -  (List)     List of restrictions, initialized empty.
	#			  "freeTimeIntervals" -  (List)		 List of timeIntervals. It represents the time intervals that are
	#												 available to work in the pending activity, since (now() + TIME_TO_START)
	#			  "user"              -  (User)     User that depends of ATO.
	#			  "alias"             -  (String)   40 char max. name that personifies the ATO of the User.
	#			  "completed"         -  (List)		List of completed activities, initialized empty.
	'''
	def __init__(self, alias = "ATO"):
		self._pendingActivities = []
		self._restrictions = []
		self._freeTimeIntervals = []
		self._completed = []
		self._user = None
		self._alias = alias

	'''
		Input:  Attributes in the Pending Activity constructor help(PendingActivity.PendingActivity)
		Output: Raise Exception if there is no time available to complete the pending activitie.
		Purpose: Create a new pending activity and add it to the list of pending activities.
	'''
	def addPendingActivity(self, title, eTime, patype, deadline, description=""):
		if ( datetime.datetime.now() + eTime + datetime.timedelta(minutes = PendingActivity.TIME_TO_START) ) <= deadline:
			newP = PendingActivity.PendingActivity(title, eTime, patype, deadline, description)
			self.pendingActivities.append(newP)
		else:
			raise Exception("There is no time available to complete the pending activity")

	'''
		Input:  Attributes in the User constructor help(User)
		Output: None.
		Purpose: Define the user data.
	'''
	def defineUser(self, username, password, careers, email, dbirth, mbirth, ybirth, license = 0, friends = []):
		self.User = User.User(username, password, careers, email, dbirth, mbirth, ybirth, license, friends)

	'''
		Input: None
		Output: "notOrganizedPending"  (List)  -  List of pending activities that haven't been organized by ATO
		Purpose: Identify the pending activities that haven't been organized by ATO.
	'''
	def notOrganized(self):
		notOrganizedPending = []
		# Main loop - Go through the list of pending activities
		for act in pendingActivities:
			# Identify if it has been organized or not.
			if not act.timeIntervals:
				notOrganizedPending.append(act)
		return notOrganizedPending

	'''
		Input: None
		Output: "intervals"   (List)  -  Ordered list of activities related with a time interval which has been set
									     in the users schedule. The list can be composed of Restrictions or TimeIntervals.
										 The start date and the duration of these activities is known.
		Purpose: Identify all activities that have been set in the user's schedule.
	'''
	def intervalsScheduled(self):
		intervals = self.restrictions # Add all the restrictions given by the user.
		for pending in pendingActivities:
			intervals += pending.timeIntervals # Add the time intervals related with a pending activity.
		intervals.sort(key = lambda x: x.start, reverse = False) # Organize the intervals by start date.
		return intervals

	'''
		Input: None
		Output: Return the last deadline in the user's schedule
		Purpose: Set the end of an schedule.
	'''
	def getLastDeadline(self):
		pending = self.pendingActivities
		pending.sort(key = lambda x: x.deadline, reverse = True)
		return pending[0].deadline


	def completePendingActivity(self, patitle):
		completed = filter( lambda x: x.title == patitle, pendingActivities)
		if not completed:
			raise Exception("That is not a pending activity")
		else:
			pendingActivities.remove(completed)




	# # Input: None
	# # Output: None
	# # Purpose: Refresh the List of time intervals related to the time available to work in 
	# #          a pending activity since datetime.datetime.now() to the last deadline in the schedule.
	# '''Find free time spaces in the schedule in order to use them for pending Activities.'''
	# def defineFreeTime(self):
	# 	startTime = datetime.datetime.now()
	# 	endTime = datetime.datetime.now()
	# 	intervals = intervalsScheduled()

	# 	i = 0 
	# 	while True:
	# 		#Check if there is time available between the last occupied time interval and the last deadline
	# 		if ( i == len(intervals) - 1):
	# 			startTime = intervals[i].end
	# 			newDuration = getLastDeadline() - startTime
	# 			if(newDuration >= TimeInterval.MINIMUM_TIME):
	# 				newInterval = TimeInterval(startTime, newDuration)
	# 				self.freeTimeIntervals.append(newInterval)
	# 				break
	# 			else:
	# 				break
	# 		# Check if there is time available between now and the first occupied time interval 
	# 		elif( i == 0 and ( (intervals[i].start - startTime) >= TimeInterval.MINIMUM_TIME ) ):
	# 			endTime = intervals[i].start
	# 			newDuration = endTime - startTime
	# 			newInterval = TimeInterval(startTime, newDuration)
	# 			self.freeTimeIntervals.append(newInterval)
	# 			i += 1
	# 		# Check if there is time available between two occupied time intervals
	# 		elif( (intervals[i+1].start - intervals[i].end) >= TimeInterval.MINIMUM_TIME ):
	# 			startTime = intervals[i].end
	# 			endTime = intervals[i+1].start
	# 			newInterval = TimeInterval(startTime, newDuration)
	# 			self.freeTimeIntervals.append(newInterval)	
	# 			i += 1		
	# 		# If there are not resctrictions or time intervals defined then there is free time since
	# 		# datetime.datetime.now() to the last deadline.
	# 		elif( not intervals ):
	# 			endTime = getLastDeadline()
	# 			newDuration = endTime - startTime
	# 			newInterval = TimeInterval(startTime, newDuration)
	# 			self.freeTimeIntervals.append(newInterval)
	# 			break
	# 		else:
	# 			i += 1

	# def sumEstimatedTimes(self):
	# 	totalETime = datetime.timedelta(hours = 0)
	# 	for pending in pendingActivities:
	# 		totalETime += pending.estimatedTime
	# 	return totalETime

	# def 


	# # Inputs: ft  (TimeInterval)  -  Free Time - Time interval of the time available to complete any pending
	# #									         activity.
	# #		  pe  (float)         -  
	# def defineTimeIntervalSize(self, ft, pe, pr, acc, pt):


	# def organizePending(self):
		
	# 	if not notOrganized():
	# 		pass
	# 	else:
	# 		defineFreeTime()
	# 		for pending in notOrganized():



				





		
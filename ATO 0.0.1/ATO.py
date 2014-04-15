#-*-coding:utf-8-*-
#---------Modules---------#
import datetime
import User
import PendingActivity
import TimeInterval
# Class Description:
	# ATO - autonomous task organizer with pending activities to organize.
class ATO(object):	

	# Constructor of the class
	# Atributes:  "pendingActivities" -  (List)     List of pending Activities, initialized empty.
	# 			  "restrictions"      -  (List)     List of restrictions, initialized empty.
	#			  "freeTimeIntervals" -  (List)		 List of timeIntervals. It represents the time intervals that are
	#												 available to work in the pending activity, since (now() + TIME_TO_START)
	#			  "user"              -  (User)     User that depends of ATO.
	#			  "alias"             -  (String)   40 char max. name that personifies the ATO of the User.
	def __init__(self, alias = "ATO"):
		self.pendingActivities = []
		self.restrictions = []
		self.freeTimeIntervals = []
		self.user = None
		self.alias = alias

	# Input:      "title"          -  (String)    Text max. of 40 char that describes the pending activity.
	#			  "timeIntervals"  -  (List)      List of timeIntervals. The sum of the duration of the timeIntervals in
	#										      the list must be greater or equal to the estimated time to complete the
	#										      pending activity.
	#			  "description"    -  (String)    140 char max. that describes details of the pending activity.
	#			  "deadline"       -  (datetime)  Limit date to end the pending activity.
	#			  "estimatedTime"  -  (timedelta) It is the time that the user believes that he/she will spend 
	#								              performing a pending activity.
	# Output: Raise Exception if there is no time available to complete the pending activitie.
	# Purpose: Create a new pending activity and add it to the list of pending activities.
	def addPendingActivity(self, title, deadline, eTime, description = ''):
		if ( datetime.datetime.now() + eTime + datetime.timedelta(minutes = PendingActivity.TIME_TO_START) ) <= deadline:
			newP = PendingActivity.PendingActivity(title, deadline, eTime, description)
			self.pendingActivities.append(newP)
		else:
			raise Exception("There is no time available to complete the pending activity")

	# Inputs:     "dbirth"    -  (Integer)  * User's day of birth   [1,31]
	#			  "mbirth"    -  (Integer)  * User's month of birth [1,12]
	# 			  "ybirth"    -  (Integer)  * User's year of birth  [0,99999]
	#  			  "username"  -  (String)   * User's name
	#			  "password"  -  (String)   * User's personal coded password
	#			  "careers"   -  (List)     * User's careers. List of indexes related with CAREERS.
	#			  "friends"   -  (List)     * The usernames of the User's friends or colleagues
	#			  "license"   -  (Integer)  * 0 if the user has a free license / 1 if the user has a paid license
	#			  "email"     -  (String)   * Email of the user - <useremail@something>
	#			  "birthday"  -  (datetime) * User's birthday
	# Output: None.
	# Purpose: Define the user data.
	def defineUser(self, username, password, careers, email, dbirth, mbirth, ybirth, license = 0, friends = []):
		self.User = User.User(username, password, careers, email, dbirth, mbirth, ybirth, license, friends)

	# Input: None
	# Output: "notOrganizedPending"  (List)  -  List of pending activities that haven't been organized by ATO
	# Purpose: Identify the pending activities that haven't been organized by ATO.
	def notOrganized(self):
		notOrganizedPending = []
		# Main loop - Go through the list of pending activities
		for act in pendingActivities:
			# Identify if it has been organized or not.
			if not act.timeIntervals:
				notOrganizedPending.append(act)
		return notOrganizedPending

	# Input: None
	# Output: "intervals"   (List)  -  Ordered list of activities related with a time interval which has been set
	#							       in the users schedule. The list can be composed of Restrictions or TimeIntervals.
	#								   The start date and the duration of these activities is known.
	# Purpose: Identify all activities that have been set in the user's schedule.
	def intervalsScheduled(self):
		intervals = self.restrictions # Add all the restrictions given by the user.
		for pending in pendingActivities:
			intervals += pending.timeIntervals # Add the time intervals related with a pending activity.
		intervals.sort(key = lambda x: x.start, reverse = False) # Organize the intervals by start date.
		return intervals

	# Input: None
	# Output: Return the last deadline in the user's schedule
	# Purpose: Set the end of an schedule.
	def getLastDeadline(self):
		pending = self.pendingActivities
		pending.sort(key = lambda x: x.deadline, reverse = True)
		return pending[0].deadline

	def defineFreeTime(self):
		startTime = datetime.datetime.now()
		endTime = datetime.datetime.now()
		intervals = intervalsScheduled()

		i = 0 
		while True:
			if ( i == len(intervals) - 1):
				startTime = intervals[i].end
				newDuration = getLastDeadline() - startTime
				if(newDuration >= TimeInterval.MINIMUM_TIME):
					newInterval = TimeInterval(startTime, newDuration)
					self.freeTimeIntervals.append(newInterval)
					break
				else:
					break
			elif( i == 0 and ( (intervals[i].start - startTime) >= TimeInterval.MINIMUM_TIME ) ):
				endTime = intervals[i].start
				newDuration = endTime - startTime
				newInterval = TimeInterval(startTime, newDuration)
				self.freeTimeIntervals.append(newInterval)
				i += 1
			elif( (intervals[i+1].start - intervals[i].end) >= TimeInterval.MINIMUM_TIME ):
				startTime = intervals[i].end
				endTime = intervals[i+1].start
				newInterval = TimeInterval(startTime, newDuration)
				self.freeTimeIntervals.append(newInterval)	
				i += 1		
			else:
				i += 1






	def organizePending(self):
		if not notOrganized():
			return 1
		else:
			for pending in notOrganized():




		
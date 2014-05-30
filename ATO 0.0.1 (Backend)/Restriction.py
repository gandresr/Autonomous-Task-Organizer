#-*-coding:utf-8-*-
#---------Modules---------#
import datetime
import Type

#---------Constants-------#
MINIMUM_TIME = 20         # (Integer) - Minimum duration for a restriction in minutes.

# Class Description:
	# Activity with an irreplaceable time.
	# Its start date and duration have to be known.
class Restriction(object):


	'''Constructor of the class'''
	# Atributes:  "title"        -  (String)             40 char max. that describes the restriction.
	#			  "start"        -  (datetime)           Start date of the restriction
	# 			  "duration"     -  (datetime.timedelta) Duration in seconds of the restriction. It has to be 
	#												     greater or equal to the MINIMUM_TIME.
	#			  "description"  -  (String)             140 char max. that describes details of the restriction.
	# 			  "type"         -  (Type)               Inicialized as none. Is the type of the restriction.
	#			  "end"			 -  (datetime)   		 End date of the restriction
 	def __init__(self, title, start, duration, description = ''):
		self.title = title
		self.start = start
		self.duration = duration
		self.end = start + duration
		self.description = description
		self.type = None

	# Input: "newStart"  -  (datetime) New start date for the restriction. It has to be greater or
	#								   equal to datetime.datetime.now()
	# Output: Raise Exception if "newStart" is lesser or equal to datetime.datetime.now()
	'''Purpose: Change the start date of the restriction. '''
	def changeStart(self, newStart):
		if( newStart >= datetime.datetime.now() ):
			self.start = newStart
		else:
			raise Exception("The new start date has to be greater than now.")

	# Input: "newDuration"  -  (datetime.timedelta) New duration of the restriction. It has to bew greater or
	#												equal to "MINIMUM_TIME".
	# Output: Raise exception if "newDuration" is lesser or equal to datetime.timedelta(minutes = MINIMUM_TIME)
	'''Purpose: Change the duration of a restriction.'''
	def changeDuration(self, newDuration):
		if( newDuration >= datetime.timedelta(minutes = MINIMUM_TIME) ):
			self.duration = newDuration
		else:
			raise Exception("The new duration has to be greater or equal than %d" % MINIMUM_TIME)

	# Input: "newDescription"  -  (String) New description for the restriction. Its length is max. 140 char.
	# Output: Raise exception if "newDescription" is lesser or equal to 140 char.
	'''Purpose: Change the description of a restriction.'''
	def editDescription(self, newDescription):
		if( len(newDescription) <= 140 ):
			self.description = newDescription
		else:
			raise Exception("The new description has to be shorter than 140 characters.")

	# Input: "typeTitle"  -  (String) The title of the type that belongs to the restriction.
	#								  Its length is max. 40 char.
	'''Purpose: Change the type of a restriction.'''
	def defineType(self, typeTitle):
		self.type = Type.Type(typeTitle)







#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

import piot.common.ConfigConst as ConfigConst

from piot.common.ConfigUtil import ConfigUtil
from piot.common.IDataMessageListener import IDataMessageListener

from piot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from piot.cda.system.SystemMemUtilTask import SystemMemUtilTask

from piot.data.SystemPerformanceData import SystemPerformanceData

class SystemPerformanceManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		pass

	def handleTelemetry(self):
		pass
		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		pass
	
	def startManager(self):
		pass
		
	def stopManager(self):
		pass

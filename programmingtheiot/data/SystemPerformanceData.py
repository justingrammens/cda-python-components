#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# You may find it more helpful to your design to adjust the
# functionality, constants and interfaces (if there are any)
# provided within in order to meet the needs of your specific
# Programming the Internet of Things project.
# 

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.BaseIotData import BaseIotData

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		super(SystemPerformanceData, self).__init__(name = ConfigConst.SYSTEM_PERF_MSG, typeID = ConfigConst.SYSTEM_PERF_TYPE, d = d)
		pass
	
	def getCpuUtilization(self):
		pass
	
	def getDiskUtilization(self):
		pass
	
	def getMemoryUtilization(self):
		pass
	
	def setCpuUtilization(self, cpuUtil):
		pass
	
	def setDiskUtilization(self, diskUtil):
		pass
	
	def setMemoryUtilization(self, memUtil):
		pass
	
	def _handleUpdateData(self, data):
		pass

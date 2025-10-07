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

class ActuatorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, typeID: int = ConfigConst.DEFAULT_ACTUATOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		super(ActuatorData, self).__init__(name = name, typeID = typeID, d = d)
		self.value = ConfigConst.DEFAULT_VAL
		self.command = ConfigConst.DEFAULT_COMMAND
		self.stateData = ""
		self.isResponse = False
	
	def getCommand(self) -> int:
		return self.command

	def getStateData(self) -> str:
		return self.stateData

	def getValue(self) -> float:
		return self.value

	def isResponseFlagEnabled(self) -> bool:
		return self.isResponse

	def setCommand(self, command: int):
		self.command = command
		self.updateTimeStamp()

	def setAsResponse(self):
		self.isResponse = True
		self.updateTimeStamp()
	
	def setStateData(self, stateData: str):
		if stateData:
			self.stateData = stateData
			self.updateTimeStamp()

	def setValue(self, val: float):
		self.value = val
		self.updateTimeStamp()
	
	def _handleUpdateData(self, data):
		if data and isinstance(data, ActuatorData):
			self.command = data.getCommand()
			self.stateData = data.getStateData()
			self.value = data.getValue()
			self.isResponse = data.isResponseFlagEnabled()
			
		
		
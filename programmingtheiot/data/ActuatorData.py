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
		pass
	
	def getCommand(self) -> int:
		pass
	
	def getStateData(self) -> str:
		pass
	
	def getValue(self) -> float:
		pass
	
	def isResponseFlagEnabled(self) -> bool:
		return False
	
	def setCommand(self, command: int):
		pass
	
	def setAsResponse(self):
		pass
		
	def setStateData(self, stateData: str):
		pass
	
	def setValue(self, val: float):
		pass
		
	def _handleUpdateData(self, data):
		pass
		
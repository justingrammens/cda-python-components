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

class SensorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
		
	def __init__(self, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		super(SensorData, self).__init__(name = name, typeID = typeID, d = d)
	
		self.value = ConfigConst.DEFAULT_VAL
	
	def getValue(self) -> float:
		return self.value
	
	def setValue(self, newVal: float):
		self.value = newVal
		self.updateTimeStamp()
		
	def _handleUpdateData(self, data):
		if data and isinstance(data, SensorData):
			self.value = data.getValue()
	
	'''
	def __str__(self):
		"""
		Returns a string representation of this instance.
		
		@return The string representing this instance, returned in CSV 'key=value' format.
		"""
		
		return '{}={},{}={},{}={},{}={},{}={},{}={},{}={},{}={},{}={},{}={}'.format(
			ConfigConst.NAME_PROP, self.name,
			ConfigConst.TYPE_ID_PROP, self.typeID,
			ConfigConst.TIMESTAMP_PROP, self.timeStamp,
			ConfigConst.STATUS_CODE_PROP, self.statusCode,
			ConfigConst.HAS_ERROR_PROP, self.hasError,
			ConfigConst.LOCATION_ID_PROP, self.locationID,
			ConfigConst.ELEVATION_PROP, self.elevation,
			ConfigConst.LATITUDE_PROP, self.latitude,
			ConfigConst.LONGITUDE_PROP, self.longitude,
			ConfigConst.VALUE_PROP, self.value)
	'''		
			
			

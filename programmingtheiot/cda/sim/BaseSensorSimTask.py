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

import logging
import random

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataSet


class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = ConfigConst.DEFAULT_VAL
	DEFAULT_MAX_VAL = 100.0
	
	def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE, dataSet: SensorDataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):

		logging.info("BaseSensorSimTask: Initializing for dataset: %s", dataSet)	
		self.dataSet = dataSet
		self.name = name
		self.typeID = typeID
		self.dataSetIndex = 0
		#self.useRandomizer = False
		# NOTE!!!!!! CHANGED TO USE RADOMNIZER BY DEFAULT
		self.useRandomizer = True
	
		self.latestSensorData = None
	
		if not self.dataSet:
			self.useRandomizer = True
			self.minVal = minVal
			self.maxVal = maxVal
	
	def generateTelemetry(self) -> SensorData:
		"""
		Implement basic logging and SensorData creation. Sensor-specific functionality
		should be implemented by sub-class.
		
		A local reference to SensorData can be contained in this base class.
		"""
		sensorData = SensorData(typeID = self.getTypeID(), name = self.getName())
		sensorVal = ConfigConst.DEFAULT_VAL
	
		if self.useRandomizer:
			logging.info("USE RANDOMIZER!!!!!")
			
			logging.info("BaseSensorSimTask: Generating random telemetry for sensor: %s", self.getName())
			
			logging.info("MIN VALUE IS: %f", self.minVal)
			logging.info("MAX VALUE IS: %f", self.minVal)
			
			## NOTE: Using RANDOM and uniform here to get float values!!!
			sensorVal = random.uniform(self.minVal, self.maxVal)
			logging.info("BaseSensorSimTask: Generating telemetry for sensor: %s, value: %f", self.getName(), sensorVal)
			logging.info("BaseSensorSimTask: Using randomizer? %s", self.useRandomizer)
		else:
			logging.info("WE ARE GEETTING IN HERE!!!!!!!!!!!!!!!!!!!!!!!!!!11!")
			sensorVal = self.dataSet.getDataEntry(index = self.dataSetIndex)
			self.dataSetIndex = self.dataSetIndex + 1
			logging.info("BaseSensorSimTask: Generating telemetry for sensor: %s, value: %f", self.getName(), sensorVal)
			logging.info("BaseSensorSimTask: Using randomizer? %s", self.useRandomizer)
			if self.dataSetIndex >= self.dataSet.getDataEntryCount() - 1:
				self.dataSetIndex = 0
		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData
	
		return self.latestSensorData
		
	
	def getTelemetryValue(self) -> float:
		"""
		If a local reference to SensorData is not None, simply return its current value.
		If SensorData hasn't yet been created, call self.generateTelemetry(), then return
		its current value.
		"""
		if not self.latestSensorData:
			self.generateTelemetry()
		return self.latestSensorData.getValue()
	
	def getLatestTelemetry(self) -> SensorData:
		"""
		This can return the current SensorData instance or a copy.
		"""
		return self.latestSensorData
	
	def getName(self) -> str:
		return self.name
	
	def getTypeID(self) -> int:
		return self.typeID
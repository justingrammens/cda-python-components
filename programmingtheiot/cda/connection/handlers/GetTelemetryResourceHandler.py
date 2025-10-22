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

import programmingtheiot.common.ConfigConst as ConfigConst

from coapthon import defines
from coapthon.resources.resource import Resource

from programmingtheiot.common.ConfigUtil import ConfigUtil

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ITelemetryDataListener import ITelemetryDataListener

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SensorData import SensorData

class GetTelemetryResourceHandler(Resource, ITelemetryDataListener):
	"""
	Observable resource that will collect telemetry based on the given
	name from the data message listener implementation.
	
	NOTE: Your implementation will likely need to extend from the selected
	CoAP library's observable resource base class.
	
	"""

	def __init__(self, name: str = ConfigConst.SENSOR_MSG, coap_server = None, dataMsgListener: IDataMessageListener = None):
		super(GetTelemetryResourceHandler, self).__init__( \
			name, coap_server, visible = True, observable = True, allow_children = True)

		self.pollCycles = \
			ConfigUtil().getInteger( \
				section = ConfigConst.CONSTRAINED_DEVICE, \
				key = ConfigConst.POLL_CYCLES_KEY, \
				defaultVal = ConfigConst.DEFAULT_POLL_CYCLES)
		
		self.dataUtil = DataUtil()
		self.sensorData = SensorData()
		
		self.dataMsgListener = dataMsgListener
		
		# reserved for lab module 10
		if self.dataMsgListener:
			self.dataMsgListener.setTelemetryDataListener(self)
		
		# for testing
		self.payload = "GetSensorData"
		
	def render_GET_advanced(self, request, response):
		if request:
			response.code = defines.Codes.CONTENT.number
			
			if not self.sensorData:
				response.code = defines.Codes.EMPTY.number
				self.sensorData = SensorData()
				
			jsonData = DataUtil().sensorDataToJson(self.sensorData)
			
			logging.info("Latest SensorData JSON: " + jsonData)
			
			response.payload = (defines.Content_types["application/json"], jsonData)
			response.max_age = self.pollCycles
	
			# 'changed' will be discussed in a later exercise
			self.changed = False
				
		return self, response
	
	def onSensorDataUpdate(self, data: SensorData) -> bool:
		self.sensorData = data
		
		
	
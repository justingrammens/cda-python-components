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

from coapthon import defines
from coapthon.resources.resource import Resource

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil

from programmingtheiot.common.ISystemPerformanceDataListener import ISystemPerformanceDataListener
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class GetSystemPerformanceResourceHandler(Resource, ISystemPerformanceDataListener):
	"""
	Observable resource that will collect system performance data based on the
	given name from the data message listener implementation.
	
	NOTE: Your implementation will likely need to extend from the selected
	CoAP library's observable resource base class.
	
	"""
	def __init__(self, name: str = ConfigConst.SYSTEM_PERF_MSG, coap_server = None, dataMsgListener: IDataMessageListener = None):
		
		super(GetSystemPerformanceResourceHandler, self).__init__( \
			name, coap_server, visible = True, observable = True, allow_children = True)

		self.pollCycles = \
			ConfigUtil().getInteger( \
				section = ConfigConst.CONSTRAINED_DEVICE, \
				key = ConfigConst.POLL_CYCLES_KEY, \
				defaultVal = ConfigConst.DEFAULT_POLL_CYCLES)
		
		self.dataUtil = DataUtil()
		self.sysPerfData = SystemPerformanceData()
		
		self.dataMsgListener = dataMsgListener
		
		# reserved for lab module 10
		if self.dataMsgListener:
			self.dataMsgListener.setSystemPerformanceDataListener(self)
		
		# for testing
		self.payload = "GetSysPerfData"
	
		
	def render_GET_advanced(self, request, response):
		if request:
			response.code = defines.Codes.CONTENT.number
			
			if not self.sysPerfData:
				response.code = defines.Codes.EMPTY.number
				self.sysPerfData = SystemPerformanceData()
				
			jsonData = DataUtil().systemPerformanceDataToJson(self.sysPerfData)
			
			logging.info("Latest SystemPerformanceData JSON: " + jsonData)
			
			response.payload = (defines.Content_types["application/json"], jsonData)
			response.max_age = self.pollCycles
	
			# 'changed' will be discussed in a later exercise
			self.changed = False
				
		return self, response
	
	def onSystemPerformanceDataUpdate(self, data: SystemPerformanceData) -> bool:
		self.sysPerfData = data
		
	
	
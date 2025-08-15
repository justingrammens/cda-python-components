#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging

import piot.common.ConfigConst as ConfigConst

from piot.common.ConfigUtil import ConfigUtil
from piot.common.ITelemetryDataListener import ITelemetryDataListener

from piot.data.DataUtil import DataUtil
from piot.data.SystemPerformanceData import SystemPerformanceData

class GetSystemPerformanceResourceHandler(ITelemetryDataListener):
	"""
	Observable resource that will collect system performance data based on the
	given name from the data message listener implementation.
	
	NOTE: Your implementation will likely need to extend from the selected
	CoAP library's observable resource base class.
	
	"""

	def __init__(self):
		pass
		
	def onSystemPerformanceDataUpdate(self, data: SystemPerformanceData) -> bool:
		pass
	
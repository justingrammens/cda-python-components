#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging

from threading import Thread
from time import sleep

from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

import piot.common.ConfigConst as ConfigConst

from piot.common.ConfigUtil import ConfigUtil
from piot.common.ResourceNameEnum import ResourceNameEnum

from piot.common.IDataMessageListener import IDataMessageListener
from piot.cda.connection.handlers.GetTelemetryResourceHandler import GetTelemetryResourceHandler
from piot.cda.connection.handlers.UpdateActuatorResourceHandler import UpdateActuatorResourceHandler
from piot.cda.connection.handlers.GetSystemPerformanceResourceHandler import GetSystemPerformanceResourceHandler

class CoapServerAdapter():
	"""
	Definition for a CoAP communications server, with embedded test functions.
	
	"""
	
	def __init__(self, dataMsgListener = None):
		pass
		
	def addResource(self, resourcePath: ResourceNameEnum = None, endName: str = None, resource = None):
		pass
				
	def startServer(self):
		pass
	
	def stopServer(self):
		pass
	
	def setDataMessageListener(self, listener: IDataMessageListener = None) -> bool:
		pass

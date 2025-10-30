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
import socket
import traceback

from coapthon import defines
from coapthon.client.helperclient import HelperClient
from coapthon.messages.option import Option
from coapthon.utils import parse_uri
from coapthon.utils import generate_random_token

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.connection.IRequestResponseClient import IRequestResponseClient

from programmingtheiot.data.DataUtil import DataUtil


class CoapClientConnector(IRequestResponseClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, dataMsgListener: IDataMessageListener = None):
		self.config = ConfigUtil()
		self.dataMsgListener = dataMsgListener
		self.enableConfirmedMsgs = False
		self.coapClient = None
		
		self.observeRequests = { }
		
		self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_COAP_PORT)
				
		self.includeDebugLogDetail = True
		self.uriPath = f"coap://{self.host}:{self.port}/"
		
		try:
			tmpHost = socket.gethostbyname(self.host)
			
			if tmpHost:
				self.host = tmpHost
				self._initClient()
			else:
				logging.error(f"Can't resolve host: {self.host}")
			
		except socket.gaierror:
			logging.error(f"Failed to resolve host: {self.host}")
			raise

		
		logging.info(f"CoAP client will connect to: {self.uriPath}")
	
	def sendDiscoveryRequest(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("Discovering remote resources...")
		
		resourcePath = self._createResourcePath(None, '.well-known/core')
		
		logging.info(f"Issuing DISCOVERY with path: {resourcePath}")
		
		request = self.coapClient.mk_request(defines.Codes.GET, path = resourcePath)
		request.token = generate_random_token(2)
		
		self.coapClient.send_request(request = request, timeout = timeout, callback = self._onDiscoveryResponse)

	def sendDeleteRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		pass

	def sendGetRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		if resource or name:
			resourcePath = self._createResourcePath(resource, name)
			
			logging.info(f"Issuing an awesome GET with path: {resourcePath}")
			
			request = self.coapClient.mk_request(defines.Codes.GET, path = resourcePath)
			request.token = generate_random_token(2)
			
			if not enableCON:
				request.type = defines.Types["NON"]
				
			response = self.coapClient.send_request(request = request, timeout = timeout)
			
			self._onGetResponse(response = response, resourcePath = resourcePath)
		else:
			logging.warning("Can't test GET - no path or path list provided.")

	def sendPostRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, payload: str = None, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		pass

	def sendPutRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, payload: str = None, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		if resource or name:
			resourcePath = self._createResourcePath(resource, name)
			
			logging.info(f"Issuing PUT with path: {resourcePath}")
			
			request = self.coapClient.mk_request(defines.Codes.PUT, path = resourcePath)
			request.token = generate_random_token(2)
			request.payload = payload
			
			if not enableCON:
				request.type = defines.Types["NON"]
						
			self.coapClient.send_request(request = request, callback = self._onPutResponse, timeout = timeout)
		else:
			logging.warning("Can't test PUT - no path or path list provided.")

	def setDataMessageListener(self, listener: IDataMessageListener = None) -> bool:
		if listener:
			self.dataMsgListener = listener
			return True
		
		return False

	def startObserver(self, resource: ResourceNameEnum = None, name: str = None, ttl: int = IRequestResponseClient.DEFAULT_TTL) -> bool:
		pass

	def stopObserver(self, resource: ResourceNameEnum = None, name: str = None, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		pass
	
	def _createResourcePath(self, resource: ResourceNameEnum = None, name: str = None):
		resourcePath = ""
		hasResource = False
		
		if resource:
			resourcePath = resourcePath + resource.value
			hasResource = True
			
		if name:
			if hasResource:
				resourcePath = resourcePath + "/"
			
			resourcePath = resourcePath + name
		
		return resourcePath
	
	def _initClient(self):
		try:
			self.coapClient = HelperClient(server = (self.host, self.port))
	
			logging.info(f"Client created. Will invoke resources at {self.uriPath}")

		except Exception as e:
			# obviously, this is a critical failure - you may want to handle this differently
			logging.error(f"Failed to create CoAP client to URI path {self.uriPath}")
			traceback.print_exception(type(e), e, e.__traceback__)
			
	def _onDeleteResponse(self, response):
		pass
	
	def _onDiscoveryResponse(self, response):
		if not response:
			logging.warning("DISCOVERY response invalid. Ignoring.")
			return
		
		logging.info(f"DISCOVERY response received: {response.payload}")
	
	def _onGetResponse(self, response, resourcePath: str = None):
		if not response:
			logging.warning("GET response invalid. Ignoring.")
			return
		
		logging.info("GET response received.")
		
		jsonData = response.payload
		locationPath = resourcePath.split('/')
		
		if len(locationPath) > 2:
			dataType = locationPath[2]
			
			if dataType == ConfigConst.ACTUATOR_CMD:
				# TODO: convert payload to ActuatorData and verify!
				logging.info(f"ActuatorData received: {jsonData}")
				
				try:
					ad = DataUtil().jsonToActuatorData(jsonData)
					
					if self.dataMsgListener:
						self.dataMsgListener.handleActuatorCommandMessage(ad)
				except:
					logging.warning(f"Failed to decode actuator data. Ignoring: {jsonData}")
					return
			else:
				logging.info(f"Response data received. Payload: {jsonData}")
				
		else:
			logging.info(f"Response data received. Payload: {jsonData}")
	
	def _onPostResponse(self, response):
		pass
	
	def _onPutResponse(self, response):
		if not response:
			logging.warning("PUT response invalid. Ignoring.")
			return
		
		logging.info(f"PUT response received: {response.payload}")
	
	

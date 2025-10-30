import logging
import socket
import threading
import traceback

import asyncio

from aiocoap import *

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.connection.IRequestResponseClient import IRequestResponseClient

from programmingtheiot.data.DataUtil import DataUtil


class AsyncCoapClientConnector(IRequestResponseClient):
    
    def __init__(self, dataMsgListener: IDataMessageListener = None):
        self.config = ConfigUtil()
        self.dataMsgListener = dataMsgListener
        self.enableConfirmedMsgs = False
        self.coapClient = None
        
        self.observeRequests = { }
        self.observeTasks = { }
        
        self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
        self.port = self.config.getInteger(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_COAP_PORT)
        
        self.includeDebugLogDetail = True
        
        try:
            tmpHost = socket.gethostbyname(self.host)
            
            if tmpHost:
                self.host = tmpHost
            else:
                logging.error(f"Can't resolve host: {self.host}")
            
        except socket.gaierror:
            logging.error(f"Failed to resolve host: {self.host}. Check hostname in config.")
            raise
        
        self.uriPath = f"coap://{self.host}:{self.port}/"
        
        logging.info(f"\tURI Path: {self.uriPath}")

        self._initEventLoop()
        
    def setDataMessageListener(self, listener: IDataMessageListener = None) -> bool:
        if listener:
            self.dataMsgListener = listener
            return True
        
        return False
    
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
    
    async def _handleStartObserveRequest(self, resourcePath: str = None):
        pass
    
    async def _handleStopObserveRequest(self, resourcePath: str = None, ignoreErr: bool = False):
        pass
    
    async def _handleDeleteRequest(self, resourcePath: str = None, enableCON: bool = False):
        pass
    
    async def _handleDiscoveryRequest(self, resourcePath: str = None, enableCON: bool = False):
        pass
    
    async def _handleGetRequest(self, resourcePath: str = None, enableCON: bool = False):
        pass
    
    async def _handlePostRequest(self, resourcePath: str = None, payload: str = None, enableCON: bool = False):
        pass
    
    async def _handlePutRequest(self, resourcePath: str = None, payload: str = None, enableCON: bool = False):
        pass

    def _onDeleteResponse(self, response):
        pass
    
    def _onDiscoveryResponse(self, response):
        pass
    
    def _onGetResponse(self, response):
        pass
    
    def _onPostResponse(self, response):
        pass
    
    def _onPutResponse(self, response):
        pass
    
    def _initEventLoop(self):
        def startEventLoop(loop):
            asyncio.set_event_loop(loop)
            loop.run_forever()

        self._eventLoopThread = asyncio.new_event_loop()
        self._executionThread = threading.Thread(
            target = startEventLoop, 
            args = (self._eventLoopThread,), 
            daemon = True
        )

        self._executionThread.start()

        future = asyncio.run_coroutine_threadsafe(
            self._initClientContext(), 
            self._eventLoopThread
        )

        future.result()

    async def _initClientContext(self):
        self.clientContext = await Context.create_client_context()
        
    
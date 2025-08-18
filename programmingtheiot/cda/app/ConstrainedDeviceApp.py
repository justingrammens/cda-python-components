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

import argparse
import logging
import traceback

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil

logging.basicConfig(format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s', level = logging.DEBUG)

class ConstrainedDeviceApp():
	"""
	Definition of the ConstrainedDeviceApp class.
	
	"""
	
	def __init__(self):
		"""
		Initialization of class.
		
		@param path The name of the resource to apply to the URI.
		"""
		logging.info("Initializing CDA...")
		
		# TODO: implementation here
		
		self.isStarted = False

	def isAppStarted(self) -> bool:
		"""
		"""
		return self.isStarted

	def startApp(self):
		"""
		Start the CDA. Calls startManager() on the device data manager instance.
		
		"""
		logging.info("Starting CDA...")
		
		# TODO: implementation here
		
		logging.info("CDA started.")

	def stopApp(self, code: int):
		"""
		Stop the CDA. Calls stopManager() on the device data manager instance.
		
		"""
		logging.info("CDA stopping...")
		
		# TODO: implementation here
		
		logging.info("CDA stopped with exit code %s.", str(code))
		
def main():
	"""
	Main function definition for running client as application.
	
	Current implementation runs for 65 seconds then exits.
	"""
	argParser = argparse.ArgumentParser( \
		description = 'CDA used for generating telemetry - Programming the IoT.')
	
	argParser.add_argument('-c', '--configFile', help = 'Optional custom configuration file for the CDA.')

	configFile = None

	try:
		args = argParser.parse_args()
		configFile = args.configFile

		logging.info('Parsed configuration file arg: %s', configFile)
	except:
		logging.info('No arguments to parse.')

	# init ConfigUtil
	configUtil = ConfigUtil(configFile)
	cda = None

	try:
		# init CDA
		cda = ConstrainedDeviceApp()

		# start CDA
		cda.startApp()

		# check if CDA should run forever
		runForever = configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.RUN_FOREVER_KEY)

		if runForever:
			# sleep ~5 seconds every loop
			while (True):
				sleep(5)
			
		else:
			# run CDA for ~65 seconds then exit
			if (cda.isAppStarted()):
				sleep(65)
				cda.stopApp(0)
			
	except KeyboardInterrupt:
		logging.warning('Keyboard interruption for CDA. Exiting.')

		if (cda):
			cda.stopApp(-1)

	except Exception as e:
		# handle any uncaught exception that may be thrown
		# during CDA initialization
		logging.error('Startup exception caused CDA to fail. Exiting.')
		traceback.print_exception(type(e), e, e.__traceback__)

		if (cda):
			cda.stopApp(-2)

	# unnecessary
	logging.info('Exiting CDA.')
	exit()

if __name__ == '__main__':
	"""
	Attribute definition for when invoking as app via command line
	
	"""
	main()

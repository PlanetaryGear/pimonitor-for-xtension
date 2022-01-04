#
#		PI MONITOR CONFIGURATION FILE		https://MacHomeAutomation.com
#
#		This program speaks to the xtension kit plugin for XTension and would
#		serve little purpose for anyone not using that.
#
#		
#
# 	User selectable options for the various functions of the pimonitor application below
#

# HOSTNAME
#	if this is not set here then the hostname set on the device will be used instead
#	uncomment this and set it if you wish to override that value
#currentHostname 		= "My Pi More Descriptive Name"


showTempsinF	 		= False 	# display the temperature in F or C. Change to False for C

alsoShowInOtherScale	= True 		# if true then the C or F value, whichever is the one  
									# you did not select for the actual value will be displayed 
									# in the value string for the unit, but the numeric value 
									# for the unit will still be the one you selected above. 
									# For example without this the display will be
									# "52°C" or "152°F" With this turned on the display 
									# in XTension will instead show 
									# "52°C (152°F)" or "152°F (52°C)"
									# Note that pi thermal throttling starts around 80°C as of this writing

#
# CPU TEMPERATURE
# how often to check for a change to the CPU Temperature
#
checkCPUTemp			= True
CPUTempScanSeconds		= 10



#
#	WiFi RSSI
#
# how often to check the RSSI level
#
RSSIScanSeconds 		= 10
checkRSSI 				= True
showBitRate 			= True
showTXPower 			= True
showLinkQuality 		= True
showWiFiFrequency 		= True




# name of the interface to scan RSSI on
# this is usually 'wlan0' but if you have unique interface names turned on or are using 
# external adaptors or have multiple wifi devices then this may be different
# NOTE that this value must be a python list even with just one element
# if you have multiple wireless lans you wish to check you can enter more in the list
# something like: ['wlan0', 'wlan1', 'wlan2']
RSSIInterfaceName 		= ['wlan0']


# CPU Usage 
checkCPUUsage 			= True
CPUUsageScanSeconds 	= 10

# CPU Frequency
# this can change very rapidly and is more of an indication of the load on the machine as even the 
# fastest pi will throttle back when it's mostly idle. While you can set the speed to be very fast to catch
# rapid changes that can occur in the course of normal operation keep in mind the XTdb will not record values
# faster than once a second so it may not be useful to scan faster than that unless you want to 

checkCPUFrequency 		= True
CPUFrequencyScanSeconds	= 0.2



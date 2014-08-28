# This test demonstrates how to use the ALLandMarkDetection module.
# - We first instantiate a proxy to the ALLandMarkDetection module
#     Note that this module should be loaded on the robot's NAOqi.
#     The module output its results in ALMemory in a variable
#     called "LandmarkDetected"
# - We then read this AlMemory value and check whether we get
#   interesting things.
import time
from naoqi import ALProxy

# Replace this with your robot's IP address
IP = "192.168.1.105"
PORT = 9559

# Create a proxy to ALLandMarkDetection
try:
  landMarkProxy = ALProxy("ALLandMarkDetection", IP, PORT)
except Exception, e:
  print "Error when creating landmark detection proxy:"
  print str(e)
  exit(1)

# Subscribe to the ALLandMarkDetection proxy
# This means that the module will write in ALMemory with
# the given period below
period = 500
landMarkProxy.subscribe("Test_LandMark", period, 0.0 )

# ALMemory variable where the ALLandMarkdetection module
# outputs its results
memValue = "LandmarkDetected"

# Create a proxy to ALMemory
try:
  memoryProxy = ALProxy("ALMemory", IP, PORT)
except Exception, e:
  print "Error when creating memory proxy:"
  print str(e)
  exit(1)

print "Creating landmark detection proxy"

# A simple loop that reads the memValue and checks
# whether landmarks are detected.
for i in range(0, 20):
	time.sleep(0.5)
	val = memoryProxy.getData(memValue, 0)
	if (val and isinstance(val, list)):
		print val[1][0][1][0];
	print ""
	print "\*****"
	print ""
	


# Unsubscribe from the module.
landMarkProxy.unsubscribe("Test_LandMark")
print "Test terminated successfully."

#
# License: GPLv3
# Source: https://www.pythonintro.com
# Author: pythonintro.com
#

# Using imports in python

# To import a module simply type "import" followed by module name
import time

#Test the module:
time.sleep(5)

for i in range(5):
	print("Going to sleep for 2 seconds")
	time.sleep(2)
	print("Sleeping done! I feel so rested!")
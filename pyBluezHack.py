#this script that advertises a bluetooth low energy beacon for 15 seconds

import time #1st party module

from bluetooth.ble import BeaconService #3rd party module

#instantiate the object to call for the 3rd party class
#calling for the 3rd party class
service = BeaconService()

service.start_advertising("11111111-2222-3333-4444-555555555555", 1, 1, 1, 200 )
#sleep after 15 seconds
time.sleep(15)
#stop the service
service.stop_advertising()
#printing Done
print("Done.")
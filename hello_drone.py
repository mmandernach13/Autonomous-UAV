# test program for the dronekit-sitl lib

import dronekit_sitl as ds
import dronekit as dk
import sys


sitl = ds.start_default()
conn = sitl.connection_string()

drone = dk.connect(conn, wait_ready=True)

print(f'GPS: {drone.gps_0}')


drone.close()
sitl.stop()


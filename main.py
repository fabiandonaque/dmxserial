import pyenttec as dmx
import time

port = dmx.select_port('/dev/tty.usbserial-AB0JPNBJ')
#port = dmx.select_port(0)

for i in range(512):
	port.dmx_frame[i] = 128
port.render()
time.sleep(2)

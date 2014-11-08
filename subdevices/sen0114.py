# Monitors soil moisture levels using a Raspberry Pi, MCP3008
# http://www.dfrobot.com/index.php?route=product/product&search=Moisture&description=true&product_id=599
# http://www.dfrobot.com/wiki/index.php?title=Moisture_Sensor_%28SKU:SEN0114%29
# https://github.com/mikeyroy/garden-moisture-sensors/blob/master/sensor.py

import subdevice
#import dhtreader
import spidev
#import datetime
import time

class SEN0114(subdevice.Subdevice):
	requiredData = ["measurement","pinNumber"]
	optionalData = ["unit"]
	readings = [0] * sensors
	#plot_delay = 600
	#plot_data = [''] * sensors

	spi = spidev.SpiDev()
        spi.open(0, 0)

	def __init__(self,data):
		#dhtreader.init()
		#dhtreader.lastDataTime = 0
		#dhtreader.lastData = (None,None)
		#curr_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.lastDataTime = time.time()
		self.lastData = 0

		self.sensorName = "SEN0114"
		self.pinNum = int(data["pinNumber"])
		self.min_moisture = int(data["min_moisture"]) #~3.11V instead of 1023@3.3V
		self.max_moisture = int(data["max_moisture"])
		self.diff_moisture = self.min_moisture - self.max_moisture
		self.sensors = int(data["sensors"])

		if "moisture" in data["measurement"].lower():
			self.valName = "Moisture"
			self.valUnit = "Percent water by weight or volume of soil"
			self.valSymbol = "%"
			if "unit" in data:
				if data["unit"]=="inches":
					self.valUnit = "Inches of water per foot of soil"
					self.valSymbol = "inches"
		return

	def ReadChannel(channel):
		adc = spi.xfer2([1, (8 + channel) << 4, 0])
		read_data = ((adc[1] & 3) << 8) + adc[2]
		return read_data

	def GetPercent(moisture_level):
		percent = (self.min_moisture - moisture_level) * 100 / self.diff_moisture
		if percent > 100:
			percent = 100
		if percent < 0:
			percent = 0
		return percent

	def getVal(self):
		#tm = dhtreader.lastDataTime
		tm = self.lastDataTime
		if (time.time()-tm)<2:
			#t, h = dhtreader.lastData
			m = self.lastData
		else:
			tim = time.time()
			try:
				#t, h = dhtreader.read(22,self.pinNum)
				m = ReadChannel(self.pinNum)
			except Exception:
				#t, h = dhtreader.lastData
				m = self.lastData
			#dhtreader.lastData = (t,h)
			self.lastData = m
			#dhtreader.lastDataTime=tim
			self.lastDataTime=tim
		if self.valName == "Moisture":
			percent = m
			if self.valUnit == "inches":
				percent = percent * 1.8 + 32
			return percent
		elif self.valName == "Relative_Humidity":
			return m

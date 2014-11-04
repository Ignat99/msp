import mspapi
import datetime

class Print(mspapi.Mspapi):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass
	def mspapiData(self,dataPoints):
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			print i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
		return True

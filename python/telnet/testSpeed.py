# -*- coding: utf-8 -*-
from universal import engineManager
import time

########################################
########################################
class customEngine(engineManager):
	def onConnect(self):
		print "RESET SYSTEM"
		self.cmd=[
			"*\n",
			"#>C0\n",
			"#>D0\n",
			"#>E0\n",
			"#>F0\n",
		]
		#commands
		self.commands={
				">":"OUTPUT",
				"<":"INPUT",
				"~":"ANALOG"
		}
		#set thread tick
		#self.setTick(0.001)
		self.switch=0
	#
	def filterData(self,data):
		try:
			data=data[1:-1]
			return [self.commands[data[0]],ord(data[1])-65,int(data[2:])]
		except:
			return ["","*",data]
			
	def onData(self,engine,data):
		#filter data
		#print data
		m,p,v=self.filterData(data)
		print "[%s] PIN:%s VAL:%s" % (m,p,v)
		
		#POLLING #################################
		#self.sendCmd("#<F\n")
		if self.switch>0:
			self.switch=0
		else:
			self.switch=1
		#apply to 2 out at the same time!
		self.sendCmd("#>G%d\n#>H%d\n#~A\n" % (self.switch,self.switch))
		
		#self.sendCmd("#>H%d\n" % self.switch)
		#self.sendCmd("#~A\n")
		##########################################
		
	def setPin(self,pin,status):
		self.sendCmd("#>%s%s\n" % (pin,status))
		
########################################
########################################
########################################
if __name__=="__main__":
	#
	#status 
	e=customEngine("192.168.1.177")
	
	#send command
	#time.sleep(3)
	#set pin C to 1
	#e.setPin("C",1)
	
	
	

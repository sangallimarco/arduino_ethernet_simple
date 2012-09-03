# -*- coding: utf-8 -*-
from universal import engineManager
from threading import Thread
import time

########################################
class actionTimer(Thread):
	def __init__(self,actions,callback):
		Thread.__init__(self)
		self.actions=actions
		self.callback=callback
		self.start()
		
	def run(self):
		while len(self.actions)>0:
			cmd,t=self.actions.pop(0)
			print "SENDING CMD: %s" % cmd[:-1]
			self.callback(cmd)
			#
			time.sleep(t)
			
########################################
class pinger(Thread):
	def __init__(self,callback):
		Thread.__init__(self)
		self.callback=callback
		self.start()
		
	def run(self):
		while 1:
			print "SENDING PING"
			self.callback("#~A0\n")
			#
			time.sleep(1)
		
########################################
class customEngine(engineManager):
	def __init__(self,host):
		engineManager.__init__(self,host)
		
		#@@@p=pinger(self.sendCmd)
		
	def onConnect(self):
			print "RESET SYSTEM"
			#append 
			self.cmd=[
				"*\n",
				"#>E0\n",
				"#>F0\n",
				"#>G0\n",
				"#>H0\n",
			]+self.cmd
			#set thread tick
			#self.setTick(0.5)
	
	def onData(self,engine,data):
		print "DATA FROM ARDUINO: %s" % data[:-1]
		
	def pumpsOn(self,on=10,off=2):
		#pass all to a timer
		cmd=[
			["#>E1\n",on],
			["#>E0\n",off],

			["#>F1\n",on],
			["#>F0\n",off],

			["#>G1\n",on],
			["#>G0\n",off],

			["#>H1\n",on],
			["#>H0\n",off],
		]
		#
		t=actionTimer(cmd,self.sendCmd)

########################################
if __name__=="__main__":
	e=customEngine("192.168.1.177")
	#send command
	time.sleep(2)
	while 1:
		#pumps on!
		e.pumpsOn(2,1)
		#
		time.sleep(20)
		print "----------------"

			
			
			
			

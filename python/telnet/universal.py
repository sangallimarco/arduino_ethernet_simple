# -*- coding: utf-8 -*-
import urllib,re,time
import telnetlib
from threading import Thread
import time


class engineManager(Thread):
	def __init__(self,host):
		Thread.__init__(self)
		self.host=host
		self.alive=True;
		#undefined status
		self.status=-1
		self.cmd=[]
		self.buffer=""
		#immediately apply
		self.delay=0.01
		#connect
		self.connect()
		#start thread
		self.start()
		
	def connect(self):
		#@@@print "CONNECTING..."
		try:
			self.conn=telnetlib.Telnet(self.host)
		except:
			time.sleep(3)
			self.connect()
		else:
			self.onConnect()
		#
		return self.conn
		
	def run(self):
		while self.alive:
			#send cmd from buffer
			self.__sendFromBuffer()
			#read 
			empty=False
			while not empty:
				empty=self.__readFromBuffer()
		
	def __sendFromBuffer(self):
		#send only if buffer is not empy
		if len(self.cmd) > 0:
			cmd=self.cmd[0]
			#try to send message
			try:
				#@@@print "SENDING > %s" % cmd
				self.conn.write(cmd)
			except:
				#reconnect
				self.connect()
			else:
				#remove message and push into res
				self.cmd.pop(0)
					
	def __readFromBuffer(self):
			try:
				res= self.conn.read_until("\n",self.delay)
			except:
				#reconnect
				self.connect()
			else:
				#check if empty, read function return empty if no data available
				self.buffer="%s%s" % (self.buffer,res)
				#
				if "\n" not in self.buffer:
					return True
				else:
					#send to callback
					self.onData(self,self.buffer)
					self.buffer=""
					#
					return False

	#push command into buffer
	def sendCmd(self,cmd):
		self.cmd.append(cmd)
		
	def setTick(self,delay):
		self.delay=delay
		
	#---------------------------------
	def onConnect(self):
		pass
		
	def onData(self,data):
		pass
		



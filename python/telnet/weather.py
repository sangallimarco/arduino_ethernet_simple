# -*- coding: utf-8 -*-
import urllib,re,time
from gardenController import *
import math

#yahoo ##########################################################################
def getWeather():
	re_red=re.compile('DB0000">([\-0-9\.]+)')
	re_green=re.compile('429108">([0-9\.]+)')
	re_purple=re.compile('C000DB">([0-9\.]+)')
	#gettemp=re.compile("\<dd\>([0-9]+)[\ ]+\°C\</dd\>")

	url="""http://www.centrometeolombardo.com/Moduli/stazioni.php?erbacentro"""
	page = urllib.urlopen(url)
	content=page.read()
	#
	red=re_red.findall(content)
	green=re_green.findall(content)
	purple=re_purple.findall(content)

	#debug
	print red,green,purple
	
	#remap
	res={
		"temp":int(float(red[0])),
		"hum":int(float(red[1])),
		"wind":int(float(green[0])),
		"rain":int(float(red[4])),
	}
	#print res
	return res
	
#ilmeteo.it ########################################################################
def getWeather_():
	getparams=re.compile('[\:\w\>]{1}([0-9]+)[\&\°\%]{1}')
	url="""http://www.ilmeteo.it/box/previsioni.php?citta=853&type=real1"""
	page = urllib.urlopen(url)
	content=re.sub("[\ \t\n\r]+","",page.read().split('"situazione"')[1])
	#fix 0 wind
	content=content.replace("assente",":0&")
	#print content
	params=getparams.findall(content)
	#print params

	#remap
	keys=[
		"temp",
		"hum",
		"wind",
	]
	#convert to int
	values=[(int(x)) for x in params]	
	res=dict(zip(keys,values))
	
	return res
	
#####################################################
if __name__=="__main__":
	#status 
	e=customEngine("192.168.1.46")
	running=False
	#-----------------------------------------------
	#triggers
	ht=21
	wt=10
	tt=25
	#dalay
	delay=60*5
	#-----------------------------------------------
	while 1:
		#current Hour
		h=time.localtime()[3]
		print "CURRENT TIME: %s" % h
		
		#get weather site data
		try:
			w=getWeather()
			print "WEATHER DATA: %s" % w
		except:
			pass
			#raise
		else:
			#check params
			if h>ht:
				print "RESET"
				running=False
			elif not running and w["rain"]<1 and w["hum"]<90 and w["wind"]<wt and w["temp"]>=tt and h==ht:
				print "SYSTEM ON"
				running=True
				#irrigation time x pump
				e.pumpsOn(delay)
			 
		#next loop within...
		time.sleep(180)	
		
		


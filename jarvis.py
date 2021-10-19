#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
JARVIS - Just Another Really Very Intelligent System
'''

import daemon
import time
import RPi.GPIO as GPIO
from optparse import OptionParser

def main():
  print "Starting AI..."

if __name__ == "__main__":
  parser=OptionParser()

# Options for the command line.

  # Debug
  parser.add_option ("-v", action="store_true", dest="verbose")
  parser.add_option ("-d", action="store_true", dest="rundaemon")
	
	# Configuration file

	
	(options,args)=parser.parse_args()
  
	# Print start up message
	print "Starting AI..."
  
  if (rundaemon is true):
    with daemon.DaemonContext():
        main()
  else:
    # Run the main program in the foreground.
    main()

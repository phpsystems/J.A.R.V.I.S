import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def setup (openp, closed): 
	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
	GPIO.setup(openp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(closed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def determinePosition (openp, closed, desiredstate=closed)
    if GPIO.input(openp) == GPIO.HIGH:
        print("Helmet is open!")

    elif GPIO.input(closed) == GPIO.HIGH:
        print("Helmet is closed!")

    else: 
    	if (desiredstate is closed):

	    		closeHelmet ()
	 	else:
	 		openHelmet ()



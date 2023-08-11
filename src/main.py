#!/usr/bin/python
#
#
# =++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#       ____     _    __     ____                                __     _             ____       
#      / __ )   (_)  / /_   / __/  ____    _____  ___    _____  / /_   (_)   ____    / __/  ____ 
#     / __  |  / /  / __/  / /_   / __ \  / ___/ / _ \  / ___/ / __/  / /   / __ \  / /_   / __ \
#    / /_/ /  / /  / /_   / __/  / /_/ / / /    /  __/ (__  ) / /_   / /   / / / / / __/  / /_/ /
#   /_____/  /_/   \__/  /_/     \____/ /_/     \___/ /____/  \__/  /_/   /_/ /_/ /_/     \____/ 
#                                                                                              
# =++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                     
#
#                                                                          Suraj Singh Bisht
#                                                                          surajsinghbisht054@gmail.com
#
# 
#
#           This Script Is A Part Of RC-AIA Framework.
#           Created For Educational And Practise purpose Only.
#			Please Don't Remove Author Initials.
#
#

__author__ 	    = "Suraj Singh Bisht"
__description__ = "Self Driving Phase One"
__version__	    = "Beta"
__date__	    = "OCT, 2018"
__email__	    = "surajsinghbisht054@gmail.com"


from server_stream import DStream
from config import WINDOW_PREVIEWER
from machine_view import DetectTrack
from utili import FocusRegion, resize
from utili import imshow



# For Server
def desktop_main():

	# Automatic Content Closing Method
	with DStream() as obj:
		# machine view
		machine_view_obj = DetectTrack()
		# Continouse Image Receiving
		while True:
			if True:
				# Image Received 
				# Image in Original Form
				im  = obj.getimage()

				
				#im = resize(im)
				# Image Without Any Processing
				machine_view_obj.setimg(im)

				adjustment = False

				# Adjustment For Rasbi Pi Car
				#adjustment =  [[200,400],[824,400]]
				
				adjustment = [[200, 240],[440,240]] #--> 640,480
				im, offset, movement = machine_view_obj.highlight(adjustment)
				
				im = resize(im)
				if imshow('Processed Image View', im):
					break
			else:
			#except Exception as e:
				#print "[ Error Occured : ]", e
				break

	return




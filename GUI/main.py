import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.app import App
#The imports we use for our GUI

class MainBoxLayout(BoxLayout):
	leftaudio = True
	rightaudio = True
	leftvolume = 0
	rightvolume = -20
	leftmute = False
	rightmute = False

	def __init__(self, MainController):
		BoxLayout.__init__(self)
		self.MainController = MainController

	def volumevalue(self):
		global leftaudio
		global rightaudio
		global leftvolume
		global rightvolume
		
		if self.leftaudio is True:
			return self.leftvolume
		
		if self.rightaudio is True:
			return self.rightvolume

	def left(self, instance, value):
		global leftaudio
		global leftvolume
		global leftmute

		if value is True:
			print("Left is True")
			self.leftaudio = True
			self.slider(self, self.leftvolume)	
			self.checkbox_mute(self, self.leftmute)
		else:
			print("Left is False")
			self.leftaudio = False

	def right(self, instance, value):
		global rightaudio
		global rightvolume
		global rightmute

		if value is True:
			print("Right is True")
			self.rightaudio = True
			self.slider(self, self.rightvolume)
			self.checkbox_mute(self, self.rightmute)
		else:
			print("Right is False")
			self.rightaudio = False

	def both(self, instance, value):
		global leftaudio
		global rightaudio
		global leftmute
		global rightmute
		global leftvolume
		global rightvolume

		if value is True:
			print("Both is True")
			self.leftaudio = True
			self.rightaudio = True
			if self.leftmute is self.rightmute:
				self.checkbox_mute(self, self.rightmute)
			else:
				self.checkbox_mute(self, False)

			if self.leftvolume is self.rightvolume:
				self.slider(self, self.rightvolume)
			else:
				self.slider(self, 0)
		else:
			print("Both is False")
			self.leftaudio = False
			self.rightaudio = False
#Radiobuttons for left- and rightaudio. This will set the left/right or both to True or False to change those settings.

	def slider(self, instance, value):
		global leftaudio
		global rightaudio
		global leftvolume
		global rightvolume
		
		if self.leftaudio is True:
			self.leftvolume = value
			self.value = self.leftvolume
			print("leftaudio")
			print("The volume has changed: " + str(value) + " db")
		
		if self.rightaudio is True:
			self.rightvolume = value
			print("rightaudio")	
			print("The volume has changed: " + str(value) + " db")
#		self.MainController.changeVolume(value, self.leftaudio, self.rightaudio)
#This function will print the volume when it has changed.

	def checkbox_mute(self, instance, value):		
		global leftaudio
		global rightaudio
		global leftmute
		global rightmute		

		if value is True:
			if self.leftaudio is True:
				self.leftmute = True
				print("Left is muted")

			if self.rightaudio is True:
				self.rightmute = True
				print("Right is muted")
		else:
			if self.leftaudio is True:
				self.leftmute = False
				print("Left is unmuted")
			
			if self.rightaudio is True:
				self.rightmute = False
				print("Right is unmuted")
#This function will print Checkbox Checked when the checkbox is checked en Checkbox unchecked when the checkbox is not checked

class MyApp(App):
	def __init__(self, MainController):
		App.__init__(self)
		self.MainController = MainController

	def build(self):
		return MainBoxLayout(self.MainController)

	def on_stop(self):
		print("Closed")
#		self.MainController.close()
		
#This wil run MyApp class which will run my.kv and MainBoxLayout.

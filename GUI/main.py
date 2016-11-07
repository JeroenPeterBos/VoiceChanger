import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.label import Label
from kivy.uix.slider import Slider
#The imports we use for our GUI

class MainBoxLayout(BoxLayout):
	def __init__(self, MainController):
		BoxLayout.__init__(self)
		self.MainController = MainController
	
	def validate(self, instance, value):
		if(value == ""):
			value = "0"
			
		print("The delay has changed: " + value + " seconds")
#This function will print the delay when it is changed. 

	def left(self, instance, value):
		if value is True:
			print("Left is True")
			self.leftaudio = BooleanProperty(True)
		else:
			print("Left is False")
			self.leftaudio = BooleanProperty(False)

	def right(self, instance, value):
		if value is True:
			print("Right is True")
			self.rightaudio = BooleanProperty(True)
		else:
			print("Right is False")
			self.rightaudio = BooleanProperty(False)

	def both(self, instance, value):
		if value is True:
			print("Both is True")
			self.leftaudio = BooleanProperty(True)
			self.rightaudio = BooleanProperty(True)
		else:
			print("Both is False")
			self.leftaudio = BooleanProperty(False)
			self.rightaudio = BooleanProperty(False)
#Radiobuttons for left- and rightaudio. This will set the left/right or both to True or False to change those settings.

	def slider(self, instance, value):
		print("The volume has changed: " + str(value) + " db")
#		self.MainController.changeVolume(value, self.leftaudio, self.rightaudio)
#This function will print the volume when it has changed.

	def checkbox_mute_clicked(self, instance, value):
		if value is True:
			print("Muted")
		else:
			print("Unmuted")
#This function will print Checkbox Checked when the checkbox is checked en Checkbox unchecked when the checkbox is not checked


	def switch_on(self, instance, value):
		if value is True:
			print("Distortion is on")
		else:
			print("Distortion is off")
#This function will print Switch on when the switch is turned on and Switch off when the switch is turned of, in the console.

class MyApp(App):
	def __init__(self, MainController):
		App.__init__(self)
		self.MainController = MainController

	def build(self):
		return MainBoxLayout(self.MainController)
#This wil run MyApp class which will run my.kv and MainBoxLayout.

import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty
#The imports we use for our GUI

class MainBoxLayout(BoxLayout):
	def __init__(self, MainController):
		BoxLayout.__init__(self)
		self.MainController = MainController


	def checkbox_mute_clicked(self, instance, value):
		if value is True:
			print("Checkbox Checked")
		else:
			print("Checkbox Unchecked")
#This function will print Checkbox Checked when the checkbox is checked en Checkbox unchecked when the checkbox is not checked


	def switch_on(self, instance, value):
		if value is True:
			print("Switch On")
		else:
			print("Switch Off")
#This function will print Switch on when the switch is turned on and Switch off when the switch is turned of, in the console.

class MyApp(App):
	def __init__(self, MainController):
		App.__init__(self)
		self.MainController = MainController


	def build(self):
		return MainBoxLayout(self.MainController)
#This wil run MyApp class which will run my.kv and MainBoxLayout.

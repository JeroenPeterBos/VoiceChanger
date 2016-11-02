import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#The imports we use for our GUI

class MainBoxLayout(BoxLayout):
	def switch_on(self, instance, value):
		if value is True:
			print("Switch On")
		else:
			print("Switch Off")
#This function will print Switch on when the switch is turned on and Switch off when the switch is turned of, in the console.

class MyApp(App):
	def build(self):
		return MainBoxLayout()


my_app = MyApp()
my_app.run()
#This wil run MyApp class which will run my.kv and MainBoxLayout.

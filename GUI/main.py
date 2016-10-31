import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.9.1')

class Controller(BoxLayout):
	def __init__(self):
		super(Controller, self). __init__()

	def new_thickness(self, *args):
        	self.lbl.text = str(int(args[1])) + "%"


class MyApp(App):
	def build(self):
		return Controller()

window = MyApp()
window.run()

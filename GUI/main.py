from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.boxlayout import BoxLayout

class Controller(BoxLayout):
	def __init__(self):
		super(Controller, self), __init__()

	def new_thickness(self, *args):
        	self.lbl.text = str(int(args[1]))
        	self.lbl.font_size = int(args[1]) * 6 + 10


class MyApp(App):
	def build(self):
		return Controller()

window = MyApp()
window.run()

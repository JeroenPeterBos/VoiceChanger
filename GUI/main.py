import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider

def callback(instace, value):
	print('the switch', instance, 'is', value)

switch Switch()

	

if __name__ == '__main__':
	class MyApp(App):
		def build(self):
			return RootWidget(Widget)

	MyApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as color
from kivy.config import Config
from kivy.base import EventLoop
from kivy.graphics import Line,Color 
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior

Config.set('graphics','width','960')
Config.set('graphics','height','540')


from kivy.core.window import Window

class RadioButton(ToggleButton):
	def _do_press(self):
		if(self.state == 'normal'):
			ToggleButtonBehavior._do_press(self)

class Canvas(Widget):
	lwidth = 2
	current_color = "#000000"
	current_bgcolor = "#FFFFFF"
	def on_touch_down(self, touch):
		if Widget.on_touch_down(self, touch):
			return
		with self.canvas:
			touch.ud['current_line'] = Line(points=(touch.x, touch.y),width=self.lwidth)

	def on_touch_move(self, touch):
		if 'current_line' in touch.ud:
			if(touch.x>100 and touch.y>25):
				touch.ud['current_line'].points+=(touch.x, touch.y)


	def clr(self):
		saved = self.children[:]
		self.clear_widgets()
		self.canvas.clear()
		for widget in saved:
			self.add_widget(widget)		

	def set_color(self,newcolor):
		self.current_color = newcolor
		self.canvas.add(Color(*self.current_color))	
	
	def set_bgcolor(self):
		self.current_bgcolor = self.current_color
		Window.clearcolor = list(self.current_bgcolor)		

	def set_line_width(self,newwidth):
		lw = {'Thin':2,'Normal':3,'Thick':5}	
		self.lwidth = lw[newwidth]

class paintApp(App):
	
	def build(self):
		self.icon = 'icon.png'
		self.canvas_widget = Canvas()
		return self.canvas_widget
		
	
			

if __name__ == '__main__':
	Window.clearcolor = color("#FFFFFF")
	paintApp().run()		
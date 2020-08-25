import random
from random import choice
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.popup import Popup 

kivy.require('1.11.1')

__version__ = "1.11.1"


class PantallaPrincipal(BoxLayout):
	pass

class P(BoxLayout):
	def azar(self):
		datos = ['El primer alunizaje fue en el año 1969', 'La palabra astronomía viene de las palabras "astro" (estrella en latín) y "nomos" (regla, orden)',
		'El primer hombre en ir al espacio fue el cosmonauta Ruso Yuri Gagarin', 'Actualmente, SpaceX es la única compañía privada en mandar seres humanos al espacio',
		'"Un pequeño paso para el hombre, un gran paso para la humanidad", fueron las famosas palabras pronunciadas por Neil Armnstrong en la superficie lunar',
		'El telescopio privado más grande del mundo está en Pearson College, Cánada', 'Saturno tiene 4 grandes anillos, pero realmente tiene muchos más', 'La primera mujer en ir al espacio fue la Cosmonauta rusa Valentina Tereshkova',
		'La montaña más grande de nuestro sistema solar está en Marte. El monte Olimpus tiene una altitud de 24 KM', 'El primer ser vivo en ir al espacio fue una perra rusa llamada Laika']

		randomizer = choice(datos)
		
		return randomizer

def show_popup():
	show = P()

	popupwindow = Popup(title='Dato al azar', content=show, size_hint=(None, None), size=(400, 400))

	popupwindow.open()

class PantallaInfo(Screen):
	pass

class AgujerosNegros(Screen):
	pass

class Misiones(Screen):
	pass

class EnergiaOscura(Screen):
	pass

class Exoplanetas(Screen):
	pass

class Galaxias(Screen):
	pass

class Telescopios(Screen):
	pass

class LasEstrellas(Screen):
	pass

class DatoAlAzar(Screen):
	def btn(self):
		show_popup()

class Bibliografia(Screen):
	pass

class WindowManager(ScreenManager):
	pass

class AstronoMeApp(App):
	popup = P()

if __name__ == '__main__':
	AstronoMeApp().run() 
from tkinter import Button, Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
root=Widget()
f1=BoxLayout(
    b1=Button(text='one')
)
root.add_widget(f1)




class InstaApp(App):
    pass





InstaApp().run()
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatingMenu(App):
    def build(self):
        layout = FloatLayout()
        btn = Button(text='Check Status', size_hint=(0.4, 0.1), pos_hint={'x':0.3, 'y':0.5})
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    FloatingMenu().run()


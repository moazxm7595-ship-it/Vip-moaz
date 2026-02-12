from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class VIPMenu(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Auto Headshot: OFF', background_color=(1, 0, 0, 1)))
        layout.add_widget(Button(text='ESP Name: OFF', background_color=(0, 0, 1, 1)))
        layout.add_widget(Button(text='Speed Hack: 1x'))
        return layout

if __name__ == '__main__':
    VIPMenu().run()


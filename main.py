from kivy.app import App
from kivy.uix.label import Label

class CJApp(App):
    def build(self):
        return Label(text="CJ Asistan Çalışıyor!", font_size='20sp')

if __name__ == "__main__":
    CJApp().run()

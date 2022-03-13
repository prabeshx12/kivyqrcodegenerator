from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
import qrcode
Window.clearcolor = (1, 1, 1, 1)


class MyLayout(Widget):
    def clear(self):
        self.data.text = ''
        self.save_as.text = ''

    def convert(self):
        data = self.data.text
        save_as = self.save_as.text
        if save_as != '':
            img = qrcode.make(data)
            img.save(f"{save_as}.jpg")
            self.data.text = ''
            self.save_as.text = ''
        else:
            self.save_as.text = 'Please enter the filename'


class MyApp(App):
    def build(self):
        self.title = '7XQRCode'
        return MyLayout()



if __name__ == '__main__':
    MyApp().run()
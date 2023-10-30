from kivy.uix.button import Button
import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


class MyWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWindow, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.913, 0.866, 0.788, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.padding = (20, 50)
        self.orientation = 'horizontal'

        button_layout = RelativeLayout(size_hint=(None, None), size=(250, 200), pos_hint={'x': 0.1, 'y': 0.2})

        button1 = Button(text='Goods', size_hint=(None, None), size=(200, 100), pos_hint={'x': 0, 'y': 1})
        button1.background_color = (1, 1, 1, 1)
        button1.pressed = False
        button1.bind(on_press=self.change_button_color)
        button2 = Button(text='Services', size_hint=(None, None), size=(200, 100), pos_hint={'x': 0, 'y': 0.2})
        button2.background_color = (1, 1, 1, 1)
        button2.pressed = False
        button2.bind(on_press=self.change_button_color)

        button_layout.add_widget(button1)
        button_layout.add_widget(button2)

        self.add_widget(button_layout)
        with self.canvas:
            Color(0.2, 0.2, 0.2, 1)
            self.line = Line(points=[250, 0, 250, 1000], width=2)

        right_layout = RelativeLayout(size_hint=(None, None), size=(600, 400), pos_hint={'center_x': 0.8, 'center_y': 0.5})

        scroll_view = ScrollView(do_scroll_y=True)
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        text_input = TextInput(text="Пример текста", size_hint=(1, None), height=800, readonly=True)

        scroll_layout.add_widget(text_input)
        scroll_view.add_widget(scroll_layout)
        right_layout.add_widget(scroll_view)

        self.add_widget(right_layout)

    @staticmethod
    def change_button_color(instance):
        if instance.pressed:
            instance.background_color = (1, 1, 1, 1)
        else:
            instance.background_color = (0.2, 0.2, 0.2, 1)
        instance.pressed = not instance.pressed

    def on_size(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class MyApp(App):
    def build(self):
        self.title = "Zooshop"
        return MyWindow()


if __name__ == '__main__':
    MyApp().run()

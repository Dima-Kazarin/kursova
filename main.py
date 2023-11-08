from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import mysql.connector

Window.clearcolor = (247 / 255, 237 / 255, 208 / 255, 1)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'zooshop',
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()


class ZooshopApp(App):
    def build(self):
        # root = BoxLayout(orientation='horizontal', spacing=10)
        root = BoxLayout(orientation='horizontal', size=(250, 100), size_hint=(None, None),
                  spacing=500, pos_hint={'top': .5})

        goods_button = Button(text='Goods', background_color=(0, 0, 0, 1), size=(200, 100), size_hint=(None, None),
                              on_press=self.change_button_color)
        goods_button.pressed = False
        services_button = Button(text='Services', background_color=(0, 0, 0, 1), size=(200, 100), size_hint=(None, None),
                                 on_press=self.change_button_color)
        services_button.pressed = False

        button_layout = BoxLayout(orientation='vertical', spacing=100)
        aside = AnchorLayout(anchor_x='left', anchor_y='center', padding=(30, 0))

        aside.add_widget(button_layout)

        button_layout.add_widget(goods_button)
        button_layout.add_widget(services_button)

        scrollview = ScrollView(size=(1000, 500), size_hint=(None, None), pos=(200, 50))

        grid_layout = GridLayout(cols=3, spacing=20, size_hint_y=1.5, padding=(0, 50), pos=(250, 250))
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        cursor.execute("SELECT name_good, price, vendor_code FROM goods")
        temp = cursor.fetchall()

        for i in temp:
            box_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=(20, 50), spacing=25)
            label_name = Label(text=f"Name: {i[0]}", color=(0, 0, 0, 1))
            box_layout.add_widget(label_name)
            label_price = Label(text=f"Price: {i[1]}", color=(0, 0, 0, 1))
            box_layout.add_widget(label_price)
            label_vendor_code = Label(text=f"Vendor Code: {i[2]}", color=(0, 0, 0, 1))
            box_layout.add_widget(label_vendor_code)
            grid_layout.add_widget(box_layout)

        scrollview.add_widget(grid_layout)
        root.add_widget(aside)
        root.add_widget(scrollview)

        return root

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


if __name__ == '__main__':
    ZooshopApp().run()

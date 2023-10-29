from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from uuid import uuid4
from kivy.uix.scrollview import ScrollView

Window.clearcolor = (247 / 255, 237 / 255, 208 / 255, 1)

animals = [['1', 'Barsik', 'cat', 'ser', 'Dima'],
           ['2', 'Sam', 'dog', 'se', 'Anatoliy'],
           ['2', 'Sam', 'dog', 'se', 'Anatoliy'],
           ['3', 'dog', 'hamster', 's', 'Nika'],
           ['3', 'dog', 'hamster', 's', 'Nika']]

clients = [['1', 'Dima', '+380975954281', '19-01-2005'],
           ['2', 'Anatoliy', '+3807573152', '29-11-2004'],
           ['2', 'Anatoliy', '+3807573152', '29-11-2004'],
           ['2', 'Anatoliy', '+3807573152', '29-11-2004'],
           ['2', 'Anatoliy', '+3807573152', '29-11-2004'],
           ['3', 'Nika', '+38012321321', '12-02-2005']]

goods = [['1', 'osheynik', '300', '001'],
         [str(uuid4()), 'osheynik', '400', '002'],
         [str(uuid4()), 'osheynik', '400', '002'],
         [str(uuid4()), 'osheynik', '400', '002'],
         [str(uuid4()), 'osheynik', '400', '002'],
         [str(uuid4()), 'osheynik', '500', '003'],
         [str(uuid4()), 'osheynik', '500', '003'],
         [str(uuid4()), 'osheynik', '500', '003'],
         [str(uuid4()), 'osheynik', '500', '003'],
         [str(uuid4()), 'osheynik', '500', '003'],
         [str(uuid4()), 'osheynik', '500', '003'],
         [str(uuid4()), 'osheynik', '500', '003']]

service = [['1', 'cat', '300', 'service1'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['2', 'cat', '400', 'service2'],
           ['3', 'dog', '500', 'service3']]


class TableApp(App):
    def __init__(self, table, **kwargs):
        self.table = table
        super(TableApp, self).__init__(**kwargs)

    @staticmethod
    def add_buttons(add_layout, edit_layout, delete_layout, button_layout, id_input, field_input, change_input,
                    del_id_input,
                    *args):
        add_layout.add_widget(Label(text='Add', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))

        for i in range(len(args)):
            add_layout.add_widget(args[i])

        add_layout.add_widget(Button(text='add', background_color=(0, 0, 0, 1), size=(100, 30),
                                     size_hint=(None, None)))

        edit_layout.add_widget(Label(text='Edit', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
        edit_layout.add_widget(id_input)
        edit_layout.add_widget(field_input)
        edit_layout.add_widget(change_input)
        edit_layout.add_widget(Button(text='edit', background_color=(0, 0, 0, 1), size=(100, 30),
                                      size_hint=(None, None)))

        delete_layout.add_widget(Label(text='Delete', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
        delete_layout.add_widget(del_id_input)
        delete_layout.add_widget(Button(text='delete', background_color=(0, 0, 0, 1), size=(100, 30),
                                        size_hint=(None, None)))

        button_layout.add_widget(add_layout)
        button_layout.add_widget(edit_layout)
        button_layout.add_widget(delete_layout)

    @staticmethod
    def add_items_to_layout(layout, button_layout, anchor, *args):
        for i in range(len(args)):
            layout.add_widget(args[i])

        root = ScrollView(size_hint=(None, None), size=(700, 300), scroll_y=0)
        root.add_widget(layout)
        button_layout.add_widget(root)
        anchor.add_widget(button_layout)

    @staticmethod
    def add_columns(*args):
        for i in args:
            i[0].add_widget(i[1])
            i[0].add_widget(Label(text='-----------', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))

    @staticmethod
    def add_fields_to_table(table, *args):
        for i in table:
            if len(args) == 5:
                args[0].add_widget(Label(text=i[0], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[1].add_widget(Label(text=i[1], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[2].add_widget(Label(text=i[2], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[3].add_widget(Label(text=i[3], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[4].add_widget(Label(text=i[4], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
            elif len(args) == 4:
                args[0].add_widget(Label(text=i[0], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[1].add_widget(Label(text=i[1], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[2].add_widget(Label(text=i[2], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[3].add_widget(Label(text=i[3], size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))

    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(None, 1.5), padding=[120, 0])
        id_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        name_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        kind_of_animal_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        button_layout = BoxLayout(orientation='horizontal', spacing=90, size_hint=(None, None), pos=(100, 250))
        add_layout = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        edit_layout = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        delete_layout = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        anchor = AnchorLayout(anchor_x='left', anchor_y='center')

        kind_of_animal = Label(text='kind_of_animal', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
        id = Label(text='id', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
        price_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
        price = Label(text='price', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

        id_input = TextInput(size_hint=(None, None), size=(150, 30),
                             hint_text='Enter id to modify')
        field_input = TextInput(size_hint=(None, None), size=(150, 30),
                                hint_text='Enter field to modify')
        change_input = TextInput(size_hint=(None, None), size=(150, 30),
                                 hint_text='Enter data to change')
        del_id_input = TextInput(size_hint=(None, None), size=(150, 30),
                                 hint_text='Enter id to delete')
        animal_input = TextInput(size_hint=(None, None), size=(150, 30),
                                 hint_text='Enter kind of animal')
        name_input = TextInput(size_hint=(None, None), size=(150, 30),
                               hint_text='Enter name')

        if self.table == 'animals':
            services_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
            owner_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            nickname = Label(text='nickname', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            services = Label(text='services', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            owner = Label(text='owner', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            services_input = TextInput(size_hint=(None, None), size=(150, 30),
                                       hint_text='Enter services')
            owner_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter owner')

            self.add_columns([id_l, id], [name_l, nickname], [kind_of_animal_l, kind_of_animal], [services_l, services],
                             [owner_l, owner])
            self.add_fields_to_table(animals, id_l, name_l, kind_of_animal_l, services_l, owner_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, name_l, kind_of_animal_l, services_l, owner_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, id_input, field_input, change_input,
                             del_id_input, name_input, animal_input, services_input, owner_input)

            return anchor
        elif self.table == 'clients':
            phone_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
            birth_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            name = Label(text='name', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            phone = Label(text='Phone number', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            birth = Label(text='Birth date', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            phone_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter phone number')
            birth_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter birth date')

            self.add_columns([id_l, id], [name_l, name], [phone_l, phone], [birth_l, birth])
            self.add_fields_to_table(clients, id_l, name_l, phone_l, birth_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, name_l, phone_l, birth_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, id_input, field_input, change_input,
                             del_id_input, name_input, phone_input, birth_input)

            return anchor
        elif self.table == 'goods':
            vendor_code_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            name_good = Label(text='name good', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            vendor_code = Label(text='vendor code', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            id = Label(text='guid', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            price_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter price')
            vendor_input = TextInput(size_hint=(None, None), size=(150, 30),
                                     hint_text='Enter vendor code')

            self.add_columns([id_l, id], [name_l, name_good], [price_l, price], [vendor_code_l, vendor_code])
            self.add_fields_to_table(goods, id_l, name_l, price_l, vendor_code_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, BoxLayout(size_hint=(None, None), width=100),
                                     name_l, price_l, vendor_code_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, id_input, field_input, change_input,
                             del_id_input,
                             name_input, price_input, vendor_input)

            return anchor
        elif self.table == 'services':
            title_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            title = Label(text='title', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            price_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter price')
            title_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter title')

            self.add_columns([id_l, id], [kind_of_animal_l, kind_of_animal], [price_l, price], [title_l, title])
            self.add_fields_to_table(service, id_l, kind_of_animal_l, price_l, title_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, kind_of_animal_l, price_l, title_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, id_input, field_input, change_input,
                             del_id_input,
                             animal_input, price_input, title_input)

            return anchor


class AdminApp(App):
    def build(self):
        animals_button = Button(text='Animals', background_color=(0, 0, 0, 1), size=(100, 30), size_hint=(None, None),
                                on_press=self.press_button)
        clients_button = Button(text='Clients', background_color=(0, 0, 0, 1), size=(100, 30), size_hint=(None, None),
                                on_press=self.press_button)
        goods_button = Button(text='Goods', background_color=(0, 0, 0, 1), size=(100, 30), size_hint=(None, None),
                              on_press=self.press_button)
        services_button = Button(text='Services', background_color=(0, 0, 0, 1), size=(100, 30), size_hint=(None, None),
                                 on_press=self.press_button)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(.2, None))

        anchor = AnchorLayout(anchor_x='center', anchor_y='center')

        button_layout.add_widget(animals_button)
        button_layout.add_widget(clients_button)
        button_layout.add_widget(goods_button)
        button_layout.add_widget(services_button)

        anchor.add_widget(button_layout)

        return anchor

    def press_button(self, instance):
        table = instance.text.lower()
        self.stop()
        TableApp(table).run()


class StartApp(App):
    def build(self):
        self.title = 'Shop'

        goods_button = Button(text='Goods', background_color=(0, 0, 0, 1), size=(200, 50), size_hint=(None, None))
        services_button = Button(text='Services', background_color=(0, 0, 0, 1), size=(200, 50), size_hint=(None, None))

        client_label = Label(text='Client', size_hint=(None, None), size=(200, 10), color=(0, 0, 0, 1), bold=True,
                             font_size=20)
        name_label = Label(text='Name - Anaaaksa', size=(200, 10), color=(0, 0, 0, 1), size_hint=(.9, None))
        birth_label = Label(text='Birth date - 19.11.2000', size=(200, 10), color=(0, 0, 0, 1), size_hint=(1.15, None))
        phone_label = Label(text='Phone number - +9821234561', size_hint=(None, None), size=(150, 10),
                            color=(0, 0, 0, 1))
        animals_label = Label(text='Animals: cat, dog', size=(200, 10), color=(0, 0, 0, 1), size_hint=(.8, None))

        button_layout = BoxLayout(orientation='vertical', spacing=100)
        aside = AnchorLayout(anchor_x='left', anchor_y='center')
        label_layout = BoxLayout(orientation='vertical', size_hint=(None, None), spacing=90, pos_hint={'top': .4})
        client_layout = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(5, .8))
        layout = BoxLayout(orientation='horizontal', size=(250, 100), size_hint=(None, None), pos=(0, 200),
                           spacing=250, pos_hint={'top': .5})

        button_layout.add_widget(goods_button)
        button_layout.add_widget(services_button)

        client_layout.add_widget(client_label)

        label_layout.add_widget(client_layout)
        label_layout.add_widget(name_label)
        label_layout.add_widget(birth_label)
        label_layout.add_widget(phone_label)
        label_layout.add_widget(animals_label)

        aside.add_widget(button_layout)

        layout.add_widget(aside)
        layout.add_widget(label_layout)

        return layout


class RegistrationApp(App):
    def build(self):
        self.title = 'Authorization'

        login_button = Button(text='Login', background_color=(0, 0, 0, 1), size=(150, 10), size_hint=(None, None),
                              pos_hint={'center_x': 0.4}, on_press=self.press_login)
        register_button = Button(text='Register', background_color=(0, 0, 0, 1), size=(150, 10), size_hint=(None, None),
                                 pos_hint={'center_x': 0.4}, on_press=self.press_login)
        admin_button = Button(text='Login as Admin', background_color=(0, 0, 0, 1), size=(150, 10),
                              size_hint=(None, None),
                              pos_hint={'center_x': 0.4}, on_press=self.press_admin)

        aut_label = Label(text='Authorization', size_hint=(1.2, None), size=(100, 70), color=(0, 0, 0, 1), bold=True)
        log_label = Label(text='Login', size_hint=(.17, None), size=(100, 10), color=(0, 0, 0, 1))
        password_label = Label(text='Password', size_hint=(.27, None), size=(100, 10), color=(0, 0, 0, 1))
        birth_label = Label(text='Birth date', size_hint=(.27, None), size=(100, 10), color=(0, 0, 0, 1))
        phone_label = Label(text='Phone number', size_hint=(.4, None), size=(100, 10), color=(0, 0, 0, 1))

        login = TextInput(size_hint=(None, None), size=(220, 30),
                          hint_text='Enter your login', pos=(100, 100))
        password = TextInput(size_hint=(None, None), size=(220, 30),
                             hint_text='Enter your password', pos=(100, 80), password=True)
        birth_date = TextInput(size_hint=(None, None), size=(220, 30),
                               hint_text='Enter your birth date', pos=(100, 60))
        phone_number = TextInput(size_hint=(None, None), size=(220, 30),
                                 hint_text='Enter your phone number', pos=(100, 40))

        log_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        pas_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        date_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        phone_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        button_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=25)

        anchor = AnchorLayout(anchor_x='center', anchor_y='center', pos_hint={'top': .95})
        layout = BoxLayout(orientation='vertical', pos=(300, 220), size=(180, 200), size_hint=(None, None), spacing=40)

        log_layout.add_widget(log_label)
        log_layout.add_widget(login)

        pas_layout.add_widget(password_label)
        pas_layout.add_widget(password)

        date_layout.add_widget(birth_label)
        date_layout.add_widget(birth_date)

        phone_layout.add_widget(phone_label)
        phone_layout.add_widget(phone_number)

        button_layout.add_widget(login_button)
        button_layout.add_widget(register_button)
        button_layout.add_widget(admin_button)

        layout.add_widget(aut_label)
        layout.add_widget(log_layout)
        layout.add_widget(pas_layout)
        layout.add_widget(date_layout)
        layout.add_widget(phone_layout)

        layout.add_widget(BoxLayout(size_hint=(1, 1)))
        layout.add_widget(button_layout)

        anchor.add_widget(layout)

        return anchor

    def press_login(self, instance):
        self.stop()
        StartApp().run()

    def press_admin(self, instance):
        self.stop()
        AdminApp().run()


if __name__ == '__main__':
    RegistrationApp().run()

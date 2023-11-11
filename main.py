from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from uuid import uuid4
from kivy.uix.scrollview import ScrollView
import mysql.connector
from datetime import datetime

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'zooshop',
    'raise_on_warnings': True,
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

Window.clearcolor = (247 / 255, 237 / 255, 208 / 255, 1)


class GoodsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.goods_button = Button(text='Goods', background_color=(0, 0, 0, 1), size=(200, 50), size_hint=(None, None),
                                   on_press=self.press_goods)
        self.services_button = Button(text='Services', background_color=(0, 0, 0, 1), size=(200, 50),
                                      size_hint=(None, None), on_press=self.press_services)

    def build(self):
        root = BoxLayout(orientation='horizontal', size=(250, 100), size_hint=(None, None),
                         spacing=500, pos_hint={'top': .5})

        self.goods_button.disabled = True

        button_layout = BoxLayout(orientation='vertical', spacing=100)
        aside = AnchorLayout(anchor_x='left', anchor_y='center')

        aside.add_widget(button_layout)

        button_layout.add_widget(self.goods_button)
        button_layout.add_widget(self.services_button)

        scrollview = ScrollView(size=(1000, 500), size_hint=(None, None), pos=(200, 50))

        grid_layout = GridLayout(cols=3, spacing=20, size_hint_y=1.5, padding=(0, 50), pos=(250, 250))
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        cursor.execute("SELECT name_good, price, vendor_code FROM goods")
        goods = cursor.fetchall()

        for i in goods:
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

    def press_goods(self, instance):
        instance.disabled = True
        self.services_button.disabled = False

    def press_services(self, instance):
        instance.disabled = True
        self.goods_button.disabled = False


class TableApp(App):
    def __init__(self, table, **kwargs):
        self.del_id_input = None
        self.change_input = None
        self.field_input = None
        self.id_input = None
        self.table = table
        self.title_input = None
        self.vendor_input = None
        self.price_input = None
        self.birth_input = None
        self.phone_input = None
        self.password_input = None
        self.name_input = None
        self.animal_input = None
        self.owner_input = None

        super(TableApp, self).__init__(**kwargs)

    def press_add(self, instance):
        if self.table == 'animals':
            nickname = self.name_input.text
            kind_of_animal = self.animal_input.text
            owner = self.owner_input.text

            cursor.execute('INSERT INTO animals (nickname, kind_of_animal, owner) VALUES (%s, %s, %s)',
                           [nickname, kind_of_animal, owner])
        elif self.table == 'clients':
            name = self.name_input.text
            phone_number = self.phone_input.text
            birth_day = self.birth_input.text
            password = self.password_input.text
            date_format = '%d-%m-%Y'
            date_obj = datetime.strptime(birth_day, date_format)

            cursor.execute('INSERT INTO `clients` (name, phone_number, birth_day, password) VALUES (%s, %s, %s, %s)',
                           [name, int(phone_number), date_obj, password])
        elif self.table == 'goods':
            name_good = self.name_input.text
            price = self.price_input.text
            vendor_code = self.vendor_input.text

            cursor.execute('INSERT INTO `goods` (id, name_good, price, vendor_code) VALUES (%s, %s, %s, %s)',
                           [str(uuid4()), name_good, int(price), int(vendor_code)])
        elif self.table == 'services':
            kind_of_animal = self.animal_input.text
            price = self.price_input.text
            title = self.title_input.text

            cursor.execute('INSERT INTO `services` (kind_of_animal, price, title) VALUES (%s, %s, %s)',
                           [kind_of_animal, int(price), title])

        conn.commit()
        self.stop()
        self.run()

    def press_edit(self, instance):
        change_id = self.id_input.text
        field = self.field_input.text
        change = self.change_input.text
        cursor.execute(f'UPDATE {self.table} SET {field} = %s WHERE id = %s', [change, change_id])
        conn.commit()

        self.stop()
        self.run()

    def press_delete(self, instance):
        del_id = self.del_id_input.text
        cursor.execute(f'DELETE FROM {self.table} WHERE id = %s', (del_id,))
        conn.commit()

        self.stop()
        self.run()

    def press_back(self, instance):
        self.stop()
        AdminApp().run()

    def add_buttons(self, add_layout, edit_layout, delete_layout, button_layout, id_input, field_input, change_input,
                    del_id_input,
                    *args):
        add_layout.add_widget(Label(text='Add', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))

        for i in range(len(args)):
            add_layout.add_widget(args[i])

        add_layout.add_widget(Button(text='add', background_color=(0, 0, 0, 1), size=(150, 30),
                                     size_hint=(None, None), on_press=self.press_add))

        edit_layout.add_widget(Label(text='Edit', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
        edit_layout.add_widget(id_input)
        edit_layout.add_widget(field_input)
        edit_layout.add_widget(change_input)
        edit_layout.add_widget(Button(text='edit', background_color=(0, 0, 0, 1), size=(150, 30),
                                      size_hint=(None, None), on_press=self.press_edit))

        delete_layout.add_widget(Label(text='Delete', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
        delete_layout.add_widget(del_id_input)
        delete_layout.add_widget(Button(text='delete', background_color=(0, 0, 0, 1), size=(150, 30),
                                        size_hint=(None, None), on_press=self.press_delete))

        button_layout.add_widget(add_layout)
        button_layout.add_widget(edit_layout)
        button_layout.add_widget(delete_layout)
        button_layout.add_widget(Label(size=(100, 30), size_hint=(None, None)))
        button_layout.add_widget(Button(text='<-', background_color=(0, 0, 0, 1), size=(100, 30),
                                        size_hint=(None, None), on_press=self.press_back))

    @staticmethod
    def add_items_to_layout(layout, button_layout, anchor, *args):
        for i in range(len(args)):
            layout.add_widget(args[i])

        root = ScrollView(size_hint=(None, None), size=(700, 300), scroll_y=0, do_scroll_x=False)
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
                args[0].add_widget(Label(text=str(i[0]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[1].add_widget(Label(text=str(i[1]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[2].add_widget(Label(text=str(i[2]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[3].add_widget(Label(text=str(i[3]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[4].add_widget(Label(text=str(i[4]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
            elif len(args) == 4:
                args[0].add_widget(Label(text=str(i[0]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[1].add_widget(Label(text=str(i[1]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[2].add_widget(Label(text=str(i[2]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))
                args[3].add_widget(Label(text=str(i[3]), size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None)))

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

        self.id_input = TextInput(size_hint=(None, None), size=(150, 30),
                                  hint_text='Enter id to modify')
        self.field_input = TextInput(size_hint=(None, None), size=(150, 30),
                                     hint_text='Enter field to modify')
        self.change_input = TextInput(size_hint=(None, None), size=(150, 30),
                                      hint_text='Enter data to change')
        self.del_id_input = TextInput(size_hint=(None, None), size=(150, 30),
                                      hint_text='Enter id to delete')

        self.animal_input = TextInput(size_hint=(None, None), size=(150, 30),
                                      hint_text='Enter kind of animal')
        self.name_input = TextInput(size_hint=(None, None), size=(150, 30),
                                    hint_text='Enter name')

        if self.table == 'animals':
            self.owner_input = TextInput(size_hint=(None, None), size=(150, 30),
                                         hint_text='Enter owner')

            owner_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            nickname = Label(text='nickname', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            owner = Label(text='owner', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            cursor.execute('SELECT * FROM animals')
            animals = cursor.fetchall()

            self.add_columns([id_l, id], [name_l, nickname], [kind_of_animal_l, kind_of_animal],
                             [owner_l, owner])
            self.add_fields_to_table(animals, id_l, name_l, kind_of_animal_l, owner_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, name_l, kind_of_animal_l, owner_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, self.id_input, self.field_input,
                             self.change_input, self.del_id_input,
                             self.name_input, self.animal_input, self.owner_input)

            return anchor
        elif self.table == 'clients':
            phone_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
            birth_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))
            password_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            name = Label(text='name', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            phone = Label(text='phone number', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            birth = Label(text='birth date', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            password = Label(text='password', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            self.phone_input = TextInput(size_hint=(None, None), size=(150, 30),
                                         hint_text='Enter phone number')
            self.birth_input = TextInput(size_hint=(None, None), size=(150, 30),
                                         hint_text='Enter birth date')
            self.password_input = TextInput(size_hint=(None, None), size=(150, 30),
                                            hint_text='Enter password')

            cursor.execute('SELECT * FROM clients')
            clients = cursor.fetchall()

            self.add_columns([id_l, id], [name_l, name], [phone_l, phone], [birth_l, birth], [password_l, password])
            self.add_fields_to_table(clients, id_l, name_l, phone_l, birth_l, password_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, name_l, phone_l, birth_l, password_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, self.id_input, self.field_input,
                             self.change_input, self.del_id_input,
                             self.name_input, self.phone_input, self.birth_input, self.password_input)

            return anchor
        elif self.table == 'goods':
            vendor_code_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            name_good = Label(text='name good', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            vendor_code = Label(text='vendor code', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))
            id = Label(text='id', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            self.price_input = TextInput(size_hint=(None, None), size=(150, 30),
                                         hint_text='Enter price')
            self.vendor_input = TextInput(size_hint=(None, None), size=(150, 30),
                                          hint_text='Enter vendor code')

            cursor.execute('SELECT * FROM goods')
            goods = cursor.fetchall()

            self.add_columns([id_l, id], [name_l, name_good], [price_l, price], [vendor_code_l, vendor_code])
            self.add_fields_to_table(goods, id_l, name_l, price_l, vendor_code_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, BoxLayout(size_hint=(None, None), width=100),
                                     name_l, price_l, vendor_code_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, self.id_input, self.field_input,
                             self.change_input, self.del_id_input,
                             self.name_input, self.price_input, self.vendor_input)

            return anchor
        elif self.table == 'services':
            title_l = BoxLayout(orientation='vertical', spacing=15, size_hint=(None, None))

            title = Label(text='title', size=(50, 10), color=(0, 0, 0, 1), size_hint=(None, None))

            self.price_input = TextInput(size_hint=(None, None), size=(150, 30),
                                         hint_text='Enter price')
            self.title_input = TextInput(size_hint=(None, None), size=(150, 30),
                                         hint_text='Enter title')

            cursor.execute('SELECT * FROM services')
            service = cursor.fetchall()

            self.add_columns([id_l, id], [kind_of_animal_l, kind_of_animal], [price_l, price], [title_l, title])
            self.add_fields_to_table(service, id_l, kind_of_animal_l, price_l, title_l)
            self.add_items_to_layout(layout, button_layout, anchor, id_l, kind_of_animal_l, price_l, title_l)
            self.add_buttons(add_layout, edit_layout, delete_layout, button_layout, self.id_input, self.field_input,
                             self.change_input,
                             self.del_id_input,
                             self.animal_input, self.price_input, self.title_input)

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
    def __init__(self, user_id, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id

    def build(self):
        self.title = 'Shop'

        cursor.execute('SELECT name, phone_number, birth_day FROM clients WHERE id = %s', (self.user_id,))
        user_info = cursor.fetchone()

        cursor.execute('SELECT nickname FROM animals WHERE owner = %s', (user_info[0],))
        animals = [j for i in cursor.fetchall() for j in i]
        user_animal = ', '.join(i for i in animals)

        goods_button = Button(text='Goods', background_color=(0, 0, 0, 1), size=(200, 50), size_hint=(None, None),
                              on_press=self.press_goods)
        services_button = Button(text='Services', background_color=(0, 0, 0, 1), size=(200, 50), size_hint=(None, None))

        client_label = Label(text='Client', size_hint=(None, None), size=(200, 10), color=(0, 0, 0, 1), bold=True,
                             font_size=20)
        name_label = Label(text=f'Name - {user_info[0]}', size=(200, 10), color=(0, 0, 0, 1), size_hint=(None, None))
        birth_label = Label(text=f'Birth date - {str(user_info[2])}', size=(200, 10), color=(0, 0, 0, 1),
                            size_hint=(None, None))
        phone_label = Label(text=f'Phone number - {user_info[1]}', size_hint=(2, None), size=(150, 10),
                            color=(0, 0, 0, 1))
        animals_label = Label(text=f'Animals: {user_animal}', size=(200, 10), color=(0, 0, 0, 1),
                              size_hint=(None, None))

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

    def press_goods(self, instance):
        self.stop()
        GoodsApp().run()


class RegistrationApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login = TextInput(size_hint=(None, None), size=(220, 30), hint_text='Enter your login', pos=(100, 100))
        self.password = TextInput(size_hint=(None, None), size=(220, 30),
                                  hint_text='Enter your password', pos=(100, 80), password=True)
        self.birth_date = TextInput(size_hint=(None, None), size=(220, 30),
                                    hint_text='Enter your birth date', pos=(100, 60))
        self.phone_number = TextInput(size_hint=(None, None), size=(220, 30),
                                      hint_text='Enter your phone number', pos=(100, 40))
        self.a_label = Label(size_hint=(1.1, None), size=(100, 10), color=(1, 0, 0, 1), bold=True)

    def build(self):
        self.title = 'Authorization'

        login_button = Button(text='Login', background_color=(0, 0, 0, 1), size=(150, 10), size_hint=(None, None),
                              pos_hint={'center_x': 0.4}, on_press=self.press_login)
        register_button = Button(text='Register', background_color=(0, 0, 0, 1), size=(150, 10), size_hint=(None, None),
                                 pos_hint={'center_x': 0.4}, on_press=self.press_register)
        admin_button = Button(text='Login as Admin', background_color=(0, 0, 0, 1), size=(150, 10),
                              size_hint=(None, None),
                              pos_hint={'center_x': 0.4}, on_press=self.press_admin)

        aut_label = Label(text='Authorization', size_hint=(1.2, None), size=(100, 70), color=(0, 0, 0, 1), bold=True)
        log_label = Label(text='Login', size_hint=(.17, None), size=(100, 10), color=(0, 0, 0, 1))
        password_label = Label(text='Password', size_hint=(.27, None), size=(100, 10), color=(0, 0, 0, 1))
        birth_label = Label(text='Birth date', size_hint=(.27, None), size=(100, 10), color=(0, 0, 0, 1))
        phone_label = Label(text='Phone number', size_hint=(.4, None), size=(100, 10), color=(0, 0, 0, 1))

        log_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        pas_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        date_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        phone_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=10)
        button_layout = BoxLayout(orientation='vertical', size=(250, 30), size_hint=(None, None), spacing=25)

        anchor = AnchorLayout(anchor_x='center', anchor_y='center', pos_hint={'top': .95})
        layout = BoxLayout(orientation='vertical', pos=(300, 220), size=(180, 200), size_hint=(None, None), spacing=40)

        log_layout.add_widget(log_label)
        log_layout.add_widget(self.login)

        pas_layout.add_widget(password_label)
        pas_layout.add_widget(self.password)

        date_layout.add_widget(birth_label)
        date_layout.add_widget(self.birth_date)

        phone_layout.add_widget(phone_label)
        phone_layout.add_widget(self.phone_number)

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
        layout.add_widget(self.a_label)

        anchor.add_widget(layout)

        return anchor

    def press_login(self, instance):
        name = self.login.text
        password = self.password.text

        if name and password:
            cursor.execute('SELECT * FROM clients WHERE name = %s AND password = %s', (name, password))
            result = cursor.fetchall()
            conn.commit()

            if result:
                cursor.execute('SELECT id FROM clients WHERE name = %s', (name,))
                user_id = cursor.fetchone()[0]
                self.stop()
                StartApp(user_id).run()
            else:
                self.a_label.text = 'Name or password is incorrect'
        else:
            self.a_label.text = 'Name or password is empty'

    def press_register(self, instance):
        name = self.login.text
        phone_number = self.phone_number.text
        birth_day = self.birth_date.text
        password = self.password.text

        try:
            date_format = '%d-%m-%Y'
            date_obj = datetime.strptime(birth_day, date_format)

            if name and password and birth_day and phone_number:
                cursor.execute(
                    'INSERT INTO `clients` (name, phone_number, birth_day, password) VALUES (%s, %s, %s, %s)',
                    [name, int(phone_number), date_obj, password])
                cursor.execute('SELECT id FROM clients WHERE name = %s', (name,))
                user_id = cursor.fetchone()[0]
                conn.commit()
                self.stop()
                StartApp(user_id).run()
        except ValueError:
            self.a_label.text = 'Data is incorrect'

    def press_admin(self, instance):
        if self.login.text == 'admin' and self.password.text == 'admin':
            self.stop()
            AdminApp().run()


if __name__ == '__main__':
    RegistrationApp().run()

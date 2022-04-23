from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests


class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 3
        self.window.size_hint = (0.9, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}




        # label widget
        self.greeting = Label(
                        text= "Ник:",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (10,10),
                    size_hint= (0.1, 0.1)
                    )
        self.window.add_widget(self.user)

        self.button_pod = Button(
            text="Подгрузить",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button_pod.bind(on_press=self.pu)
        self.window.add_widget(self.button_pod)

        self.greeting2 = Label(
            text="боев:",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting2)

        self.user2 = TextInput(
                    multiline= False,
                    padding_y= (10,10),
                    size_hint= (0.5, 0.5)
                    )
        self.window.add_widget(self.user2)

        self.greeting3 = Label(
            text="",
            font_size=9,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting3)

        self.greeting3 = Label(
            text="средуха:",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting3)

        self.user3 = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(0.5, 0.5)
        )
        self.window.add_widget(self.user3)

        self.greeting4 = Label(
            text="",
            font_size=9,
            color='#00FFCE'
        )

        self.window.add_widget(self.greeting4)

        self.greeting5 = Label(
            text="надо су:",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting5)

        self.user4 = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(0.5, 0.5)
        )
        self.window.add_widget(self.user4)

        self.greeting6 = Label(
            text="",
            font_size=9,
            color='#00FFCE'
        )

        self.window.add_widget(self.greeting6)

        self.greeting7 = Label(
            text="Сессия:",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting7)

        self.user5 = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(0.5, 0.5)
        )
        self.window.add_widget(self.user5)

        self.greeting8 = Label(
            text="",
            font_size=9,
            color='#00FFCE'
        )

        self.window.add_widget(self.greeting8)

        # button widget
        self.button = Button(
                      text= "Результат",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.itog)
        self.window.add_widget(self.button)

        self.greeting9 = Label(
            text="",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting9)
        self.greeting10 = Label(
            text="",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting10)
        self.greeting11 = Label(
            text="",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting11)
        self.greeting12 = Label(
            text="",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting12)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting9.text = "Хай " + self.user.text + "!"
        self.user4.text = self.user.text

    def pu(self, instance):
        nickname = self.user.text
        r = requests.get(
            f'https://api.wotblitz.ru/wotb/account/list/?application_id=a5bbb5e7abf6e5746d519a1485fad676&search={nickname}&limit=1')
        data = r.json()

        account_id = data["data"][0]["account_id"]

        t = requests.get(
            f'https://api.wotblitz.ru/wotb/account/info/?application_id=a5bbb5e7abf6e5746d519a1485fad676&account_id={account_id}')
        stat = t.json()
        stat = stat["data"][f"{account_id}"]["statistics"]["all"]
        self.battles = stat["battles"]
        self.wins = stat["wins"]
        self.damage_dealt = stat["damage_dealt"]
        self.cy = round(self.damage_dealt / self.battles)
        self.pp = round(self.wins / self.battles * 100, 2)

        self.user2.text = f'{self.battles}'
        self.user3.text = f'{self.cy}'
        #self.user2.insert_text(battles, from_undo=False)
        #self.user3.text = cy.text
        self.greeting9.text = f"hi {nickname}"# cy {self.cy}, pp {self.pp}"


    def itog(self, instance):
        rez = round((int(self.user2.text) * int(self.user3.text) - int(self.user2.text) * int(self.user4.text)) / (
                int(self.user4.text) - int(self.user5.text)), 0)
        self.greeting12.text = f"Нужно еще {rez} боев чтобы апнуть {self.user4.text} су"

# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
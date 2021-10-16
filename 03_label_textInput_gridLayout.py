from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        # self.cols = 3
        # self.cols = 4
        # self.cols = 6
        ########################################################################
        # self.add_widget(Label(text='Name: '))
        # self.name = TextInput(multiline=False) # Only One Line
        # self.add_widget(self.name)
        ########################################################################
        self.add_widget(Label(text='First Name: '))
        self.first_name = TextInput(multiline=False) # Only One Line
        self.add_widget(self.first_name)

        self.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        ########################################################################


class MyApp(App):
    def build(self):
        return MyGrid()


################################################################################
if __name__ == '__main__':
    MyApp().run()
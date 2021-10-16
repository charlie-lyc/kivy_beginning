from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ########################################################################
        # self.cols = 2

        # self.add_widget(Label(text='First Name: '))
        # self.first_name = TextInput(multiline=False)
        # self.add_widget(self.first_name)
        # self.add_widget(Label(text='Last Name: '))
        # self.last_name = TextInput(multiline=False)
        # self.add_widget(self.last_name)
        # self.add_widget(Label(text='Email: '))
        # self.email = TextInput(multiline=False)
        # self.add_widget(self.email)
        ########################################################################
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='First Name: '))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)
        self.inside.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)
        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        ########################################################################
        self.cols = 1

        self.add_widget(self.inside)

        self.submit = Button(text='Submit', font_size=30)
        self.submit.bind(on_press=self.press_on) # Actual Event: 'on_release' (when button clicked)
        self.add_widget(self.submit)

    def press_on(self, instance):
        # print('Button Pressed')

        ## Get Value from Text Input
        first_name = self.first_name.text
        last_name = self.last_name.text
        email = self.email.text
        print('Name: {} {}, Email: {}'.format(first_name, last_name, email))
        ## Clear Text Input
        self.first_name.text = ''
        self.last_name.text = ''
        self.email.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


################################################################################
if __name__ == '__main__':
    MyApp().run()
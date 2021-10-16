from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    first_name = ObjectProperty()
    last_name = ObjectProperty()
    email = ObjectProperty()

    def press_on(self): # No Need 'instance'
        # print('Button Pressed')

        ## Get Value from Text Input
        print('Name: {} {}, Email: {}'.format(
            self.first_name.text,
            self.last_name.text,
            self.email.text
        ))
        ## Clear Text Input
        self.first_name.text = ''
        self.last_name.text = ''
        self.email.text = ''


class KivyApp(App):
    def build(self):
        return MyGrid()


################################################################################
if __name__ == '__main__':
    KivyApp().run()
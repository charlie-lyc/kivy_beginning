from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect1 = Rectangle(pos=(0, 0), size=(50, 50))
            Color(1, 1, 0, 0.5, mode='rgba')
            self.rect2 = Rectangle(pos=(100, 100), size=(100, 100))
            Color(1, 1, 1, 0.5, mode='rgba')
            ## from (x1, y1) point to (x2, y2) point, then to (x3, y3) point
            Line(points=(300, 300, 500, 500, 60, 500))

    def on_touch_down(self, touch):
        print('Mouse Down', touch)
        self.rect1.pos = touch.pos

    def on_touch_move(self, touch):
        print('Mouse Move', touch)
        self.rect2.pos = touch.pos

    def on_touch_up(self, touch):
        print('Mouse Up', touch)


## Window Title: 'Canvas'
class CanvasApp(App):
    def build(self):
        return Touch()


################################################################################
if __name__ == '__main__':
    CanvasApp().run()
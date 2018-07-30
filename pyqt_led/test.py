
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from pyqt_led import Led
# import numpy as np
import sys


class Test(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._layout = QHBoxLayout(self)
        self._create_leds()
        self._arrange_leds()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def _create_leds(self):
        self._led_1 = Led(self)
        self._led_2 = Led(self, on_color=Led.blue, shape=Led.capsule)
        self._led_3 = Led(self, off_color=Led.red, shape=Led.circle)
        self._led_4 = Led(self, shape=Led.rectangle)
        self._led_4.set_on_color(Led.orange)
        self._led_5 = Led(self, on_color=Led.purple, off_color=Led.yellow)
        self._led_5.set_shape(Led.circle)
        self._led_5.setFixedSize(80, 50)

    def _arrange_leds(self):
        self._layout.addWidget(self._led_1)
        self._layout.addWidget(self._led_2)
        self._layout.addWidget(self._led_3)
        self._layout.addWidget(self._led_4)
        self._layout.addWidget(self._led_5)


app = QApplication(sys.argv)
test = Test()
test.show()
sys.exit(app.exec_())

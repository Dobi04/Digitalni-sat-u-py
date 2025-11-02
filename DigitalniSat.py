import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(700,300,400,100)
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Digital clock")
        
        self.time_label = QLabel(self)
        self.time_label.setStyleSheet("color: #00e34c;"
                                      "font-size: 150px;")
        
        font_id = QFontDatabase.addApplicationFont("DS-DIGIB.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        
        self.timer = QTimer(self)
        
        VBox = QVBoxLayout()
        VBox.addWidget(self.time_label)
        self.setLayout(VBox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.timer.timeout.connect(self.UbdateTime)
        self.timer.start(100)
        
    def UbdateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)
        
        
def main():
    app=QApplication(sys.argv)
    window=DigitalClock()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
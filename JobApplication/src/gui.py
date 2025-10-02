from PySide6.QtWidgets import QApplication, QWidget
import sys

class GUI:
    def __init__(self):
        pass
    
    @staticmethod
    def run():
        app = QApplication(sys.argv)
        window = QWidget()
        window.show()
        app.exec()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
import sys
import requests

from PyQt5 import QtWidgets

from DesktopProgram.sample.sample import Ui_MainWindow
from DesktopProgram.utils import load_configs, get_address

CONFIG = dict()


if __name__ == "__main__":
    CONFIG = load_configs()
    session = requests.Session()
    ADDRESS_SERVER = get_address(CONFIG)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(session, ADDRESS_SERVER)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

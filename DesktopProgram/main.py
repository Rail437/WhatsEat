import sys
import requests
import json

from PyQt5 import QtWidgets

from DesktopProgram.sample_program.sample import Ui_WhatsEat
from DesktopProgram.utils import load_configs, get_address

CONFIG = dict()


if __name__ == "__main__":
    CONFIG = load_configs()
    session = requests.Session()
    ADDRESS_SERVER = get_address(CONFIG)

    # Response server (TEST)
    # with open('answer_server_2.json', 'w') as f:
    #     answer = session.get('http://185.46.8.32:8080/whatseat/api/v1/dishes?products=')
    #     json.dump(answer.json(), f)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_WhatsEat(session, ADDRESS_SERVER)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

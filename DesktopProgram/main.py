import sys
import requests
import json

from PyQt5 import QtCore, QtGui, QtWidgets

from DesktopProgram.sample_program.sample import Ui_WhatsEat
from DesktopProgram.utils import load_configs, get_address, get_items_response, get_response_server, get_image_address


CONFIG = dict()


class WhatsEatApp(Ui_WhatsEat):
    def __init__(self, session, ADDRESS_SERVER):
        self.session = session
        self.ADDRESS_SERVER = ADDRESS_SERVER
        self.list_answer_recipes = dict()
        self.list_view_recipes = 0
        self.max_list_recipes = 0
        self.images_recipes = dict()
        
    def setupUi(self, WhatsEat):
        super(WhatsEatApp, self).setupUi(WhatsEat)
        self.menu_search.clicked.connect(self.__get_search_window)
        self.menu_login.clicked.connect(self.__get_login_window)
        self.menu_help.clicked.connect(self.__get_help_window)
        self.__get_search_window()

    
    def __get_search_window(self):
        self.__clear_content(self.content_area)
        self.__get_search_panel_window()

    def __get_login_window(self):
        self.__clear_content(self.content_area)
        login_panel = QtWidgets.QWidget(self.content_area)
        login_panel.setGeometry(QtCore.QRect(213, 123, 400, 240))
        login_panel.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                       "border-radius: 10px;")
        login_panel.setObjectName("login_panel")
        registration_btn = QtWidgets.QPushButton(login_panel)
        registration_btn.setGeometry(QtCore.QRect(50, 154, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        registration_btn.setFont(font)
        registration_btn.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                            "border-radius: 10px;")
        registration_btn.setObjectName("registration_btn")
        registration_btn.setText("РЕГИСТРАЦИЯ")
        registration_btn.clicked.connect(self.__get_registration_window)
        auth_btn = QtWidgets.QPushButton(login_panel)
        auth_btn.setGeometry(QtCore.QRect(50, 24, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        auth_btn.setFont(font)
        auth_btn.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                    "border-radius: 10px;")
        auth_btn.setObjectName("auth_btn")
        auth_btn.setText("АВТОРИЗАЦИЯ")
        auth_btn.clicked.connect(self.__get_auth_window)
        login_panel.show()

    def __get_auth_window(self):
        self.__clear_content(self.content_area)
        auth_panel = QtWidgets.QWidget(self.content_area)
        auth_panel.setGeometry(QtCore.QRect(213, 37, 400, 386))
        auth_panel.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                      "border-radius: 10px;")
        auth_panel.setObjectName("auth_panel")
        login_label = QtWidgets.QLabel(auth_panel)
        login_label.setGeometry(QtCore.QRect(26, 22, 211, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        login_label.setFont(font)
        login_label.setStyleSheet("color: rgb(255, 255, 255);")
        login_label.setObjectName("login_label")
        login_label.setText("Введите логин:")
        password_label = QtWidgets.QLabel(auth_panel)
        password_label.setGeometry(QtCore.QRect(26, 137, 261, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        password_label.setFont(font)
        password_label.setStyleSheet("color: rgb(255, 255, 255);")
        password_label.setObjectName("password_label")
        password_label.setText("Введите пароль:")
        input_password = QtWidgets.QLineEdit(auth_panel)
        input_password.setGeometry(QtCore.QRect(26, 191, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_password.setFont(font)
        input_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 5px;\n"
                                          "")
        input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        input_password.setObjectName("input_password")
        input_login = QtWidgets.QLineEdit(auth_panel)
        input_login.setGeometry(QtCore.QRect(26, 61, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_login.setFont(font)
        input_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 5px;")
        input_login.setObjectName("input_login")
        auth_btn = QtWidgets.QPushButton(auth_panel)
        auth_btn.setGeometry(QtCore.QRect(50, 299, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        auth_btn.setFont(font)
        auth_btn.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                      "border-radius: 10px;")
        auth_btn.setObjectName("pushButton")
        auth_btn.setText("АВТОРИЗАЦИЯ")
        auth_btn.clicked.connect(lambda: self._send_request_validation_user(input_login.text(), input_password.text()))
        auth_panel.show()

    def __get_help_window(self):
        self.__clear_content(self.content_area)
        help_panel = QtWidgets.QWidget(self.content_area)
        help_panel.setGeometry(QtCore.QRect(0, 0, 868, 583))
        font = QtGui.QFont()
        font.setPointSize(16)
        help_panel.setFont(font)
        help_panel.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                      "border-radius: 10px;")
        help_panel.setObjectName("help_panel")
        feedback_btn = QtWidgets.QPushButton(help_panel)
        feedback_btn.setGeometry(QtCore.QRect(434, 542, 371, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        feedback_btn.setFont(font)
        feedback_btn.setStyleSheet("color: rgb(255, 255, 255);")
        feedback_btn.setObjectName("feedback_btn")
        feedback_btn.setText("Остались вопросы - напишите нам.")
        feddback_icon_btn = QtWidgets.QPushButton(help_panel)
        feddback_icon_btn.setGeometry(QtCore.QRect(817, 542, 36, 26))
        feddback_icon_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/feedback/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        feddback_icon_btn.setIcon(icon3)
        feddback_icon_btn.setIconSize(QtCore.QSize(36, 26))
        feddback_icon_btn.setObjectName("feddback_icon_btn")
        text_area = QtWidgets.QLabel(help_panel)
        text_area.setGeometry(QtCore.QRect(21, 24, 826, 506))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        text_area.setFont(font)
        text_area.setStyleSheet("color: rgb(255, 255, 255);")
        text_area.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        text_area.setObjectName("text_area")
        text_area.setText("Как пользоваться программой.")
        help_panel.show()

    def __get_search_panel_window(self):
        search_panel_form = QtWidgets.QWidget(self.content_area)
        search_panel = QtWidgets.QWidget(search_panel_form)
        search_panel.setGeometry(QtCore.QRect(5, 5, 858, 99))
        search_panel.setMinimumSize(QtCore.QSize(858, 99))
        search_panel.setMaximumSize(QtCore.QSize(858, 99))
        search_panel.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: rgb(56, 56, 56);")
        search_panel.setObjectName("search_panel")
        search_label = QtWidgets.QLabel(search_panel)
        search_label.setGeometry(QtCore.QRect(20, 22, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        search_label.setFont(font)
        search_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 18pt \"Times New Roman\";")
        search_label.setObjectName("label")
        search_label.setText("Поиск:")
        input_product = QtWidgets.QLineEdit(search_panel)
        input_product.setGeometry(QtCore.QRect(10, 52, 667, 32))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        input_product.setFont(font)
        input_product.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-top-left-radius: 5px;\n"
                                         "border-bottom-left-radius: 5px;\n"
                                         "border-top-right-radius: 0;\n"
                                         "border-bottom-right-radius: 0;")
        input_product.setObjectName("lineEdit")
        search_recipes = QtWidgets.QPushButton(search_panel)
        search_recipes.setGeometry(QtCore.QRect(676, 52, 170, 32))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        search_recipes.setFont(font)
        search_recipes.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                          "border-radius:5px;\n"
                                          "border-top-left-radius: 0;\n"
                                          "border-bottom-left-radius: 0;")
        search_recipes.setObjectName("search_recipes")
        search_recipes.setText("Подобрать рецепт")
        search_recipes.clicked.connect(lambda x: self._send_request_recipes(input_product.text()))
        list_recipes = QtWidgets.QWidget(search_panel_form)
        list_recipes.setGeometry(QtCore.QRect(5, 136, 858, 447))
        list_recipes.setObjectName("list_recipes")
        search_panel_form.show()

    def __get_registration_window(self):
        self.__clear_content(self.content_area)
        registration_panel = QtWidgets.QWidget(self.content_area)
        registration_panel.setGeometry(QtCore.QRect(213, 37, 400, 447))
        registration_panel.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                              "border-radius: 10px;")
        registration_panel.setObjectName("registration_panel")
        login_label = QtWidgets.QLabel(registration_panel)
        login_label.setGeometry(QtCore.QRect(26, 22, 311, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        login_label.setFont(font)
        login_label.setStyleSheet("color: rgb(255, 255, 255);")
        login_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        login_label.setObjectName("login_label")
        login_label.setText("Придумайте логин:")
        password_label = QtWidgets.QLabel(registration_panel)
        password_label.setGeometry(QtCore.QRect(26, 125, 301, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        password_label.setFont(font)
        password_label.setStyleSheet("color: rgb(255, 255, 255);")
        password_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        password_label.setObjectName("password_label")
        password_label.setText("Придумайте пароль:")
        input_password = QtWidgets.QLineEdit(registration_panel)
        input_password.setGeometry(QtCore.QRect(26, 157, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_password.setFont(font)
        input_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 5px;\n"
                                          "")
        input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        input_password.setObjectName("input_password")
        input_login = QtWidgets.QLineEdit(registration_panel)
        input_login.setGeometry(QtCore.QRect(26, 51, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_login.setFont(font)
        input_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 5px;")
        input_login.setObjectName("input_login")
        registration_btn = QtWidgets.QPushButton(registration_panel)
        registration_btn.setGeometry(QtCore.QRect(50, 354, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        registration_btn.setFont(font)
        registration_btn.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                            "border-radius: 10px;")
        registration_btn.setObjectName("registration_btn")
        registration_btn.setText("РЕГИСТРАЦИЯ")
        password_verification_label = QtWidgets.QLabel(registration_panel)
        password_verification_label.setGeometry(QtCore.QRect(26, 231, 300, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        password_verification_label.setFont(font)
        password_verification_label.setStyleSheet("color: rgb(255, 255, 255);")
        password_verification_label.setObjectName("password_verification_label")
        input_password_verification = QtWidgets.QLineEdit(registration_panel)
        input_password_verification.setGeometry(QtCore.QRect(25, 265, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_password_verification.setFont(font)
        input_password_verification.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "border-radius: 5px;\n"
                                                       "")
        input_password_verification.setEchoMode(QtWidgets.QLineEdit.Password)
        input_password_verification.setObjectName("input_password_verification")
        password_verification_label.setText("Повторите пароль:")
        registration_panel.show()

    def __get_next_recipes(self):
        if self.list_view_recipes < self.max_list_recipes:
            self.list_view_recipes += 1
            self.__getting_recipes(self.list_answer_recipes[str(self.list_view_recipes)])

    def __get_button_load_more(self):
        load_more = QtWidgets.QPushButton(self.content_area)
        load_more.setGeometry(QtCore.QRect(360, 546, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        load_more.setFont(font)
        load_more.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                     "border-radius: 5px;")
        load_more.setObjectName("load_more")
        load_more.clicked.connect(self.__get_next_recipes)
        load_more.setText("Загрузить еще")
        load_more.show()

    def __preparation_form(self, recipe:dict, target, geometry:dict):
        recipe_form = QtWidgets.QWidget(target)
        recipe_form.setGeometry(QtCore.QRect(geometry['x'], geometry['y'], 268, 384))
        recipe_form.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                  "border-radius: 10px;")
        recipe_form.setObjectName("recipe")
        recipe_image = QtWidgets.QLabel(recipe_form)
        recipe_image.setGeometry(QtCore.QRect(10, 11, 248, 170))
        recipe_image.setText("")
        try:
            pixmap = QtGui.QPixmap()
            # pixmap.load('http://185.46.8.32:8080/whatseat/sample/img/vanilnyy-pirog-s-klubnikoy-v-chashke-medium.jpg')
            pixmap.loadFromData(self.images_recipes[str(recipe["id"])])
            # recipe_image.setPixmap(QtGui.QPixmap(recipe['img']))
            recipe_image.setPixmap(pixmap)
        except Exception:
            recipe_image.setPixmap(QtGui.QPixmap(":/preview_image/image-recipe.png"))
        recipe_image.setScaledContents(True)
        recipe_image.setObjectName("recipe_image")
        recipe_name = QtWidgets.QLabel(recipe_form)
        recipe_name.setGeometry(QtCore.QRect(10, 197, 248, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        recipe_name.setFont(font)
        recipe_name.setStyleSheet("color: rgb(255, 255, 255);")
        recipe_name.setObjectName("recipe_name")
        recipe_name.setText(recipe['title'])
        recipe_description = QtWidgets.QLabel(recipe_form)
        recipe_description.setGeometry(QtCore.QRect(10, 238, 248, 140))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        recipe_description.setFont(font)
        recipe_description.setStyleSheet("color: rgb(255, 255, 255);")
        recipe_description.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        recipe_description.setObjectName("recipe_des")
        recipe_description.setText(recipe['description'])
        recipe_form.show()

    def __getting_recipes(self, list_recipes):
        self.__clear_content(self.content_area)
        self.__get_search_panel_window()
        self.__request_image_recipes(list_recipes)
        column = 0
        for recipe in list_recipes:
            x = self.__get_geometry_x(column)
            self.__preparation_form(recipe, self.content_area, {'x': x, 'y': 136})
            column += 1
        self.__get_button_load_more()

    def __clear_content(self, target):
        for widget in target.children():
            widget.deleteLater()

    def _send_request_recipes(self, text_input):
        item_response = get_items_response()
        answer_server = self.session.get(get_response_server(self.ADDRESS_SERVER, item_response, text_input))
        answer_server = answer_server.json()
        self.list_answer_recipes = dict()
        i = 0
        list_recipes = 1
        temp = []
        for recipe in answer_server:
            if i < 2:
                temp.append(recipe)
                i += 1
            else:
                temp.append(recipe)
                self.list_answer_recipes[str(list_recipes)] = temp
                list_recipes += 1
                temp = []
                i = 0
        self.list_answer_recipes[f'{list_recipes}'] = temp
        self.max_list_recipes = len(self.list_answer_recipes)
        self.list_view_recipes = 1
        self.__getting_recipes(self.list_answer_recipes[str(self.list_view_recipes)])

    def _send_request_validation_user(self, user_login, user_password):
        pass

    def _send_request_registration_user(self):
        pass

    def __request_image_recipes(self, recipes):
        for recipe in recipes:
            image = self.session.get(get_image_address(recipe["img"]))
            image = image.content
            self.images_recipes[str(recipe["id"])] = image


    @staticmethod
    def __get_geometry_x(column):
        margin = 27
        width_card = 268
        return (column * width_card + column * margin)


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
    ui = WhatsEatApp(session, ADDRESS_SERVER)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

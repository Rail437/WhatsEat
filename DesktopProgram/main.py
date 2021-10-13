import sys
import requests
import json

from PyQt5 import QtCore, QtGui, QtWidgets

from DesktopProgram.sample.sample import Ui_WhatsEat
from DesktopProgram.utils import load_configs, get_address, get_items_response_recipes, get_response_server, get_image_address


CONFIG = dict()


class WhatsEatApp(Ui_WhatsEat):
    def __init__(self, session:requests.Session, ADDRESS_SERVER):
        self.session = session
        self.ADDRESS_SERVER = ADDRESS_SERVER
        self.list_answer_recipes = dict()
        self.list_view_recipes = 0
        self.max_list_recipes = 0
        self.images_recipes = dict()
        self.email = ''
        self.login = ''
        self.username = ''
        
    def setupUi(self, WhatsEat):
        super(WhatsEatApp, self).setupUi(WhatsEat)
        self.menu_search.clicked.connect(self.__get_search_window)
        self.menu_login.clicked.connect(self.__get_login_window)
        self.menu_help.clicked.connect(self.__get_help_window)
        self.__get_search_window()

    def __menu_user_login(self):
        self.menu_login.deleteLater()
        self.menu_profile = QtWidgets.QPushButton(self.menu_bar)
        self.menu_profile.setGeometry(QtCore.QRect(5, 76, 50, 50))
        self.menu_profile.setText("")
        icon_profile = QtGui.QIcon()
        icon_profile.addPixmap(QtGui.QPixmap(":/menu/menu_edit-profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_profile.setIcon(icon_profile)
        self.menu_profile.setIconSize(QtCore.QSize(50, 50))
        self.menu_profile.setObjectName("menu_profile")
        self.menu_profile.clicked.connect(self.__get_edit_profile_window)
        self.menu_logout = QtWidgets.QPushButton(self.menu_bar)
        self.menu_logout.setGeometry(QtCore.QRect(5, 141, 50, 50))
        self.menu_logout.setText("")
        icon_logout = QtGui.QIcon()
        icon_logout.addPixmap(QtGui.QPixmap(":/menu/menu_close-profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_logout.setIcon(icon_logout)
        self.menu_logout.setIconSize(QtCore.QSize(50, 50))
        self.menu_logout.setObjectName("menu_logout")
        self.menu_logout.clicked.connect(self._logout_user)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 60, 267))
        self.menu_help.setGeometry(QtCore.QRect(5, 206, 50, 50))
        self.menu_profile.show()
        self.menu_logout.show()

    def _logout_user(self):
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 60, 200))
        self.menu_help.setGeometry(QtCore.QRect(5, 141, 50, 50))
        self.menu_login = QtWidgets.QPushButton(self.menu_bar)
        self.menu_login.setGeometry(QtCore.QRect(5, 76, 50, 50))
        self.menu_login.setText("")
        icon_login = QtGui.QIcon()
        icon_login.addPixmap(QtGui.QPixmap(":/menu/menu_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_login.setIcon(icon_login)
        self.menu_login.setIconSize(QtCore.QSize(50, 50))
        self.menu_login.setObjectName("menu_login")
        self.menu_login.clicked.connect(self.__get_login_window)
        self.menu_login.show()
        self.menu_profile.deleteLater()
        self.menu_logout.deleteLater()
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
        feedback_icon_btn = QtWidgets.QPushButton(help_panel)
        feedback_icon_btn.setGeometry(QtCore.QRect(817, 542, 36, 26))
        feedback_icon_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/feedback/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        feedback_icon_btn.setIcon(icon3)
        feedback_icon_btn.setIconSize(QtCore.QSize(36, 26))
        feedback_icon_btn.setObjectName("feedback_icon_btn")
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
        registration_panel.setGeometry(QtCore.QRect(213, 27, 400, 536))
        registration_panel.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                              "border-radius: 10px;")
        registration_panel.setObjectName("registration_panel")
        login_label = QtWidgets.QLabel(registration_panel)
        login_label.setGeometry(QtCore.QRect(26, 127, 311, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        login_label.setFont(font)
        login_label.setStyleSheet("color: rgb(255, 255, 255);")
        login_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        login_label.setObjectName("login_label")
        login_label.setText("Придумайте логин:")
        email_label = QtWidgets.QLabel(registration_panel)
        email_label.setGeometry(QtCore.QRect(26, 16, 311, 26))
        email_label.setFont(font)
        email_label.setStyleSheet("color: rgb(255, 255, 255);")
        email_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        email_label.setObjectName("email_label")
        email_label.setText("Введите почту:")
        input_email = QtWidgets.QLineEdit(registration_panel)
        input_email.setGeometry(QtCore.QRect(26, 54, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_email.setFont(font)
        input_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5px;")
        input_email.setObjectName("input_email")
        input_email.setText(self.email)
        password_label = QtWidgets.QLabel(registration_panel)
        password_label.setGeometry(QtCore.QRect(26, 238, 301, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        password_label.setFont(font)
        password_label.setStyleSheet("color: rgb(255, 255, 255);")
        password_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        password_label.setObjectName("password_label")
        password_label.setText("Придумайте пароль:")
        input_password = QtWidgets.QLineEdit(registration_panel)
        input_password.setGeometry(QtCore.QRect(26, 276, 348, 57))
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
        input_login.setGeometry(QtCore.QRect(26, 165, 348, 57))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        input_login.setFont(font)
        input_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 5px;")
        input_login.setObjectName("input_login")
        input_login.setText(self.login)
        registration_btn = QtWidgets.QPushButton(registration_panel)
        registration_btn.setGeometry(QtCore.QRect(50, 460, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        registration_btn.setFont(font)
        registration_btn.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                            "border-radius: 10px;")
        registration_btn.setObjectName("registration_btn")
        registration_btn.setText("РЕГИСТРАЦИЯ")
        registration_btn.clicked.connect(lambda : self._send_request_registration_user(input_email.text(), input_login.text(), input_password.text(), input_password_verification.text()))
        password_verification_label = QtWidgets.QLabel(registration_panel)
        password_verification_label.setGeometry(QtCore.QRect(26, 349, 300, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        password_verification_label.setFont(font)
        password_verification_label.setStyleSheet("color: rgb(255, 255, 255);")
        password_verification_label.setObjectName("password_verification_label")
        input_password_verification = QtWidgets.QLineEdit(registration_panel)
        input_password_verification.setGeometry(QtCore.QRect(25, 387, 348, 57))
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

    def __get_edit_profile_window(self):
        self.__clear_content(self.content_area)
        form_preview_area = QtWidgets.QWidget(self.content_area)
        form_preview_area.setGeometry(QtCore.QRect(0, 0, 868, 583))
        font_input = QtGui.QFont()
        font_input.setFamily("Times New Roman")
        font_input.setPointSize(18)
        input_login_preview = QtWidgets.QLineEdit(form_preview_area)
        input_login_preview.setGeometry(QtCore.QRect(16, 48, 348, 57))
        input_login_preview.setStyleSheet("border-radius: 10px;background-color: rgb(180, 180, 180);width: 348px;height: 57px;")
        input_login_preview.setReadOnly(True)
        input_login_preview.setObjectName("input_login_preview")
        input_login_preview.setText(self.login)
        input_login_preview.setFont(font_input)
        login_label = QtWidgets.QLabel(form_preview_area)
        login_label.setGeometry(QtCore.QRect(16, 12, 231, 24))
        font_label = QtGui.QFont()
        font_label.setFamily("Times New Roman")
        font_label.setPointSize(18)
        login_label.setFont(font_label)
        login_label.setStyleSheet("color: rgb(255, 255, 255);")
        login_label.setObjectName("login_label")
        login_label.setText("Логин:")
        input_username_preview = QtWidgets.QLineEdit(form_preview_area)
        input_username_preview.setGeometry(QtCore.QRect(16, 153, 348, 57))
        input_username_preview.setStyleSheet("border-radius: 10px;background-color: rgb(255, 255, 255);width: 348px;height: 57px;")
        input_username_preview.setObjectName("input_username_preview")
        input_username_preview.setFont(font_input)
        input_username_preview.setText(self.username)
        user_name_label = QtWidgets.QLabel(form_preview_area)
        user_name_label.setGeometry(QtCore.QRect(16, 117, 340, 24))
        user_name_label.setFont(font_label)
        user_name_label.setStyleSheet("color: rgb(255, 255, 255);")
        user_name_label.setObjectName("user_name_label")
        user_name_label.setText("Имя:")
        input_old_password = QtWidgets.QLineEdit(form_preview_area)
        input_old_password.setGeometry(QtCore.QRect(16, 258, 348, 57))
        input_old_password.setStyleSheet("border-radius: 10px;background-color: rgb(255, 255, 255);width: 348px;height: 57px;")
        input_old_password.setEchoMode(QtWidgets.QLineEdit.Password)
        input_old_password.setObjectName("input_old_password")
        input_old_password.setFont(font_input)
        input_new_password = QtWidgets.QLineEdit(form_preview_area)
        input_new_password.setGeometry(QtCore.QRect(16, 363, 348, 57))
        input_new_password.setStyleSheet("border-radius: 10px;background-color: rgb(255, 255, 255);width: 348px;height: 57px;")
        input_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        input_new_password.setObjectName("input_new_password")
        input_new_password.setFont(font_input)
        old_password_label = QtWidgets.QLabel(form_preview_area)
        old_password_label.setGeometry(QtCore.QRect(16, 222, 340, 24))
        old_password_label.setFont(font_label)
        old_password_label.setStyleSheet("color: rgb(255, 255, 255);")
        old_password_label.setObjectName("old_password_label")
        old_password_label.setText("Старый пароль:")
        new_password_label = QtWidgets.QLabel(form_preview_area)
        new_password_label.setGeometry(QtCore.QRect(16, 327, 340, 24))
        new_password_label.setFont(font_label)
        new_password_label.setStyleSheet("color: rgb(255, 255, 255);")
        new_password_label.setObjectName("new_password_label")
        new_password_label.setText("Новый пароль:")
        new_password_validation = QtWidgets.QLabel(form_preview_area)
        new_password_validation.setGeometry(QtCore.QRect(16, 432, 340, 24))
        new_password_validation.setFont(font_label)
        new_password_validation.setStyleSheet("color: rgb(255, 255, 255);")
        new_password_validation.setObjectName("new_password_validation")
        new_password_validation.setText("Подтвердите новый пароль:")
        input_new_password_validation = QtWidgets.QLineEdit(form_preview_area)
        input_new_password_validation.setGeometry(QtCore.QRect(16, 468, 348, 57))
        input_new_password_validation.setStyleSheet("border-radius: 10px;background-color: rgb(255, 255, 255);width: 348px;height: 57px;")
        input_new_password_validation.setEchoMode(QtWidgets.QLineEdit.Password)
        input_new_password_validation.setObjectName("input_new_password_validation")
        input_new_password_validation.setFont(font_input)
        change_password_btn = QtWidgets.QPushButton(form_preview_area)
        change_password_btn.setGeometry(QtCore.QRect(40, 537, 300, 45))
        change_password_btn.setFont(font_label)
        change_password_btn.setStyleSheet("background-color: rgb(231, 180, 0);border-radius: 10px;")
        change_password_btn.setObjectName("change_password_btn")
        change_password_btn.setText("Сменить пароль")
        change_password_btn.clicked.connect(lambda : self._send_request_edit_profile(input_login_preview.text(), input_new_password.text(), input_new_password_validation.text(), input_username_preview.text()))
        preview_list_label = QtWidgets.QLabel(form_preview_area)
        preview_list_label.setGeometry(QtCore.QRect(440, 12, 340, 24))
        preview_list_label.setFont(font_label)
        preview_list_label.setStyleSheet("color: rgb(255, 255, 255);")
        preview_list_label.setObjectName("preview_list_label")
        preview_list_label.setText("Отложенные рецепты:")
        list_last_preview_recipes = QtWidgets.QWidget(form_preview_area)
        list_last_preview_recipes.setGeometry(QtCore.QRect(440, 48, 401, 521))
        list_last_preview_recipes.setObjectName("list_last_preview_recipes")
        form_preview_area.show()

    def __get_next_recipes(self):
        if self.list_view_recipes < self.max_list_recipes:
            self.list_view_recipes += 1
            self.__getting_recipes(self.list_answer_recipes[str(self.list_view_recipes)])

    def __get_preview_recipes(self):
        if self.list_view_recipes > 1:
            self.list_view_recipes -= 1
            self.__getting_recipes(self.list_answer_recipes[str(self.list_view_recipes)])

    def __get_button_load_next(self):
        load_more = QtWidgets.QPushButton(self.content_area)
        load_more.setGeometry(QtCore.QRect(710, 546, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        load_more.setFont(font)
        load_more.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                     "border-radius: 5px;")
        load_more.setObjectName("load_more")
        load_more.clicked.connect(self.__get_next_recipes)
        load_more.setText("Далее")
        load_more.show()

    def __get_button_load_preview(self):
        load_more = QtWidgets.QPushButton(self.content_area)
        load_more.setGeometry(QtCore.QRect(0, 546, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        load_more.setFont(font)
        load_more.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                     "border-radius: 5px;")
        load_more.setObjectName("load_more")
        load_more.clicked.connect(self.__get_preview_recipes)
        load_more.setText("Назад")
        load_more.show()

    def __get_view_list(self):
        view_list_recipe = QtWidgets.QWidget(self.content_area)
        view_list_recipe.setGeometry(QtCore.QRect(150, 546, 560, 31))
        current_page = QtWidgets.QLabel(view_list_recipe)
        current_page.setGeometry(QtCore.QRect(0, 0, 560, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        current_page.setFont(font)
        current_page.setStyleSheet("color: rgb(255, 255, 255);")
        current_page.setObjectName("recipe_name")
        current_page.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        current_page.setText(f"{self.list_view_recipes} из {self.max_list_recipes}")
        view_list_recipe.show()

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
            pixmap.loadFromData(self.images_recipes[str(recipe["id"])])
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
        recipe_btn = QtWidgets.QPushButton(recipe_form)
        recipe_btn.setGeometry(QtCore.QRect(0, 0, 268, 384))
        recipe_btn.setStyleSheet('background-color: rgba(162, 255, 111, 0);')
        recipe_btn.clicked.connect(lambda : self.__get_recipe_preview(recipe))
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
        self.__get_button_load_preview()
        self.__get_view_list()
        self.__get_button_load_next()

    def __get_recipe_preview(self, recipe):
        self.__clear_content(self.content_area)
        recipe_form = QtWidgets.QWidget(self.content_area)
        recipe_form.setGeometry(QtCore.QRect(0, 0, 868, 583))
        recipe_form.setStyleSheet("border-radius: 10px;background-color: rgb(56, 56, 56);")
        recipe_form.setObjectName("recipe_form")
        recipe_preview_image = QtWidgets.QLabel(recipe_form)
        recipe_preview_image.setGeometry(QtCore.QRect(15, 15, 300, 200))
        recipe_preview_image.setText("")
        try:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(self.images_recipes[str(recipe["id"])])
            recipe_preview_image.setPixmap(pixmap)
        except Exception:
            recipe_preview_image.setPixmap(QtGui.QPixmap(":/preview_image/image-recipe.png"))
        recipe_preview_image.setScaledContents(True)
        recipe_preview_image.setObjectName("recipe_preview_image")
        recipe_name = QtWidgets.QLabel(recipe_form)
        recipe_name.setGeometry(QtCore.QRect(330, 15, 523, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        recipe_name.setFont(font)
        recipe_name.setStyleSheet("color: rgb(255, 255, 255);")
        recipe_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        recipe_name.setObjectName("recipe_name")
        recipe_name.setText(recipe['title'])
        recipe_description = QtWidgets.QLabel(recipe_form)
        recipe_description.setGeometry(QtCore.QRect(15, 230, 838, 307))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        recipe_description.setFont(font)
        recipe_description.setStyleSheet("color: rgb(255, 255, 255);")
        recipe_description.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        recipe_description.setObjectName("recipe_description")
        recipe_description.setText(recipe['description'])
        btn_comeback = QtWidgets.QPushButton(recipe_form)
        btn_comeback.setGeometry(QtCore.QRect(15, 542, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        btn_comeback.setFont(font)
        btn_comeback.setText("Назад")
        btn_comeback.setStyleSheet("background-color: rgb(231, 180, 0);\n"
                                          "border-radius:5px;\n")
        btn_comeback.clicked.connect(self.__get_comeback_recipes)
        recipe_form.show()

    def __get_comeback_recipes(self):
        self.__clear_content(self.content_area)
        self.__getting_recipes(self.list_answer_recipes[str(self.list_view_recipes)])


    def __getting_delayed_recipes(self):
        pass

    def __clear_content(self, target):
        for widget in target.children():
            widget.deleteLater()

    def __preparation_link_delayed_recipe(self, recipe):
        pass

    def _send_request_recipes(self, text_input):
        item_response = get_items_response_recipes()
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
        result = self.session.post(get_response_server(self.ADDRESS_SERVER, 'login'), params={'username': user_login, 'password': user_password})
        if result.status_code == 200:
            self.__menu_user_login()
            self.__get_search_window()
            self.login = user_login
        else:
            message = QtWidgets.QMessageBox()
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setWindowTitle("Не верный логин или пароль!")
            message.setText("<p style='color: white;'>Проверьте поля и попробуйте еще раз<\p>")
            message.setStyleSheet('QMessageBox {background-color: rgb(56, 56, 56);color: rgb(255, 255, 255);}'
                                  'QPushButton {width: 35px;height:25px;border-radius: 5px;background-color: rgb(231, 180, 0);color: rgb(0, 0, 0);}')
            message.exec_()

    def _send_request_registration_user(self, email_user, login_user, password_user, password_user_ver):
        self.email = email_user
        self.login = login_user
        if email_user == '' or login_user == '' or password_user == '' or password_user_ver == '':
            print("password:", password_user, password_user_ver, sep="\n")
            message = QtWidgets.QMessageBox()
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setWindowTitle("Заполнены не все поля!")
            message.setText("<p style='color: white;'>Проверьте поля и попробуйте еще раз<\p>")
            message.setStyleSheet('QMessageBox {background-color: rgb(56, 56, 56);color: rgb(255, 255, 255);}'
                                  'QPushButton {width: 35px;height:25px;border-radius: 5px;background-color: rgb(231, 180, 0);color: rgb(0, 0, 0);}')
            message.exec_()
            self.__get_registration_window()
        else:
            if password_user == password_user_ver:
                print("password verification")
                self.session.post(get_response_server(self.ADDRESS_SERVER, 'registration'), params={'email': email_user, 'login': login_user, 'password': password_user})
                self.__get_search_window()
            else:
                print("password:", password_user, password_user_ver, sep="\n")
                message = QtWidgets.QMessageBox()
                message.setIcon(QtWidgets.QMessageBox.Critical)
                message.setWindowTitle("Введеные пароли не совпадают!")
                message.setText("<p style='color: white;'>Проверьте введеные данные и попробуйте еще раз<\p>")
                message.setStyleSheet('QMessageBox {background-color: rgb(56, 56, 56);color: rgb(255, 255, 255);}'
                                      'QPushButton {width: 35px;height:25px;border-radius: 5px;background-color: rgb(231, 180, 0);color: rgb(0, 0, 0);}')
                message.exec_()
                self.__get_registration_window()

    def _send_request_edit_profile(self, user_login, user_password, user_password_validation, user_name):
        if user_password != '':
            if user_name != '':
                if user_password == user_password_validation:
                    self.session.post(get_response_server(self.ADDRESS_SERVER, 'editpass'),
                                      params={'username': user_name, 'password': user_password, 'login': user_login})
                    self.username = user_name
                else:
                    message = QtWidgets.QMessageBox()
                    message.setIcon(QtWidgets.QMessageBox.Critical)
                    message.setWindowTitle("Пароли не совпадают!")
                    message.setText("<p style='color: white;'>Проверьте пароли и попробуйте еще раз<\p>")
                    message.setStyleSheet('QMessageBox {background-color: rgb(56, 56, 56);color: rgb(255, 255, 255);}'
                                          'QPushButton {width: 35px;height:25px;border-radius: 5px;background-color: rgb(231, 180, 0);color: rgb(0, 0, 0);}')
                    message.exec_()
            else:
                if user_password == user_password_validation:
                    self.session.post(get_response_server(self.ADDRESS_SERVER, 'editpass'),
                                      params={'password': user_password, 'login': user_login})
                else:
                    message = QtWidgets.QMessageBox()
                    message.setIcon(QtWidgets.QMessageBox.Critical)
                    message.setWindowTitle("Пароли не совпадают!")
                    message.setText("<p style='color: white;'>Проверьте пароли и попробуйте еще раз<\p>")
                    message.setStyleSheet('QMessageBox {background-color: rgb(56, 56, 56);color: rgb(255, 255, 255);}'
                                          'QPushButton {width: 35px;height:25px;border-radius: 5px;background-color: rgb(231, 180, 0);color: rgb(0, 0, 0);}')
                    message.exec_()
        else:
            if user_name != '':
                self.session.post(get_response_server(self.ADDRESS_SERVER, 'editpass'),
                                  params={'username': user_name, 'login': user_login})
                self.username = user_name
        self.__clear_content(self.content_area)
        self.__get_edit_profile_window()

    def __request_image_recipes(self, recipes):
        for recipe in recipes:
            image = self.session.get(get_image_address(recipe["img_path"]))
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

    # # Response server (TEST)
    # with open('answer_server_profile.json', 'w') as f:
    #     answer = session.get('http://185.46.8.32:8080/whatseat/api/v1/getUser?login=Alex23')
    #     json.dump(answer.json(), f)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WhatsEatApp(session, ADDRESS_SERVER)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

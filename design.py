# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, 
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient, QTextCursor)
from PyQt5.QtWidgets import *
from PySide2.QtGui import QAccessibleTextInterface
from PyQt5 import QtWidgets
import os
import sys
import pyqtgraph as pg
import pyqtgraph.exporters

class Ui_Main(object):
    def __init__(self, QMainWindow):
        self.setupUi(QMainWindow)

    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 550)
        Main.setMaximumSize(QSize(800, 550))
        Main.setStyleSheet(u"background-color: rgb(30, 30, 30)")

        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setWeight(50)

        self.actionOpen = QAction(Main)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(Main)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(Main)
        self.actionExit.setObjectName(u"actionExit")
        self.actionUndo = QAction(Main)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(Main)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(Main)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(Main)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPast = QAction(Main)
        self.actionPast.setObjectName(u"actionPast")
        self.actionSelect_fun = QAction(Main)
        self.actionSelect_fun.setObjectName(u"actionSelect_fun")
        self.actionClear_fun = QAction(Main)
        self.actionClear_fun = QAction(Main)
        self.actionas_PNG = QAction(Main)
        self.actionas_PNG.setObjectName(u"actionas_PNG")
        self.actionjpeg = QAction(Main)
        self.actionjpeg.setObjectName(u"actionjpeg")
        self.action = QAction(Main)
        self.action.setObjectName(u"action")

        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color:rgb(225, 225, 225)")

        self.errors = QLabel(self.centralwidget)
        self.errors.setObjectName(u"errors")
        self.errors.setGeometry(QRect(370, 8, 411, 31))

        self.min_x_text = QLabel(self.centralwidget)
        self.min_x_text.setObjectName(u"min_x_text")
        self.min_x_text.setGeometry(QRect(20, 40, 151, 20))
        
        self.min_y_text = QLabel(self.centralwidget)
        self.min_y_text.setObjectName(u"min_y_text")
        self.min_y_text.setGeometry(QRect(20, 100, 151, 20))

        self.max_y_text = QLabel(self.centralwidget)
        self.max_y_text.setObjectName(u"max_y_text")
        self.max_y_text.setGeometry(QRect(190, 100, 151, 20))

        self.max_x_text = QLabel(self.centralwidget)
        self.max_x_text.setObjectName(u"max_x_text")
        self.max_x_text.setGeometry(QRect(190, 40, 151, 20))

        self.fun_text = QLabel(self.centralwidget)
        self.fun_text.setObjectName(u"fun_text")
        self.fun_text.setGeometry(QRect(370, 29, 411, 31))
        
        self.min_x = QTextEdit(self.centralwidget)
        self.min_x.setObjectName(u"min_x")
        self.min_x.setGeometry(QRect(20, 60, 151, 31))
        self.min_x.setFont(font)
        self.min_x.setStyleSheet(u"background-color: rgb(42, 42, 43); \n"
                                    "color: #fff;\n padding-top: 2px;"
                                    "border: 0px solid;\n"
                                    "border-radius: 10px;")

        self.min_y = QTextEdit(self.centralwidget)
        self.min_y.setObjectName(u"min_y")
        self.min_y.setGeometry(QRect(20, 120, 151, 31))
        self.min_y.setFont(font)
        self.min_y.setStyleSheet(u"background-color: rgb(42, 42, 43); \n"
                                    "color: #fff;\n padding-top: 2px;"
                                    "border: 0px solid;\n"
                                    "border-radius: 10px;")

        self.max_y = QTextEdit(self.centralwidget)
        self.max_y.setObjectName(u"max_y")
        self.max_y.setGeometry(QRect(190, 120, 151, 31))
        self.max_y.setFont(font)
        self.max_y.setStyleSheet(u"background-color: rgb(42, 42, 43); \n"
                                    "color: #fff;\n padding-top: 2px;"
                                    "border: 0px solid;\n"
                                    "border-radius: 10px;")

        self.max_x = QTextEdit(self.centralwidget)
        self.max_x.setObjectName(u"max_x")
        self.max_x.setGeometry(QRect(190, 60, 151, 31))
        self.max_x.setFont(font)
        self.max_x.setStyleSheet(u"background-color: rgb(42, 42, 43); \n"
                                    "color: #fff;\n padding-top: 2px;"
                                    "border: 0px solid;\n"
                                    "border-radius: 10px;")

        self.fun_data = QTextEdit(self.centralwidget)
        self.fun_data.setObjectName(u"fun_data")
        self.fun_data.setGeometry(QRect(370, 60, 411, 31))
        self.fun_data.setPlaceholderText(u"")
        self.fun_data.setFont(font)
        self.fun_data.setStyleSheet(u"background-color: rgb(42, 42, 43); \n"
                                     "color: #fff;\n padding-top: 2px;"
                                     "border: 0px solid;\n"
                                     "border-radius: 10px;")

        self.bild_butt = QPushButton(self.centralwidget)
        self.bild_butt.setObjectName(u"bild_butt")
        self.bild_butt.setGeometry(QRect(370, 110, 411, 41))
        self.bild_butt.setStyleSheet(u"QPushButton{\n"
                                        "color: #e5e5e5;\n"
                                        "font-size: 15px;\n"
                                        "line-height: 1.55;\n"
                                        "font-weight: 600;\n"
                                        "border: 0px solid;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:rgb(96, 42, 116);\n"
                                        "background-position: center center;\n"
                                        "border-color: transparent;\n"
                                        "border-style: solid;}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color:rgb(120, 53, 147);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "color: #000;\n"
                                        "background-color:rgb(221, 53, 104);\n"
                                        "}")

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setOffset(0, 0)
        self.bild_butt.setGraphicsEffect(self.shadow)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 180, 760, 290))

        self.domain_function_label = QLabel(self.centralwidget)
        self.domain_function_label.setObjectName(u"domain_function_label")
        self.domain_function_label.setGeometry(QRect(20, 5, 321, 31))

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 480, 761, 23))
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
                                        "    border: 0px solid grey;\n"
                                        "    color: #828282;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QProgressBar::chunk {\n"
                                        "    background-color: #05B8CC;\n"
                                        "    width: 20px;\n"
                                        "}")

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setStyleSheet(u"background-color:rgb(50, 50, 51);\n"
"color: rgb(200, 200, 200)")
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuSave_as = QMenu(self.menu)
        self.menuSave_as.setObjectName(u"menuSave_as")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSelection = QMenu(self.menubar)
        self.menuSelection.setObjectName(u"menuSelection")

        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(10, 150, 780, 330))

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.guiplot = pg.PlotWidget()
        self.gridLayout.addWidget(self.guiplot)
        self.guiplot.plot([5, 2, 12, 4, 5, 8, 10])

        Main.setMenuBar(self.menubar)        
        self.menubar.addAction(self.menu.menuAction())
        # self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSelection.menuAction())
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.menuSave_as.menuAction())
        self.menu.addAction(self.actionExit)
        self.menuSave_as.addAction(self.actionas_PNG)
        self.menuSave_as.addAction(self.actionjpeg)
        # self.menuEdit.addAction(self.actionUndo)
        # self.menuEdit.addAction(self.actionRedo)
        # self.menuEdit.addSeparator()
        # self.menuEdit.addAction(self.actionCut)
        # self.menuEdit.addAction(self.actionCopy)
        # self.menuEdit.addAction(self.actionPast)
        self.menuSelection.addAction(self.actionSelect_fun)
        self.menuSelection.addAction(self.actionClear_fun)

        self.actionExit.triggered.connect(qApp.quit)
        self.actionClear_fun.triggered.connect(self.clear_all)
        self.actionSave.triggered.connect(self.save)
        self.menuSave_as.triggered.connect(self.save_as)
        self.actionOpen.triggered.connect(self.open)
        self.actionSelect_fun.triggered.connect(self.fun_data.selectAll)
        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(u"Main")
        self.actionOpen.setText(u"Open .txt")
        self.actionOpen.setShortcut(u"Ctrl+O")
        
        self.actionSave.setText(u"Save .txt")
        self.actionSave.setShortcut(u"Ctrl+S")

        self.actionExit.setText(u"Exit")
        self.actionExit.setShortcut(u"Ctrl+W")

        self.actionUndo.setText(u"Undo")
        self.actionUndo.setShortcut(u"Ctrl+Z")

        self.actionRedo.setText(u"Redo")
        self.actionRedo.setShortcut(u"Ctrl+Shift+Z")

        self.actionCut.setText(u"Cut")
        self.actionCut.setShortcut(u"Ctrl+X")

        self.actionCopy.setText(u"Copy")
        self.actionCopy.setShortcut(u"Ctrl+C")

        self.actionPast.setText(u"Paste")
        self.actionPast.setShortcut(u"Ctrl+V")

        self.actionSelect_fun.setText(u"Select function")
        self.actionSelect_fun.setShortcut(u"Ctrl+A")

        self.actionClear_fun.setText(u"Clear function")
        self.actionClear_fun.setShortcut(u"Ctrl+Shift+W")

        self.actionas_PNG.setText(u"png")
        self.actionjpeg.setText(u"jpeg")
        
        self.fun_data.setPlaceholderText(u"gamma(cos((x*pi)/5)-tan(4*(x^e))/1)")
        self.fun_data.setText(u"x^3")
        self.min_x.setText(u"-100")
        self.max_x.setText(u"100")
        self.max_y.setText(u"1000")
        self.min_y.setText(u"0")
        
        self.min_y_text.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Минимум по оси у:</span></p></body></html>")
        self.max_y_text.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Максимум по оси у:</span></p></body></html>")

        self.min_x_text.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Минимум:</span></p></body></html>")
        self.max_x_text.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Максимум:</span></p></body></html>")
        
        self.fun_text.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Функция</span></p></body></html>")

        self.bild_butt.setText(u"Построить график")

        self.domain_function_label.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Область определения функции</span></p></body></html>")

        self.menu.setTitle(u"File")
        self.menuSave_as.setTitle(u"Save as ...")
        self.menuEdit.setTitle(u"Edit")
        self.menuSelection.setTitle(u"Selection")
    # retranslateUi

    def error_data(self, error_code=None, error_name=None):
        '''
        Здесь идёт обработка и вывод всех ошибок.
        MB - выводит сообщение в отдельное окно.
        errors - выводит сообщение над функцией, чтобы пользователь не забыл, в чём проблема.
        '''
        self.MB = QtWidgets.QMessageBox()
        self.MB.setIcon(QtWidgets.QMessageBox.Critical)
        if error_code == None: 
            self.MB.setText(error_name)
            self.errors.setText(f"<html><head/><body><p align=\"center\">{error_name[:55]}</p></body></html>")
        elif error_code == "NothingLeftToLose": 
            self.MB.setText("Не введены данные")
            self.MB.setInformativeText("Вы оставили обе строки пустыми. Введите данные")
        elif error_code == "FunLost": 
            self.MB.setText("Не введена функция")
            self.MB.setInformativeText("Вы не ввели функцию")
        elif error_code == "ZeroDivisionError":
            self.MB.setText("Произошло деление на ноль")
            self.MB.setInformativeText("Некорректный ввод функцию")

        self.MB.setWindowTitle("Ошибка ввода данных")
        self.MB.setDetailedText("""Пример ввода для функции: \ngamma(cos((x*pi)/5)), \nlog10(x), log(x, 3), sqrt(X). 
\nДля значений Х и лимитов оси Y подходят только целые числа!
\nПроверьте данные и повторите попытку.""")
        self.MB.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.MB.exec_()
    # ErrorUi

    def open(self):
        fname = QFileDialog.getOpenFileName(self.centralwidget, "Open File", os.path.abspath(__file__), "Text files (*.txt)")
        if fname[0]:
            f = open(fname[0], "r")
            self.fun_data.setText(f"{f.read()}")

    def save(self):
        fname = QFileDialog.getSaveFileName(self.centralwidget, 'Save', os.path.abspath(__file__).replace(__file__, "") + ".txt", "Text files (*.txt)")
        if fname[0]:
            f = open("fname[0]", "w")
            f.write(self.fun_data.toPlainText())
            f.close()

    def save_as(self):
        exporter = pg.exporters.ImageExporter(self.guiplot.plotItem)
        fname = QFileDialog.getSaveFileName(self.centralwidget, 'Save as', os.path.abspath(__file__).replace(__file__, "") + ".jpg", "Images (*.png *.jpg)")
        exporter.parameters()['width'] = 720
        if fname[0]:
            exporter.export(fname[0])

    def clear_all(self):
        self.guiplot.clear()
        self.fun_data.setText("")
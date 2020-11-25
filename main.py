# This Python file uses the following encoding: utf-8
import sys
import os
from math import *

from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow, QBoxLayout, QWidget
from PySide2.QtCore import QRect, QSize
import pyqtgraph as pg
from design import *

class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self)
        self.ui = Ui_Main(self)
        self.ui.bild_butt.clicked.connect(self.function)

    def graph(self, x_list_final):
        self.ui.guiplot.clear()
        self.ui.guiplot.plot(x_list_final)
        self.ui.errors.setText("")

    def function(self):
        self.statusBar().setStyleSheet(u"color:#fff")
        self.statusBar().showMessage("In process")        
        self.ui.progressBar.reset()
        x_list_final = []
        try:
            self.min_x = int(self.ui.min_x.toPlainText())
            self.max_x = int(self.ui.max_x.toPlainText())
            self.min_y = int(self.ui.min_y.toPlainText())
            self.max_y = int(self.ui.max_y.toPlainText())

            if self.min_x == self.max_x:
                raise ValueError
            if self.min_y == self.max_y:
                raise ValueError

            if self.min_x > self.max_x:
                self.min_x, self.max_x = self.max_x, self.min_x
            if self.min_y > self.max_y:
                self.min_y, self.max_y = self.max_y, self.min_y

            self.ui.progressBar.setRange(self.min_x-1, self.max_x)

            x_list = list(range(self.min_x-1, self.max_x))

            for x in x_list:
                self.ui.progressBar.setValue(x)                
                fun = self.ui.fun_data.toPlainText()
                if (fun != ""):
                    try:
                        ans = abs(eval(fun.replace("^", "**").replace("x", f"{x}").replace("X", f"{x}")))
                        x_list_final.append(int(ans))
                        a = []
                        [a.append(i) for i in range(len(x_list_final)) if x_list_final[i] > self.max_y or x_list_final[i] < self.min_y]
                        a.reverse()
                        [x_list_final.pop(i) for i in a]
                    except NameError:
                        self.err()
                        self.ui.progressBar.setValue(0)
                        self.ui.error_data(error_code = "FunLost")
                        break
                    except ZeroDivisionError:
                        self.err()                        
                        self.ui.error_data(error_code = "ZeroDivisionError")
                    except AttributeError:
                        self.err()
                        self.ui.error_data(error_name = "Не верно введены данные в функции")
                        break
                    except SyntaxError:
                        self.err()
                        self.ui.error_data(error_name = "Не корректно введены данные в функции")
                        break   
                    except OverflowError:
                        self.err()
                        self.ui.error_data(error_name = """Введена слишком большая разница для значений по оси X.
Попробуйте упростить функцию или уменьшить значения минимума и/или максимума области определения функции""")
                        break
                    except MemoryError:
                        print("MemoryError")
                        raise OverflowError           
                else:
                    if (fun == "" and x == ""):
                        self.err()
                        self.ui.error_data(error_code = "NothingLeftToLose")
                        break
                    elif fun == "":
                        self.err()
                        self.ui.error_data(error_code = "FunLost")
                        break
            if x_list_final != []:
                self.graph(x_list_final)
                self.ui.progressBar.setValue(self.max_x)
                self.statusBar().clearMessage()
                self.statusBar().setStyleSheet(u"color: #00ff48")
                self.statusBar().showMessage("Done", 2000)
            else:
                self.ui.error_data(error_name = "Нет доступных значений")
        except ValueError:
            self.err()
            self.ui.error_data(error_name="Не верно введёны лимиты")
            self.ui.progressBar.setValue(0)
        except UnboundLocalError:
            self.err()
            self.ui.error_data(error_name="Не введёны лимиты")
            self.ui.progressBar.setValue(0)

    def err(self):
        self.ui.progressBar.setValue(0)
        self.statusBar().setStyleSheet(u"color: red")
        self.statusBar().showMessage("Error", 2000)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('graph.ico'))
    widget = Main()
    widget.setWindowTitle('Расчёт функции')
    widget.show()

    sys.exit(app.exec_())
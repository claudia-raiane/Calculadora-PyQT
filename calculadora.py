
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        Calculadora.setObjectName("Calculadora")
        Calculadora.resize(338, 408)
        Calculadora.setMinimumSize(QtCore.QSize(338, 408))
        Calculadora.setMaximumSize(QtCore.QSize(384, 569))
        Calculadora.setWindowIcon(QtGui.QIcon("math.png"))
        Calculadora.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(Calculadora)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.botao_dividir = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_dividir.sizePolicy().hasHeightForWidth())
        self.botao_dividir.setSizePolicy(sizePolicy)
        self.botao_dividir.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 85, 255);")
        self.botao_dividir.setObjectName("botao_dividir")
        self.gridLayout.addWidget(self.botao_dividir, 4, 3, 1, 1)
        self.botao_desligar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_desligar.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_desligar.setObjectName("botao_desligar")
        self.gridLayout.addWidget(self.botao_desligar, 1, 1, 1, 1)
        self.botao_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_8.sizePolicy().hasHeightForWidth())
        self.botao_8.setSizePolicy(sizePolicy)
        self.botao_8.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_8.setObjectName("botao_8")
        self.gridLayout.addWidget(self.botao_8, 4, 1, 1, 1)
        self.botao_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_2.sizePolicy().hasHeightForWidth())
        self.botao_2.setSizePolicy(sizePolicy)
        self.botao_2.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_2.setObjectName("botao_2")
        self.gridLayout.addWidget(self.botao_2, 2, 1, 1, 1)
        self.botao_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_6.sizePolicy().hasHeightForWidth())
        self.botao_6.setSizePolicy(sizePolicy)
        self.botao_6.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_6.setObjectName("botao_6")
        self.gridLayout.addWidget(self.botao_6, 3, 2, 1, 1)
        self.botao_multiplicar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_multiplicar.sizePolicy().hasHeightForWidth())
        self.botao_multiplicar.setSizePolicy(sizePolicy)
        self.botao_multiplicar.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 85, 255);")
        self.botao_multiplicar.setObjectName("botao_multiplicar")
        self.gridLayout.addWidget(self.botao_multiplicar, 3, 3, 1, 1)
        self.botao_clear = QtWidgets.QPushButton(self.centralwidget)
        self.botao_clear.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_clear.setObjectName("botao_clear")
        self.gridLayout.addWidget(self.botao_clear, 1, 0, 1, 1)
        self.botao_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_3.sizePolicy().hasHeightForWidth())
        self.botao_3.setSizePolicy(sizePolicy)
        self.botao_3.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_3.setObjectName("botao_3")
        self.gridLayout.addWidget(self.botao_3, 2, 2, 1, 1)
        self.botao_ponto = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_ponto.sizePolicy().hasHeightForWidth())
        self.botao_ponto.setSizePolicy(sizePolicy)
        self.botao_ponto.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_ponto.setObjectName("botao_ponto")
        self.gridLayout.addWidget(self.botao_ponto, 5, 2, 1, 1)
        self.botao_subtrair = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_subtrair.sizePolicy().hasHeightForWidth())
        self.botao_subtrair.setSizePolicy(sizePolicy)
        self.botao_subtrair.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 85, 255);")
        self.botao_subtrair.setObjectName("botao_subtrair")
        self.gridLayout.addWidget(self.botao_subtrair, 2, 3, 1, 1)
        self.botao_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_7.sizePolicy().hasHeightForWidth())
        self.botao_7.setSizePolicy(sizePolicy)
        self.botao_7.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_7.setObjectName("botao_7")
        self.gridLayout.addWidget(self.botao_7, 4, 0, 1, 1)
        self.botao_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_9.sizePolicy().hasHeightForWidth())
        self.botao_9.setSizePolicy(sizePolicy)
        self.botao_9.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_9.setObjectName("botao_9")
        self.gridLayout.addWidget(self.botao_9, 4, 2, 1, 1)
        self.botao_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_0.sizePolicy().hasHeightForWidth())
        self.botao_0.setSizePolicy(sizePolicy)
        self.botao_0.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_0.setObjectName("botao_0")
        self.gridLayout.addWidget(self.botao_0, 5, 0, 1, 2)
        self.botao_somar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_somar.sizePolicy().hasHeightForWidth())
        self.botao_somar.setSizePolicy(sizePolicy)
        self.botao_somar.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 85, 255);")
        self.botao_somar.setObjectName("botao_somar")
        self.gridLayout.addWidget(self.botao_somar, 1, 3, 1, 1)
        self.botao_igual = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_igual.sizePolicy().hasHeightForWidth())
        self.botao_igual.setSizePolicy(sizePolicy)
        self.botao_igual.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 85, 255);")
        self.botao_igual.setObjectName("botao_igual")
        self.gridLayout.addWidget(self.botao_igual, 5, 3, 1, 1)
        self.botao_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_4.sizePolicy().hasHeightForWidth())
        self.botao_4.setSizePolicy(sizePolicy)
        self.botao_4.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_4.setObjectName("botao_4")
        self.gridLayout.addWidget(self.botao_4, 3, 0, 1, 1)
        self.botao_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_5.sizePolicy().hasHeightForWidth())
        self.botao_5.setSizePolicy(sizePolicy)
        self.botao_5.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_5.setObjectName("botao_5")
        self.gridLayout.addWidget(self.botao_5, 3, 1, 1, 1)
        self.visor = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.visor.sizePolicy().hasHeightForWidth())
        self.visor.setSizePolicy(sizePolicy)
        self.visor.setStyleSheet("font: 75 28pt \"Roboto\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(85, 0, 255);")
        self.visor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visor.setObjectName("visor")
        self.gridLayout.addWidget(self.visor, 0, 0, 1, 4)
        self.botao_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_1.sizePolicy().hasHeightForWidth())
        self.botao_1.setSizePolicy(sizePolicy)
        self.botao_1.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"\n"
"")
        self.botao_1.setObjectName("botao_1")
        self.gridLayout.addWidget(self.botao_1, 2, 0, 1, 1)
        self.botao_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.botao_delete.sizePolicy().hasHeightForWidth())
        self.botao_delete.setSizePolicy(sizePolicy)
        self.botao_delete.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.botao_delete.setObjectName("botao_delete")
        self.gridLayout.addWidget(self.botao_delete, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Calculadora.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculadora)
        self.botao_desligar.clicked.connect(Calculadora.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Calculadora)
        self.botao_0.clicked.connect(self.funcao0)
        self.botao_1.clicked.connect(self.funcao1)
        self.botao_2.clicked.connect(self.funcao2)
        self.botao_3.clicked.connect(self.funcao3)
        self.botao_4.clicked.connect(self.funcao4)
        self.botao_5.clicked.connect(self.funcao5)
        self.botao_6.clicked.connect(self.funcao6)
        self.botao_7.clicked.connect(self.funcao7)
        self.botao_8.clicked.connect(self.funcao8)
        self.botao_9.clicked.connect(self.funcao9)
        self.botao_ponto.clicked.connect(self.funcao_ponto)
        self.botao_somar.clicked.connect(self.funcao_soma)
        self.botao_subtrair.clicked.connect(self.funcao_subtracao)
        self.botao_multiplicar.clicked.connect(self.funcao_multiplicacao)
        self.botao_dividir.clicked.connect(self.funcao_divisao)
        self.botao_igual.clicked.connect(self.funcao_igualar)
        self.botao_delete.clicked.connect(self.funcao_deletar)
        self.botao_clear.clicked.connect(self.funcao_limpar)

    # funções de cada botão
    def funcao0(self):
        text = self.visor.text()
        self.visor.setText(text + "0")

    def funcao1(self):
        text = self.visor.text()
        self.visor.setText(text + "1")

    def funcao2(self):
        text = self.visor.text()
        self.visor.setText(text + "2")

    def funcao3(self):
        text = self.visor.text()
        self.visor.setText(text + "3")

    def funcao4(self):
        text = self.visor.text()
        self.visor.setText(text + "4")

    def funcao5(self):
        text = self.visor.text()
        self.visor.setText(text + "5")

    def funcao6(self):
        text = self.visor.text()
        self.visor.setText(text + "6")

    def funcao7(self):
        text = self.visor.text()
        self.visor.setText(text + "7")

    def funcao8(self):
        text = self.visor.text()
        self.visor.setText(text + "8")

    def funcao9(self):
        text = self.visor.text()
        self.visor.setText(text + "9")

    def funcao_ponto(self):
        text = self.visor.text()
        self.visor.setText(text + ".")

    def funcao_soma(self):
        text = self.visor.text()
        self.visor.setText(text + "+")

    def funcao_subtracao(self):
        text = self.visor.text()
        self.visor.setText(text + "-")

    def funcao_multiplicacao(self):
        text = self.visor.text()
        self.visor.setText(text + "*")

    def funcao_divisao(self):
        text = self.visor.text()
        self.visor.setText(text + "/")

    def funcao_limpar(self):
        self.visor.setText("")

    def funcao_deletar(self):
        text = self.visor.text()
        self.visor.setText(text[:len(text) - 1])

    def funcao_igualar(self):
        text = self.visor.text()
        try:
            res = eval(text)
            self.visor.setText(str(res))
        except:
            self.visor.setText("Erro na entrada!")

    def retranslateUi(self, Calculadora):
        _translate = QtCore.QCoreApplication.translate
        Calculadora.setWindowTitle(_translate("Calculadora", "Calculadora"))
        self.botao_dividir.setText(_translate("Calculadora", "÷"))
        self.botao_dividir.setShortcut(_translate("Calculadora", "/"))
        self.botao_desligar.setText(_translate("Calculadora", "OFF"))
        self.botao_8.setText(_translate("Calculadora", "8"))
        self.botao_8.setShortcut(_translate("Calculadora", "8"))
        self.botao_2.setText(_translate("Calculadora", "2"))
        self.botao_2.setShortcut(_translate("Calculadora", "2"))
        self.botao_6.setText(_translate("Calculadora", "6"))
        self.botao_6.setShortcut(_translate("Calculadora", "6"))
        self.botao_multiplicar.setText(_translate("Calculadora", "x"))
        self.botao_multiplicar.setShortcut(_translate("Calculadora", "*"))
        self.botao_clear.setText(_translate("Calculadora", "Clear"))
        self.botao_3.setText(_translate("Calculadora", "3")) 
        self.botao_3.setShortcut(_translate("Calculadora", "3"))
        self.botao_ponto.setText(_translate("Calculadora", "."))
        self.botao_ponto.setShortcut(_translate("Calculadora", "."))
        self.botao_subtrair.setText(_translate("Calculadora", "-"))
        self.botao_subtrair.setShortcut(_translate("Calculadora", "-"))
        self.botao_7.setText(_translate("Calculadora", "7"))
        self.botao_7.setShortcut(_translate("Calculadora", "7"))
        self.botao_9.setText(_translate("Calculadora", "9"))
        self.botao_9.setShortcut(_translate("Calculadora", "9"))
        self.botao_0.setText(_translate("Calculadora", "0"))
        self.botao_0.setShortcut(_translate("Calculadora", "0"))
        self.botao_somar.setText(_translate("Calculadora", "+"))
        self.botao_somar.setShortcut(_translate("Calculadora", "+"))
        self.botao_igual.setText(_translate("Calculadora", "="))
        self.botao_igual.setShortcut(_translate("Calculadora", "="))
        self.botao_4.setText(_translate("Calculadora", "4"))  
        self.botao_4.setShortcut(_translate("Calculadora", "4"))
        self.botao_5.setText(_translate("Calculadora", "5"))
        self.botao_5.setShortcut(_translate("Calculadora", "5"))
        self.visor.setText(_translate("Calculadora", "0"))
        self.botao_1.setText(_translate("Calculadora", "1"))
        self.botao_1.setShortcut(_translate("Calculadora", "1"))
        self.botao_delete.setText(_translate("Calculadora", "Delete"))
        self.botao_delete.setShortcut(_translate("Calculadora", "Backspace"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Calculadora()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
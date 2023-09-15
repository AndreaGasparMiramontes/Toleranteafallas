# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 622)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(530, 20, 121, 16))
        self.plainTextEdit_procesos = QPlainTextEdit(self.tab)
        self.plainTextEdit_procesos.setObjectName(u"plainTextEdit_procesos")
        self.plainTextEdit_procesos.setGeometry(QRect(440, 50, 311, 441))
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 401, 211))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 2, 2, 1, 1)

        self.lineEdit_num = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_num.setObjectName(u"lineEdit_num")

        self.gridLayout_4.addWidget(self.lineEdit_num, 4, 1, 1, 3)

        self.spinBox = QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_4.addWidget(self.spinBox, 2, 3, 1, 1)

        self.lineEdit_nombre = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")

        self.gridLayout_4.addWidget(self.lineEdit_nombre, 1, 1, 1, 3)

        self.spinBox_2 = QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_4.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.spinBox_tiempo = QSpinBox(self.gridLayoutWidget)
        self.spinBox_tiempo.setObjectName(u"spinBox_tiempo")
        self.spinBox_tiempo.setMinimum(1)

        self.gridLayout_4.addWidget(self.spinBox_tiempo, 3, 1, 1, 3)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton_registrar = QPushButton(self.gridLayoutWidget)
        self.pushButton_registrar.setObjectName(u"pushButton_registrar")

        self.gridLayout_4.addWidget(self.pushButton_registrar, 5, 0, 1, 4)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 210))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 46, 431, 463))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_transcurrido = QLCDNumber(self.layoutWidget)
        self.lcdNumber_transcurrido.setObjectName(u"lcdNumber_transcurrido")
        self.lcdNumber_transcurrido.setLayoutDirection(Qt.LeftToRight)
        self.lcdNumber_transcurrido.setDigitCount(3)
        self.lcdNumber_transcurrido.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_transcurrido, 8, 2, 1, 1)

        self.plainTextEdit_proejecucion = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_proejecucion.setObjectName(u"plainTextEdit_proejecucion")

        self.gridLayout.addWidget(self.plainTextEdit_proejecucion, 8, 0, 2, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)

        self.lcdNumber_restante = QLCDNumber(self.layoutWidget)
        self.lcdNumber_restante.setObjectName(u"lcdNumber_restante")
        self.lcdNumber_restante.setDigitCount(3)
        self.lcdNumber_restante.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdNumber_restante, 9, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 3)

        self.tableWidget_lote = QTableWidget(self.layoutWidget)
        self.tableWidget_lote.setObjectName(u"tableWidget_lote")

        self.gridLayout.addWidget(self.tableWidget_lote, 5, 0, 1, 3)

        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(453, 46, 311, 463))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.tableWidget_terminados = QTableWidget(self.layoutWidget1)
        self.tableWidget_terminados.setObjectName(u"tableWidget_terminados")

        self.verticalLayout_2.addWidget(self.tableWidget_terminados)

        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 751, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber_global = QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_global.setObjectName(u"lcdNumber_global")
        self.lcdNumber_global.setDigitCount(3)
        self.lcdNumber_global.setProperty("intValue", 0)

        self.horizontalLayout.addWidget(self.lcdNumber_global)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.label_pendientes = QLabel(self.horizontalLayoutWidget)
        self.label_pendientes.setObjectName(u"label_pendientes")

        self.horizontalLayout.addWidget(self.label_pendientes)

        self.label_13 = QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.spinBox_procesos = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_procesos.setObjectName(u"spinBox_procesos")
        self.spinBox_procesos.setMinimum(1)

        self.horizontalLayout.addWidget(self.spinBox_procesos)

        self.pushButton_iniciar = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_iniciar.setObjectName(u"pushButton_iniciar")

        self.horizontalLayout.addWidget(self.pushButton_iniciar)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Procesos registrados", None))
        self.comboBox.setCurrentText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tiempo max estimado", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nombre programador", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n a realizar", None))
        self.pushButton_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de programa", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Informacion del proceso", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tiempo transcurrido en ejecucion", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tiempo restante a ejecutar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lote en ejecuci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Procesos terminados", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tiempo Global", None))
        self.label_12.setText("")
        self.label_pendientes.setText(QCoreApplication.translate("MainWindow", u"Lotes pendientes : ", None))
        self.label_13.setText("")
        self.pushButton_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar la simulaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Simulaci\u00f3n", None))
    # retranslateUi

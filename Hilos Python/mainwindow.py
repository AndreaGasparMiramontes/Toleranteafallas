from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QGraphicsScene, QDialog
from PySide6.QtCore import Slot, QEventLoop
from PySide6.QtGui import QPen, QColor, QTransform

from lote import Lote
from proceso import Proceso
from ui_mainwindow import Ui_MainWindow

from threading import Thread
import time
import random
import keyboard


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.__lotes = []

        self.lote = Lote()

        self.__terminados = []

        self.id = 0

        self.operaciones = ['+','-','*','/','%']

        self.interrupcion = False
        self.error = False
        self.pausa = False
        self.continuar = True


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.scene = QGraphicsScene()
        # self.ui.graphicsView.setScene(self.scene)

        self.ui.pushButton_registrar.clicked.connect(self.click_registrar)
        self.ui.pushButton_iniciar.clicked.connect(self.simulacion)

    def registrar_random(self):
        id = self.id
        self.id = self.id+1
        programador = ""
        num1 = random.randint(0,99)
        op = self.operaciones[random.randint(0,4)]
        num2 = random.randint(0,99)
        tiempo = random.randint(7,18)

        proceso = Proceso(id,programador,num1,op,num2,tiempo)

        if(self.lote.__len__()<3):
            self.lote.agregar_final(proceso)
            print(self.__lotes.__len__())
        else:
            self.__lotes.append(self.lote)
            self.lote = Lote()
            self.lote.agregar_final(proceso)
    
    @Slot()
    def click_registrar(self):
        id = self.ui.lineEdit_num.text()
        programador = self.ui.lineEdit_nombre.text()
        num1 = self.ui.spinBox_2.value()
        op = self.ui.comboBox.currentData()
        num2 = self.ui.spinBox.value()
        tiempo = self.ui.spinBox_tiempo.value()

        proceso = Proceso(id,programador,num1,op,num2,tiempo)

        if(self.lote.__len__()<3):
            self.lote.agregar_final(proceso)
            print(self.__lotes.__len__())
        else:
            self.__lotes.append(self.lote)
            self.lote = Lote()
            self.lote.agregar_final(proceso)
        self.mostrar_procesos()

    @Slot()
    def mostrar_procesos(self):
        self.ui.plainTextEdit_procesos.clear()
        c = 1
        for l in self.__lotes:
            imp = "Lote" + str(c) + ":\n" + str(l)
            self.ui.plainTextEdit_procesos.insertPlainText(imp)   
            c = c+1
        imp = "Lote" + str(c) +":\n" + str(self.lote)
        self.ui.plainTextEdit_procesos.insertPlainText(imp)

    @Slot()
    def simulacion(self):
        self.continuar = True
        push_key = Thread(target=self.get_key)
        push_key.start()
        actualizar = Thread(target=self.simul)
        actualizar.start()
        #push_key.join()
        #actualizar.join()


    @Slot()
    def simul(self):
        ##generar procesos random:
        cantidad = self.ui.spinBox_procesos.value()
        self.lote = Lote()
        self.__lotes.clear()
        self.__terminados.clear()
        for a in range (0,cantidad):
            self.registrar_random()
        self.__lotes.append(self.lote)
        ##inicia el proceso:
        begging = time.time()
        t_global = 0
        pendientes = self.__lotes.__len__()
        self.ui.lcdNumber_global.display(t_global.__round__())
        for lote in self.__lotes:
            self.ui.label_pendientes.setText("Lotes pendientes: " + str(pendientes-1))
            self.lote = lote
            self.mostrar_tabla()
            for proceso in lote:
                print("inicia conteo regresivo")
                self.ui.plainTextEdit_proejecucion.clear()
                self.ui.plainTextEdit_proejecucion.insertPlainText(str(proceso))
                t_restante = proceso.restante
                for i in range (0,proceso.restante):
                    while(self.pausa):
                        if keyboard.is_pressed('c'):
                            self.pausa = False
                    if(self.interrupcion == True):
                        proceso.set_time(t_restante)
                        lote.agregar_final(proceso)
                        #lote.eliminar(proceso)
                        self.lote = lote
                        self.ui.tableWidget_lote.removeRow(0)
                        
                        #self.mostrar_tabla()
                        #actualizar_tabla = Thread(target=self.mostrar_tabla)
                        #actualizar_tabla.start()
                        #actualizar_tabla.join()
                        break
                    if(self.error == True):
                        self.error = False
                        proceso.set_error()
                        break
                    self.ui.lcdNumber_transcurrido.display(i)
                    self.ui.lcdNumber_restante.display(t_restante)
                    time.sleep(1)
                    t_restante = t_restante - 1
                    finish = time.time()
                    current = finish-begging
                    self.ui.lcdNumber_global.display(current.__round__())
                    #self.ui.tabWidget.repaint()
                if (self.interrupcion == False):
                    self.__terminados.append(proceso)
                    self.mostrar_terminados()
                    self.ui.tableWidget_lote.removeRow(0)
                else:
                    rows = self.ui.tableWidget_lote.rowCount()
                    self.ui.tableWidget_lote.setRowCount(rows+1)
                    id_widget = QTableWidgetItem(str(proceso.id))
                    tiempo_widget = QTableWidgetItem(str(proceso.tiempo))
                    restante_widget = QTableWidgetItem(str(proceso.restante))


                    self.ui.tableWidget_lote.setItem(rows, 0, id_widget)
                    self.ui.tableWidget_lote.setItem(rows, 1, tiempo_widget)
                    self.ui.tableWidget_lote.setItem(rows, 2, restante_widget)
                    self.interrupcion = False
            pendientes = pendientes-1
        finish = time.time()
        self.continuar = False
        print(finish-begging)

    def mostrar_tabla(self):
        self.ui.tableWidget_lote.clear()
        self.ui.tableWidget_lote.setColumnCount(3)
        headers = ["Numero de programa", "Max esperado","Tiempo restante"]
        self.ui.tableWidget_lote.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget_lote.setRowCount(len(self.lote))
        row:int = 0
        for process in self.lote:
            id_widget = QTableWidgetItem(str(process.id))
            tiempo_widget = QTableWidgetItem(str(process.tiempo))
            restante_widget = QTableWidgetItem(str(process.restante))


            self.ui.tableWidget_lote.setItem(row, 0, id_widget)
            self.ui.tableWidget_lote.setItem(row, 1, tiempo_widget)
            self.ui.tableWidget_lote.setItem(row, 2, restante_widget)

            row = row+1

    def mostrar_terminados(self):
        self.ui.tableWidget_terminados.setColumnCount(3)
        headers = ["Numero de programa", "Operacion","Resultado"]
        self.ui.tableWidget_terminados.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget_terminados.setRowCount(len(self.__terminados))
        row = 0
        for proceso in self.__terminados:
            id_widget = QTableWidgetItem(str(proceso.id))
            operacion_widget = QTableWidgetItem(str(proceso.operacion))
            resultado_widget = QTableWidgetItem(str(proceso.resultado))


            self.ui.tableWidget_terminados.setItem(row, 0, id_widget)
            self.ui.tableWidget_terminados.setItem(row, 1, operacion_widget)
            self.ui.tableWidget_terminados.setItem(row, 2, resultado_widget)

            row = row+1

    def get_key(self):
        while(self.continuar):
            if keyboard.is_pressed('i') and self.interrupcion != True:
                print("i presionada")
                self.interrupcion = True
            elif keyboard.is_pressed('e') and self.error != True:
                print("e presionada")
                self.error = True
            elif keyboard.is_pressed('p') and self.pausa != True:
                self.pausa = True

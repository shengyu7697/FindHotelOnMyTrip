#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QCompleter
from PyQt5.QtCore import QStringListModel
from ui.gui import Ui_MainWindow
from findAgoda import searchAgoda, subDate

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        app_root = os.path.dirname(os.path.abspath(sys.argv[0]))
        path = os.path.join(app_root, 'ui', 'images', 'icon.png')
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowTitle('FindAgoda-gui')
        self.ui.statusbar.showMessage('Ready.')

        self.setMenuAction()
        self.setConnections()
        self.setCompleter(self.ui.lineEditHotel)
        self.initTable()

        self.rowcount = 0
        self.ui.tableWidget.setRowCount(0)
        self.ui.buttonSearch.setEnabled(False)

        self.show()

    def setMenuAction(self):
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionLicense.triggered.connect(self.showLicense)
        self.ui.actionAbout.triggered.connect(self.showAbout)

    def showLicense(self):
        QtWidgets.QMessageBox.information(self, 'License', '')

    def showAbout(self):
        QtWidgets.QMessageBox.information(self, 'About', '')

    def setConnections(self):
        self.ui.buttonAdd.clicked.connect(self.addBtnEvent)
        self.ui.buttonDelete.clicked.connect(self.deleteBtnEvent)
        self.ui.buttonClear.clicked.connect(self.clearBtnEvent)
        self.ui.buttonSearch.clicked.connect(self.searchBtnEvent)
        self.ui.buttonExit.clicked.connect(self.close)

    def setCompleter(self, lineEdit):
        self.getHotelData()
        model = QStringListModel()
        model.setStringList(self.hotelStringList)
        completer = QCompleter()
        completer.setModel(model)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        lineEdit.setCompleter(completer)

    def getHotelData(self):
        # TODO load string list from file
        self.hotelStringList = ['東橫INN博多口站前 (Toyoko Inn Hakata-guchi Ekimae)', \
                                '東橫INN博多口站前2 (Toyoko Inn Hakata-guchi Ekimae No.2)', \
                                '東橫INN博多站南 (Toyoko Inn Hakata-eki Minami)', \
                                '東橫INN博多站前祇園 (Toyoko Inn Hakata Ekimae Gion)', \
                                '東橫INN福岡天神 (Toyoko Inn Fukuoka Tenjin)', \
                                '東橫INN博多西中州 (Toyoko Inn Hakata Nishi-nakasu)', \
                                '博多超級酒店 (Super Hotel Hakata)', \
                                '博多城市Sutton飯店 (Sutton Hotel Hakata City)', \
                                'AreaOne飯店 - 博多 (Hotel Areaone Hakata)', \
                                'APA飯店 - 名古屋錦EXCELLENT (APA Hotel Nagoya-Nishiki Excellent)', \
                                'Dormy Inn高階飯店 - 名古屋榮天然溫泉錦鯱之湯 (Dormy Inn Premium Nagoya Sakae Natural Hot Spring)', \
                                ]
        self.hotelUrlStringList = ['toyoko-inn-hakata-guchi-ekimae', \
                                   'toyoko-inn-hakata-guchi-ekimae-no-2', \
                                   'toyoko-inn-hakata-eki-minami', \
                                   'toyoko-inn-hakata-ekimae-gion', \
                                   'toyoko-inn-fukuoka-tenjin', \
                                   'toyoko-inn-hakata-nishi-nakasu', \
                                   'super-hotel-hakata', \
                                   'sutton-hotel-hakata-city', \
                                   'hotel-areaone-hakata', \
                                   'apa-hotel-nagoya-nishiki-excellent', \
                                   'dormy-inn-premium-nagoya-sakae-natural-hot-spring', \
                                   ]
        self.hotelCityStringList = ['fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'fukuoka-jp', \
                                    'nagoya-jp', \
                                   'nagoya-jp', \
                                   ]

    def searchHotelUrl(self, hotelString):
        for i in range(len(self.hotelStringList)):
            if (self.hotelStringList[i] == hotelString):
                return self.hotelUrlStringList[i]
        return ""

    def searchHotelCity(self, hotelString):
        for i in range(len(self.hotelStringList)):
            if (self.hotelStringList[i] == hotelString):
                return self.hotelCityStringList[i]
        return ""

    def initTable(self):
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setColumnWidth(0, 110)
        self.ui.tableWidget.setColumnWidth(1, 90)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 50)
        self.ui.tableWidget.setColumnWidth(4, 80)
        self.ui.tableWidget.setColumnWidth(5, 60)
        self.ui.tableWidget.setColumnWidth(6, 60)
        self.ui.tableWidget.setColumnWidth(7, 50)

    def insertTable(self, i, hotel, checkIn, checkOut, days, city, rooms, adults, childs):
        self.ui.tableWidget.insertRow(i)
        self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(hotel))
        self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(checkIn))
        self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(checkOut))
        self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(days))
        self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(city))
        self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(rooms))
        self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(adults))
        self.ui.tableWidget.setItem(i, 7, QTableWidgetItem(childs))

    def addBtnEvent(self):
        print('addBtnEvent')
        hotel_name = self.ui.lineEditHotel.text()
        start_date = self.ui.lineEditCheckIn.text()
        end_date = self.ui.lineEditCheckOut.text()
        city = self.searchHotelCity(self.ui.lineEditHotel.text())
        rooms = self.ui.comboBoxRooms.currentText()
        adults = self.ui.comboBoxAdults.currentText()
        childs = self.ui.comboBoxChilds.currentText()

        self.insertTable(self.rowcount, hotel_name, \
                         start_date, end_date, \
                         subDate(start_date, end_date), city, \
                         rooms, adults, childs)
        self.ui.tableWidget.selectRow(self.rowcount)
        #self.ui.tableWidget.verticalScrollBar().setSliderPosition(self.ui.tableWidget.verticalScrollBar().maximum())
        self.rowcount += 1
        self.ui.buttonSearch.setEnabled(True)

    def deleteBtnEvent(self):
        if (self.rowcount > 0):
            self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())
            self.rowcount -= 1

        if (self.rowcount == 0):
            self.ui.buttonSearch.setEnabled(False)

    def clearBtnEvent(self):
        self.ui.tableWidget.setRowCount(0)
        self.rowcount = 0
        self.ui.buttonSearch.setEnabled(False)

    def searchBtnEvent(self):
        print('searchBtnEvent')
        for i in range(self.ui.tableWidget.rowCount()):
            hotel_name = self.searchHotelUrl(self.ui.tableWidget.item(i, 0).text())
            start_date = self.ui.tableWidget.item(i, 1).text()
            end_date = self.ui.tableWidget.item(i, 2).text()
            los = self.ui.tableWidget.item(i, 3).text()
            city = self.ui.tableWidget.item(i, 4).text()
            rooms = self.ui.tableWidget.item(i, 5).text()
            adults = self.ui.tableWidget.item(i, 6).text()
            childs = self.ui.tableWidget.item(i, 7).text()
            hotel_url = 'https://www.agoda.com/zh-tw/' + hotel_name + '/hotel/' + city + '.html'
            searchAgoda(hotel_url, start_date, end_date, rooms, adults, childs, los)
            print('Hotel URL: ' + hotel_url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())

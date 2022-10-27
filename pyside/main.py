import sys
import time

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pyqtgraph as pg
from mainSystem import Ui_Form as main_ui
from chartWin import Ui_Form as chart_ui
from systemSetting import Ui_Form as setting_ui
from home1System import Ui_Form as home1_ui
from home2System import Ui_Form as home2_ui
from home3System import Ui_Form as home3_ui
import paho.mqtt.publish as publish
from io import open as op
import threading
from sub import Sub

broker = 'broker.emqx.io'
port = 1883
topic = "/pyside/mqtt"


class MainWin(QWidget, main_ui):

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.sub = Sub()
        self.search_btn.clicked.connect(self.gotoChart)
        self.jump_btn.clicked.connect(self.gotoSetting)
        self.home1_btn.clicked.connect(self.gotoHome1)
        self.home2_btn.clicked.connect(self.gotoHome2)
        self.home3_btn_2.clicked.connect(self.gotoHome3)
        self.sub_thread()
        self.mutex = threading.Lock()

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()

    def gotoHome1(self):
        self.settingwin = Home1Win()
        self.settingwin.show()
        self.close()

    def gotoHome2(self):
        self.settingwin = Home2Win()
        self.settingwin.show()
        self.close()

    def gotoHome3(self):
        self.settingwin = Home3Win()
        self.settingwin.show()
        self.close()

    def sub_thread(self):
        t1 = threading.Thread(target=self.run_sub)
        t2 = threading.Thread(target=self.sub_text)
        t1.start()
        t2.start()

    def run_sub(self):
        # self.sub = Sub()
        # self.sub.run()
        self.sub.run()

    def sub_text(self):
        data = ''
        while True:
            if data != self.sub.msg and data != None:
                data = self.sub.msg
                try:
                    name = data.split(":")[0].strip()
                    num = data.split(":")[1].strip()
                except:
                    continue
                self.mutex.acquire()
                with op("data", mode="a") as fp:
                    fp.seek(0, 2)
                    fp.write(f"{name},{num},{time.time()}\n")
                self.mutex.release()


class Home1Win(QWidget, home1_ui):

    def __init__(self):
        super(Home1Win, self).__init__()
        self.setupUi(self)
        self.search_btn.clicked.connect(self.gotoMain)
        self.jump_btn.clicked.connect(self.gotoChart)
        self.jump_btn_2.clicked.connect(self.gotoSetting)
        self.tem_control()
        self.hum_control()
        self.ch_control()
        self.pm_control()
        self.new_ch_control()
        self.mutex = threading.Lock()
        self.funct_name = {
            "temperature": 1,
            "humidity": 2,
            "ch4": 3,
        }
        self.all_funct = {
            1: self.tem_control,
            2: self.hum_control,
            3: self.ch_control,
        }

        self.set_num()

    def tem_control(self, num=0):
        self.temprature_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.temprature_lcd.setDigitCount(3)
        self.temprature_lcd.display(num)

    def hum_control(self, num=0):
        self.humidity_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.humidity_lcd.setDigitCount(3)
        self.humidity_lcd.display(num)

    def ch_control(self, num=0):
        self.ch4_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.ch4_lcd.setDigitCount(3)
        tem_num = 1
        self.ch4_lcd.display(num)

    def pm_control(self, num=0):
        self.ch4_lcd_2.setSegmentStyle(QLCDNumber.Flat)
        self.ch4_lcd_2.setDigitCount(3)
        tem_num = 123
        self.ch4_lcd_2.display(num)

    def new_ch_control(self, num=0):
        self.ch4_lcd_3.setSegmentStyle(QLCDNumber.Flat)
        self.ch4_lcd_3.setDigitCount(3)
        self.ch4_lcd_3.display(num)

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()

    def set_num(self):
        with op("data", mode="r") as fp:
            alldata = fp.readlines()
            for i in range(len(alldata)):
                alldata[i] = alldata[i].strip()
            realdata = alldata[::-1]
            for i in range(3):
                linedata = realdata[i]
                name = linedata.split(",")[0]
                num = linedata.split(",")[1].split(",")[0]
                print(name)
                print(num)
                self.all_funct.get(self.funct_name.get(name))(num)


class Home2Win(QWidget, home2_ui):

    def __init__(self):
        super(Home2Win, self).__init__()
        self.setupUi(self)
        self.main_btn.clicked.connect(self.gotoMain)
        self.jump_btn.clicked.connect(self.gotoChart)
        self.jump_btn_2.clicked.connect(self.gotoSetting)

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()


class Home3Win(QWidget, home3_ui):

    def __init__(self):
        super(Home3Win, self).__init__()
        self.setupUi(self)
        self.home_btn.clicked.connect(self.gotoMain)
        self.jump_btn.clicked.connect(self.gotoChart)
        self.jump_btn_2.clicked.connect(self.gotoSetting)

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()


class ChartWin(QWidget, chart_ui):

    def __init__(self):
        super(ChartWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gotoMain)
        self.pushButton_2.clicked.connect(self.gotoSetting)
        self.pw = pg.PlotWidget()
        self.pw.setTitle('数据动态曲线', color='black', size='12pt')
        self.pw.setLabel('left', '温度、湿度、甲烷', color='black')
        self.pw.setLabel('bottom', '时间', color='black')
        self.pw.setBackground('#f0ffff')
        self.pw.showGrid(x=True, y=True)
        self.horizontalLayout.addWidget(self.pw)
        self.draw_lines()
        self.mutex = threading.Lock()
        self.parameter = {
            "temperature": 1,
            "humidity": 2,
            "ch4": 3,
        }
        self.temperature = []
        self.humidity = []
        self.ch4 = []

    def draw_lines(self, times=None, temperature=None, humidity=None, ch4=None):
        # 通过调用该方法，传递参数，来实现动态更新
        # 下面是默认的测试数据，删除就行
        times = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        temperature = [30, 32, 24, 31, 19, 12, 20, 28, 38, 30]
        humidity = [10, 12, 13, 9, 3, 14, 17, 12, 11, 10]
        ch4 = [1, 2, 2.4, 1.2, 1.8, 1.3, 2.5, 3.1, 4.6, 3.4]

        # self.mutex.acquire()
        #
        # with os.open("filedata", mode="r") as fp:
        #     fp.seek(0, 0)
        #     alldata = fp.readlines()
        #     for i in range(len(alldata)):
        #         alldata[i] = alldata[i].strip()
        #     realdata = alldata[::-1]
        #     for i in range(10):
        #         linedata = realdata
        #         name = linedata.split(",")[0]
        #         num = linedata.split(",")[0].split(",")[0]
        #         time = linedata.split(",")[0].split(",")[1]
        #
        #
        # self.mutex.release()
        self.pw.plot(times, temperature, pen=pg.mkPen(width=3, color='#3fc5c6'))
        self.pw.plot(times, humidity, pen=pg.mkPen(width=3, color='#35d0a6'))
        self.pw.plot(times, ch4, pen=pg.mkPen(width=3, color='#bce49e'))

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()

    def sub_thread(self):
        t1 = threading.Thread(target=self.run_sub)
        t1.start()
        t2 = threading.Thread(target=self.sub_text)
        t2.start()

    # def run_sub(self):
    #     # self.sub = Sub()
    #     # self.sub.run()
    #     self.sub.run()
    #
    # def sub_text(self):
    #     data = ''
    #     while True:
    #         if data != self.sub.msg and data != None:
    #             data = self.sub.msg
    #             try:
    #                 name = data.split(":")[0]
    #                 num = data.split(":")[1]
    #             except:
    #                 continue
    #             self.mutex.acquire()
    #             with os.open("filedata", mode="w") as fp:
    #                 fp.seek(0, 2)
    #                 fp.write(f"{name},{num},{time.time()}\n")
    #             self.mutex.release()


class SettingWin(QWidget, setting_ui):

    def __init__(self):
        super(SettingWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gotoMain)
        self.pushButton_6.clicked.connect(self.gotoChart)

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()


# def run_sub():
#     sub = Sub()
#     sub.run()
#     # path = r'python E:\PycharmProjects\hospitalproject\室内环境监测系统\sub.py'
#     # os.system(path)

# def run_thread():
#     t1 = threading.Thread(target=run_sub)
#     t1.start()

if __name__ == '__main__':
    # run_thread()
    app = QApplication(sys.argv)
    mywin = MainWin()
    mywin.show()
    sys.exit(app.exec_())
